import cv2
import cv2.data

path=cv2.data.haarcascades+"haarcascade_frontalface_default.xml"

model=cv2.CascadeClassifier(path)
camera=cv2.VideoCapture(0)
while True:
    status,image=camera.read()
    faces=model.detectMultiScale(image,1.3,5)
    for oneface in faces:
        x,y,w,h=oneface
        image=cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255,3))
        cv2.imshow("faces",image)
        if cv2.waitKey(1)==ord("q"):
            break    