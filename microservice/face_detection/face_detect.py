import cv2
import os
import numpy

front_face = os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_default.xml")
face_detector = cv2.CascadeClassifier(front_face)

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BAYER_RG2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        return img

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    frame = detect_face(frame)
    cv2.show("Video face detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows()