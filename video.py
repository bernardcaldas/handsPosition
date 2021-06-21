import mediapipe as mp
import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame, 
                'Hello', 
                (50, 50), 
                font, 1, 
                (255, 255, 255), 
                1, 
                cv2.LINE_AA)

    cv2.putText(frame, 
                'this is a video stream', 
                (50, 100), 
                font, 1, 
                (255, 255, 255), 
                1, 
                cv2.LINE_AA)



    cv2.imshow('WebCam Live', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
