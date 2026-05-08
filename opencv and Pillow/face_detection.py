import cv2

cap = cv2.VideoCapture(0)
#load model 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    isOpen, frame = cap.read()

    if not isOpen:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces - face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
    eyes = eye_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    for(x,y,w,h) in eyes:
        cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), (0,0,255), 2)

    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()


