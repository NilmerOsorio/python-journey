# ✋ Exercise 01 — Hand Tracking with MediaPipe and OpenCV

## 🎯 Objective

In this exercise, I adapted a Google Colab hand-tracking notebook to run directly on a computer with a webcam. OpenCV captures and displays the video, MediaPipe locates the hand, and pandas summarises what happened during the session.

The original reference was `MediaPipe_Mano_Camara_Colab.ipynb`, supplied during development. Its detection, finger-counting, smoothing and analysis workflow forms the basis of this application. Local camera capture and a desktop preview replace the notebook's browser camera controls.

## 📷 Features and Workflow

1. **Capture and mirror.** OpenCV opens the default webcam with `cv2.VideoCapture(0)` and resizes each frame to 640 × 480 pixels if needed. It flips the frame horizontally once with `cv2.flip(frame, 1)`, then converts it from BGR to RGB for MediaPipe. Moving your hand to your left moves it to the left in the preview.
2. **Locate the hand.** MediaPipe's Hand Landmarker processes one frame at a time, with a maximum of one hand and a minimum detection confidence of 0.5. The preview draws the 21 landmarks in red and connects them in green. The script records the handedness label supplied by MediaPipe.
3. **Count raised fingers.** A finger counts as raised when its tip appears above its middle joint in the image. The thumb is excluded, so the on-screen count ranges from zero to four. This rule works best with an upright hand.
4. **Follow the index fingertip.** A yellow ring marks the average fingertip position over the last five detections. The recorded coordinates are the fingertip's position in the current mirrored frame, in pixels measured from the top-left corner.
5. **Analyse the session.** The application collects detection records, displays statistics in the terminal and exports the results to JSON when the session ends.

The detector receives the mirrored image before any overlays are drawn. The landmarks, yellow ring and recorded coordinates therefore share the preview's coordinate system. The smoothing window retains its last positions while the hand is out of view.

## 📂 Project Structure

```text
03-mediapipe/
├── .venv/                      Shared Python environment
├── requirements.txt            Pinned dependencies for the MediaPipe exercises
└── 03-opencv-webcam/
    └── 01_hand_tracking/
        ├── README.md            Project guide
        ├── hand_tracking.py      Standalone webcam application
        ├── hand_landmarker.task  Model downloaded here if missing
        └── hand_camera.json      Generated when launched from this directory
```

The root `.gitignore` excludes `hand_camera.json` at the repository root and in this exercise directory, matching the two launch locations documented below.

### Main components

| Component | Responsibility |
|---|---|
| `prepare_model()` | Reuses the local model or downloads it before the session. |
| `track_hands()` | Captures and mirrors frames, runs detection, displays the preview and releases camera resources. |
| `annotate_hand()` | Draws the landmarks, counts raised fingers and smooths the index-fingertip position. |
| `FrameRecord` | Holds the measurements for one detected hand in a frame. |
| `summarise_and_save()` | Builds the pandas table, prints statistics and exports JSON. |
| `main()` | Configures MediaPipe and handles session interruptions and reported failures. |

## 💻 Development Environment

The project has been tested on Windows with PowerShell, **64-bit Python 3.13.15**, and a webcam accessible to desktop applications.

| Library | Pinned version | Purpose |
|---|---|---|
| MediaPipe | 1.2.2 | Detects hand landmarks and estimates handedness. |
| OpenCV (`opencv-python` and `opencv-contrib-python`) | 5.0.0.93 | Provides the `cv2` module for capture, image processing and the preview window. |
| NumPy | 2.5.4 | Provides the pixel arrays used by OpenCV and MediaPipe. |
| pandas | 3.1.1 | Builds the results table, calculates statistics and writes JSON. |

The complete shared dependency list, including supporting packages, is pinned in `03-mediapipe/requirements.txt`. The preview requires a local graphical desktop and a working webcam.

### Virtual environment and installation

From the repository root, use the interpreter in the existing shared environment. Calling it directly also works when PowerShell activation is unavailable.

```powershell
& ".\03-mediapipe\.venv\Scripts\python.exe" --version
& ".\03-mediapipe\.venv\Scripts\python.exe" -m pip --version
```

If dependencies are missing, install the pinned packages into that environment.

```powershell
& ".\03-mediapipe\.venv\Scripts\python.exe" -m pip install -r ".\03-mediapipe\requirements.txt"
& ".\03-mediapipe\.venv\Scripts\python.exe" -m pip check
```

The installation command reuses packages that already satisfy the pins. These commands use the existing `03-mediapipe/.venv` directly. If that folder is missing from a fresh checkout, restore or set up the shared MediaPipe environment before following this guide.

The script downloads the hand landmark model from Google when the model file is missing. That first download needs internet access and write access to the script's directory. Later sessions reuse the local file.

## ⚙️ Camera Configuration

The following settings are defined in `hand_tracking.py`.

| Setting | Current value and behaviour |
|---|---|
| `cv2.VideoCapture(0)` | Opens camera index `0`. If another connected camera is required, edit this index in `track_hands()`. |
| `FRAME_SIZE` | `(640, 480)`, the width and height used for processing and display. Captured frames are resized when needed. |
| `cv2.flip(frame, 1)` | Applies horizontal mirroring once, before colour conversion and detection. |
| `MAX_FRAMES` | `600`, the maximum number of captured frames per session. |
| `num_hands` | `1`, the maximum number of hands detected per frame. |
| `min_hand_detection_confidence` | `0.5`, the minimum detection confidence. |
| `deque(maxlen=5)` | Retains up to five detected fingertip positions for the yellow ring. |

MediaPipe uses its default `IMAGE` running mode through `detect()`. The stream is processed one image at a time. Session duration depends on the achieved frame rate.

## 🚀 Running the Application

From the **repository root**, run the following command.

```powershell
& ".\03-mediapipe\.venv\Scripts\python.exe" ".\03-mediapipe\03-opencv-webcam\01_hand_tracking\hand_tracking.py"
```

If PowerShell is already in **`01_hand_tracking`**, use the shorter command.

```powershell
& "..\..\.venv\Scripts\python.exe" ".\hand_tracking.py"
```

Hold one hand upright in the **Hand tracking** window and raise or lower individual fingers. To finish, press **Q** with the preview in focus, close the window, or press **Ctrl+C** in the terminal. The session stops automatically after 600 captured frames, including frames without a detection. On exit, the application releases the camera and closes the preview.

### Session results

The terminal shows the table dimensions and up to ten sample rows. For a session with detections, it also shows the frame count for each observed finger count, the mean index-fingertip position and the number of open-hand frames (all four counted fingers raised).

The script writes `hand_camera.json` in the **directory where you launched it**. Each detection produces one record with `frame` (numbered from 1), `handedness`, `index_x`, `index_y` and `raised_fingers`. A completed session with no detections produces an empty array. Each export replaces the previous file in that directory.

Relative to the repository root, the export paths are `hand_camera.json` when launched from the root and `03-mediapipe/03-opencv-webcam/01_hand_tracking/hand_camera.json` when launched from the exercise directory. The terminal prints the full saved path.

Frames without a detected hand contribute to the session limit but produce no record, so exported frame numbers can have gaps. If capture or detection fails after records have been collected, the application reports the error, attempts to export those records and exits with a failure status. A failure before any detection exits without exporting.

## 🔧 Troubleshooting

| Symptom | What to check |
|---|---|
| The default camera cannot be opened, or a frame cannot be read. | Check the webcam connection and Windows camera permissions for desktop apps. Close other applications using the camera and restart the script. The script opens camera index `0`. |
| Python reports a missing module. | Use the shared interpreter shown above and run the pinned installation command from the repository root. Run `pip check` through that interpreter to check package dependencies. |
| Installation reports an unsupported Python version or no matching package build. | Check the interpreter path, Python version and architecture. The verified environment uses 64-bit Python 3.13.15. Use that shared environment and its pinned requirements. |
| PowerShell cannot find the interpreter or script. | Check the current directory and use the matching launch command above. Confirm that `03-mediapipe/.venv/Scripts/python.exe` exists. |
| The model download fails. | Check the internet connection and confirm that the folder containing `hand_tracking.py` is writable. |
| The preview opens but the export is empty. | Look for the red landmarks in the preview. Hold one hand fully in view with adequate lighting. Only frames with a detection are recorded. |
| Finger counts seem incorrect. | Keep the hand upright with fingers visible. The count compares vertical fingertip and joint positions, so rotating the hand can change the result. |
| JSON cannot be saved. | Check write access to the directory from which the script was launched. |

## 📚 What I Learnt

This exercise connects camera capture, colour conversion, landmark coordinates, a sliding window and pandas analysis in one application. Keeping detection and drawing in the same mirrored coordinate system makes the preview easier to use and the exported positions easier to interpret.

Feel free to explore the script and compare the visual feedback with the session results.
