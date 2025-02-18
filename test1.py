import cv2
from deepface import DeepFace
import os

data_base = r'C:\Users\sudip\Programme\Projects\Python\FaceRecognition\images'
cam = cv2.VideoCapture(0)
print("Opening webcam..... Press 'q' to quit....")
while True :
    camopened, frame = cam.read()

    if not(camopened) :
        print("Failed to capture frame.....  Exiting.....")
        break

    try :
        match = DeepFace.find(img_path = frame, db_path = data_base, enforce_detection = True)
        if len(match[0]) > 0 :
            text = match[0].iloc[0,0][64:-4]
            color = (0, 255, 0)
        else :
            text = 'NO MATCH'
            color = (0, 0, 255)
    except :
        text = 'NO FACE DETECTED'
        color = (0, 255, 255)

    cv2.putText(frame, text, (25, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
    cv2.imshow('Live Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
