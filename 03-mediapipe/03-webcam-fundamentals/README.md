# 📷 Exercise 03 — Webcam Fundamentals

## 🎯 Objective

Learn how to access a webcam and capture real-time video using **Python and OpenCV**.

In this exercise, I explored how video streams work, how to capture individual frames, and how to display them continuously in an OpenCV window.

## 📚 What I Learnt

Throughout this exercise, I practised the following concepts:

| Concept | What I learnt |
|---|---|
| `cv2.VideoCapture(0)` | Access the default webcam. |
| `cap.isOpened()` | Check whether the camera was initialised successfully. |
| `cap.read()` | Capture a frame and return two values: success status and image data. |
| `while` loop | Continuously capture new frames. |
| `cv2.imshow()` | Display captured frames in a window. |
| `cv2.waitKey()` | Detect keyboard input to interact with the application. |
| `cap.release()` | Release the webcam resource. |
| `cv2.destroyAllWindows()` | Close all OpenCV windows. |

### 💡 Key Takeaways

- A video is essentially a sequence of individual images called **frames**.
- Each iteration of the loop captures a new frame, replacing the previous value stored in the `frame` variable.
- Displaying frames continuously creates the appearance of real-time video.
- Proper resource management is important when working with hardware such as webcams.

## 🛠️ Implementation

Created a Python application that:

1. Initialises the computer's webcam.
2. Checks whether the camera is available.
3. Captures frames continuously.
4. Displays the video in an OpenCV window.
5. Detects when the user presses `q` to exit.
6. Releases the camera and closes the application windows.

**File created:** `03-webcam-fundamentals/webcam.py`

## ✅ Testing Results

The application was successfully tested.

- ✅ Webcam opens correctly.
- ✅ Frames update continuously.
- ✅ Pressing `q` exits the application.
- ✅ Webcam resources are released correctly.

## 💻 Development Environment

| Component | Version |
|---|---|
| Operating System | Windows |
| Python | 3.13.15 |
| OpenCV | 5.0.0 |
| MediaPipe | 1.2.2 |
| Virtual Environment | Shared `.venv/` |
