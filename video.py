import cv2
camera=cv2.VideoCapture(0)
while True:
    s,image=camera.read()
    
    #image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGBA)
    cv2.imshow("video",image)
    cv2.waitKey(1)
    
    