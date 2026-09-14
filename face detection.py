import cv2
import cv2.data
path=cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
model=cv2.CascadeClassifier(path)

image=cv2.imread("./WhatsApp Image 2025-10-14 at 00.04.22_f37e2daa.jpg")
faces=model.detectMultiScale(image,1.3,5)
for oneface in faces:
    x,y,w,h=oneface
    image=cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255,3))
    
    
#gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("faces",image)
#cv2.imshow("frame",gray_image)
cv2.waitKey(0)