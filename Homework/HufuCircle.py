import cv2
import numpy as np 

filename = r'C:/Users/lenovo/Documents/305_Projects/computer_Vision/material/Hufucircle.jpg'
img = cv2.imread(filename)
img1 = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,40,param1 = 110,param2 = 100)
for i in circles[0,:]:
	cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('Hough_Circle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
