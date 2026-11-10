import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Couldn't open video source.")
    exit()

while True:
    success, frame = cap.read()

    if not success:
        print("End of stream or failed to grab frame.")
        break

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
