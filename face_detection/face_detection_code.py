import cv2

vid = cv2.VideoCapture('C:\\Users\\nurcan\\Desktop\\face_detection\\face.mp4')
#vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('C:\\Users\\nurcan\\Desktop\\face_detection\\frontalface.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\nurcan\\Desktop\\face_detection\\eye.xml')

if (vid.isOpened()== False):
    print("Video dosyasi acilamiyor")
else:
    print("Video dosyası acilabildi")


while True:

    ret, frame = vid.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi = frame[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh), 255, 2)

        cv2.imshow('video', frame)

        if cv2.waitKey(5)&0xFF == ord('q'):
            vid.release()
            cv2.destroyAllWindows()
            break
            
