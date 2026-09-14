import cv2
image=cv2.imread("./WhatsApp Image 2025-10-14 at 00.01.48_b36eace9.jpg")
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("image",image)
cv2.imshow("frame",gray_image)
cv2.waitKey(0)