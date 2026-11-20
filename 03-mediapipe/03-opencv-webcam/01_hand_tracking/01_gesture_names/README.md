# ✋ Activity 01 — Gesture Names

## 🎯 Objective

In this activity, I extended the existing hand-tracking application to display a gesture name in the webcam preview. The first programming activity in the supplied hand-tracking document asks for a dictionary that translates raised-finger counts into names. This version uses English labels and retains the baseline camera processing, landmarks, fingertip smoothing and session recording.

## 📂 Project Structure

```text
03-mediapipe/
├── .venv/                         Existing shared Python environment
├── requirements.txt               Shared pinned dependencies
└── 03-opencv-webcam/
    └── 01_hand_tracking/
        ├── hand_tracking.py       Original application
        ├── README.md              Original application guide
        ├── hand_landmarker.task   Shared detection model
        └── 01_gesture_names/
            ├── gesture_tracking.py  Executable activity
            └── README.md            This guide
```

The two activity files are self-contained for running and understanding the exercise. The script reuses the model in its parent directory and creates `gesture_camera.json` beside itself after a completed session. The original application is unchanged.

## 🖐️ Gesture Mapping

The document lists six gesture names for five counts, from zero to four. Peace and the Rock hand sign both use two raised fingers, so a count alone cannot distinguish them. The agreed solution keeps all six names and checks finger arrangements only when the count is two.

| Raised fingers, excluding the thumb | Arrangement | Preview name |
|---|---|---|
| 0 | All four counted fingers lowered | Fist |
| 1 | Any one counted finger raised | One |
| 2 | Index and middle raised; ring and little lowered | Peace |
| 2 | Index and little raised; middle and ring lowered | Rock hand sign |
| 2 | Any other pair raised | Two fingers |
| 3 | Any three counted fingers raised | Three fingers |
| 4 | All four counted fingers raised | Open hand |

`GESTURES` has one entry for each count. Its entry for `2` contains a second dictionary with the Peace and Rock hand sign arrangements. Boolean tuples follow the order **index, middle, ring, little**; `True` means raised. A lookup with `.get()` supplies **Two fingers** for the other arrangements. No duplicate count key overwrites a name.

The thumb is ignored throughout: **Fist** means zero counted fingers, and **Open hand** means four, regardless of thumb position. These are simple exercise labels rather than complete pose descriptions.

## ⚙️ How It Works

1. **Capture and mirror.** `track_hands()` opens camera `0`, resizes frames to 640 × 480 when necessary and flips each frame horizontally once. It converts BGR to RGB colour channels before MediaPipe detection.
2. **Detect and measure.** MediaPipe finds up to one hand. `annotate_hand()` draws its landmarks and compares fingertip/joint pairs `(8, 6)`, `(12, 10)`, `(16, 14)` and `(20, 18)`. A tip with a smaller image `y` coordinate than its joint counts as raised; equal heights count as lowered.
3. **Recognise and label.** `recognise_gesture()` sums the four Boolean states and looks up `GESTURES`, checking arrangements for count two. The preview shows, for example, `Gesture: Peace | Fingers: 2`. Each frame starts with **No hand detected**, preventing a stale gesture when detection is lost.
4. **Smooth and record.** A yellow ring follows the average of the last five detected index-fingertip positions. `FrameRecord` stores the current, unsmoothed coordinates, count and gesture. As in the baseline, the smoothing history survives gaps in detection.
5. **Finish and export.** `main()` initialises and closes the detector. The camera loop releases the webcam and closes windows in `finally`; `summarise_and_save()` prints the baseline statistics and writes the records to JSON.

Detection happens on the mirrored image before drawing. Landmarks, the yellow ring and recorded positions therefore use the same coordinates as the preview. No second flip is applied to the overlays. Horizontal mirroring changes left and right without changing the vertical comparisons used to count fingers.

## 💻 Shared Environment

Use the existing **`03-mediapipe/.venv`**, verified with 64-bit Python **3.13.15**. Required installed packages are MediaPipe **1.2.2**, OpenCV **5.0.0.93** (`cv2` reports **5.0.0**), NumPy **2.5.4** and pandas **3.1.1**. The shared requirements contain both OpenCV distributions already used by the baseline. Imports and `pip check` passed; no packages were installed or changed.

To check dependencies from the repository root:

```powershell
& ".\03-mediapipe\.venv\Scripts\python.exe" -m pip check
```

If a required module is missing, use that interpreter to install only the missing package at its version in `03-mediapipe/requirements.txt`. No separate environment is needed. A graphical desktop and an accessible webcam are required for the live preview.

`prepare_model()` locates `../hand_landmarker.task` relative to the script. If missing, it downloads the baseline model from Google into that parent directory; this needs internet access and write permission there. An existing model is reused without downloading.

## 🚀 Running the Application

From the **repository root**, run:

```powershell
& ".\03-mediapipe\.venv\Scripts\python.exe" ".\03-mediapipe\03-opencv-webcam\01_hand_tracking\01_gesture_names\gesture_tracking.py"
```

From the **`01_gesture_names` activity directory**, run:

```powershell
& "..\..\..\.venv\Scripts\python.exe" ".\gesture_tracking.py"
```

Hold one hand upright, fully visible and well lit in the **Gesture tracking** window. Raise or lower fingers to change its label. Press **Q** with the preview in focus, close the preview, or press **Ctrl+C** in the terminal to stop. The session also ends after **600 captured frames**, including frames without a hand.

### Session results

Both launch locations write to **`03-mediapipe/03-opencv-webcam/01_hand_tracking/01_gesture_names/gesture_camera.json`**, relative to the repository root. The export path is based on the script's location, so changing the working directory does not move the output or overwrite the baseline export. Each session replaces the previous activity export. The repository's `.gitignore` excludes `gesture_camera.json` from Git tracking while retaining the local file.

Each detected frame produces `frame`, `handedness`, `index_x`, `index_y`, `raised_fingers` and `gesture`. Coordinates are measured in pixels from the mirrored image's top-left corner. No images or video are saved. Undetected frames produce no record; a completed session without detections exports `[]`. A capture or detection failure after collecting records attempts to save the partial session; a failure before any detection exits without exporting. The terminal prints the saved path and baseline count and fingertip statistics.

## ✅ Validation and Limitations

| Check | Actual result |
|---|---|
| Syntax, imports and dependency consistency | Passed; no installation required. |
| Existing model | Loaded successfully and processed a blank image with no detected hand. |
| All 16 finger arrangements | Passed with synthetic landmarks, including all six requested names and the fallback; thumb exclusion and equal-height comparisons also passed. |
| Preview processing | Simulated frames verified label changes, no-hand reset, a single horizontal flip before detection, RGB conversion and matching overlay coordinates. |
| Smoothing and export | Verified five-detection averaging, unsmoothed coordinates, JSON fields, empty exports and partial-session exports. |
| Controls and cleanup | Simulated Q, window closure, frame limit, read/detection failures and interruption passed resource-release checks. |
| Both documented launch commands | Reached model initialisation, then exited with the clear camera-unavailable message and status `1`. |
| Complete entry point with a simulated camera | Passed from both launch directories using the real model; verified resizing, the fixed export destination, cleanup and status `0`. All label widths also fit the preview. |

## 🔧 Troubleshooting

| Symptom | What to check |
|---|---|
| Camera unavailable or a frame cannot be read | Check the connection and Windows camera permissions for desktop apps; close other camera applications. If needed, change camera index `0` in `track_hands()`. |
| Interpreter, script or module cannot be found | Use the command matching your current directory and the existing shared environment. Check installed dependencies before installing anything. |
| Model cannot be loaded or downloaded | Check the parent model file. If it is missing, check internet access and write permission in `01_hand_tracking`. |
| Unexpected labels or no detection | Keep the hand upright and fully visible with good lighting. Peace and Rock require the specific arrangements in the mapping table. |
| Export cannot be saved | Check write access to `01_gesture_names`; the launch directory does not control the export location. |

Feel free to explore the dictionary and compare the live labels with the saved session records.
