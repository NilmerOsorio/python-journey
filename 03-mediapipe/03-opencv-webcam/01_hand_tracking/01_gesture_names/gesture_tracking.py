"""Recognise named gestures with the baseline hand tracker and export detections."""

from collections import deque
from http.client import HTTPException
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from typing import NamedTuple
from urllib.request import urlretrieve

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import pandas as pd


MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/"
    "hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
)
ACTIVITY_DIRECTORY = Path(__file__).resolve().parent
MODEL_PATH = ACTIVITY_DIRECTORY.parent / "hand_landmarker.task"
OUTPUT_PATH = ACTIVITY_DIRECTORY / "gesture_camera.json"
WINDOW_NAME = "Gesture tracking"
FRAME_SIZE = (640, 480)
MAX_FRAMES = 600
CONNECTIONS = (
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17),
)
FINGER_JOINTS = ((8, 6), (12, 10), (16, 14), (20, 18))
# Counts select names; only two raised fingers need an arrangement lookup.
# Tuple positions follow FINGER_JOINTS: index, middle, ring and little finger.
GESTURES = {
    0: "Fist",
    1: "One",
    2: {
        (True, True, False, False): "Peace",
        (True, False, False, True): "Rock hand sign",
    },
    3: "Three fingers",
    4: "Open hand",
}


class FrameRecord(NamedTuple):
    """Measurements for one detection, using the unsmoothed fingertip position."""

    frame: int
    handedness: str
    index_x: int
    index_y: int
    raised_fingers: int
    gesture: str


def prepare_model() -> Path:
    """Reuse the parent application's model, downloading it there if missing."""
    if not MODEL_PATH.is_file():
        print("Downloading the hand landmark model...")
        # Publish the model only after the entire download has succeeded.
        with TemporaryDirectory(dir=MODEL_PATH.parent) as directory:
            download = Path(directory) / MODEL_PATH.name
            try:
                urlretrieve(MODEL_URL, download)
            except (OSError, HTTPException) as error:
                raise RuntimeError(
                    f"Could not download the hand landmark model: {error}"
                ) from error
            download.replace(MODEL_PATH)
    return MODEL_PATH


def recognise_gesture(finger_states: tuple[bool, ...]) -> str:
    """Look up a count, distinguishing the two agreed two-finger arrangements."""
    raised = sum(finger_states)
    if raised == 2:
        # A count alone cannot distinguish Peace from the Rock hand sign.
        return GESTURES[raised].get(finger_states, "Two fingers")
    return GESTURES[raised]


def annotate_hand(
    frame: np.ndarray,
    result: vision.HandLandmarkerResult,
    frame_number: int,
    recent_tips: deque[tuple[int, int]],
) -> FrameRecord:
    """Draw the hand, recognise its gesture and smooth the index fingertip."""
    hand = result.hand_landmarks[0]
    height, width = frame.shape[:2]
    pixels = [(int(point.x * width), int(point.y * height)) for point in hand]
    for start, end in CONNECTIONS:
        cv2.line(frame, pixels[start], pixels[end], (0, 200, 0), 2)
    for point in pixels:
        cv2.circle(frame, point, 5, (0, 0, 255), -1)

    # Image y increases downwards: a smaller tip y means a raised finger.
    # The thumb is deliberately excluded, as in the original application.
    finger_states = tuple(hand[tip].y < hand[joint].y for tip, joint in FINGER_JOINTS)
    raised = sum(finger_states)
    gesture = recognise_gesture(finger_states)
    index_x, index_y = pixels[8]
    recent_tips.append((index_x, index_y))
    centre = (
        int(sum(x for x, _ in recent_tips) / len(recent_tips)),
        int(sum(y for _, y in recent_tips) / len(recent_tips)),
    )
    cv2.circle(frame, centre, 10, (0, 255, 255), 2)
    return FrameRecord(
        frame_number, result.handedness[0][0].category_name,
        index_x, index_y, raised, gesture,
    )


def track_hands(detector: vision.HandLandmarker, records: list[FrameRecord]) -> None:
    """Process up to 600 webcam frames, retaining detections across interruptions."""
    recent_tips = deque(maxlen=5)
    camera = cv2.VideoCapture(0)
    try:
        if not camera.isOpened():
            raise RuntimeError(
                "Could not open the default camera. Check its connection and permissions."
            )

        print("Looking for a hand. Press Q or close the preview to stop.")
        for frame_number in range(1, MAX_FRAMES + 1):
            success, frame = camera.read()
            if not success or frame is None:
                raise RuntimeError(f"Could not read frame {frame_number} from the camera.")

            # Retain the baseline preview dimensions before processing.
            if (frame.shape[1], frame.shape[0]) != FRAME_SIZE:
                frame = cv2.resize(frame, FRAME_SIZE)
            # Use the mirrored frame for detection, drawing and recorded coordinates.
            frame = cv2.flip(frame, 1)
            # MediaPipe expects RGB colour channels; OpenCV uses BGR.
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = detector.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb))
            # Reset every frame so a lost detection never leaves a stale name.
            label = "No hand detected"
            if result.hand_landmarks:
                record = annotate_hand(frame, result, frame_number, recent_tips)
                records.append(record)
                label = f"Gesture: {record.gesture} | Fingers: {record.raised_fingers}"

            cv2.putText(
                frame, label, (10, 28), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 255), 2, cv2.LINE_AA,
            )
            cv2.imshow(WINDOW_NAME, frame)
            key = cv2.waitKey(1) & 0xFF
            if key in (ord("q"), ord("Q")):
                break
            if cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


def summarise_and_save(records: list[FrameRecord]) -> None:
    """Retain the baseline statistics and export each detection with its gesture."""
    table = pd.DataFrame.from_records(records, columns=FrameRecord._fields)
    print(f"Frames with a detected hand: {len(table)}")
    print(f"DataFrame shape (rows, columns): {table.shape}")
    print(table.head(10).to_string(index=False))
    if not table.empty:
        print("\nFrame count by number of raised fingers:")
        print(table.groupby("raised_fingers")["frame"].count().to_string())
        mean_x, mean_y = table[["index_x", "index_y"]].mean()
        print(f"\nMean index fingertip (x, y): {mean_x:.1f}, {mean_y:.1f}")
    else:
        print("No fingertip positions to average.")
    print(f"Open-hand frames (four raised fingers): {(table.raised_fingers == 4).sum()}")
    table.to_json(OUTPUT_PATH, orient="records", force_ascii=False, indent=4)
    print(f"Saved {OUTPUT_PATH.resolve()}")


def main() -> int:
    """Run the local capture session and report any capture or export failure."""
    records: list[FrameRecord] = []
    exit_code = 0
    try:
        options = vision.HandLandmarkerOptions(
            base_options=python.BaseOptions(model_asset_path=str(prepare_model())),
            num_hands=1,
            min_hand_detection_confidence=0.5,
        )
        with vision.HandLandmarker.create_from_options(options) as detector:
            track_hands(detector, records)
    except KeyboardInterrupt:
        print("\nSession interrupted.")
        exit_code = 130
    except (OSError, RuntimeError, ValueError, cv2.error) as error:
        print(f"Gesture tracking failed: {error}", file=sys.stderr)
        if not records:
            return 1
        exit_code = 1

    try:
        summarise_and_save(records)
    except OSError as error:
        print(f"Could not save {OUTPUT_PATH}: {error}", file=sys.stderr)
        return 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
