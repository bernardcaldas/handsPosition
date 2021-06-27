import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

wCam, hCam = 640,480
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        cv2.line(image,(0,165),(640,165),(255,0,0),1,cv2.LINE_AA)
        x1 = int (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * wCam)
        y1 = int (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * hCam)
        label = 'ok'
        if y1 < 165 :
          label = 'Posicao incorreta'
    

        cv2.putText(image,label,(x1,y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1, cv2.LINE_AA)
        print(x1,y1)

        
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
    #print([mp_hands.HandLandmark.INDEX_FINGER_TIP].x)
            
    cv2.imshow('MediaPipe Hands', image)
    #print(results.multi_hand_landmarks)
     
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()