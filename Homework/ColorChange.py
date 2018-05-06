import cv2
import numpy as np 

filename = r'C:/Users/lenovo/Documents/305_Projects/computer_Vision/material/strawberry.jpg'
#绿色hsv范围(35,43,46) ~ (77,255,255)
#红色hsv范围(0,50,50) ~ (10,255,255) && (156,50,50) ~ (180,255,255)
img = cv2.imread(filename)
cv2.imshow('window',img)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
k1 = (77-35) / (10 - 0)
b1 = 77 - 10 * k1
k2 = (77 - 35) / (180 - 156)
b2 = 77 - k2 * 180
def Red2Green(param):
	x = param[0]
	if (x >= 0 and x <= 10):
		y = k1 * x + b1
	elif (x >= 156 and x <= 180):
		y = k2 * x + b2
	else:
		y = x
	return [y,param[1],param[2]]


lower_red1 = np.array([0,50,50])
lower_red2 = np.array([156,50,50])
upper_red1 = np.array([10,255,255])
upper_red2 = np.array([180,255,255])

mask1 = cv2.inRange(hsv,lower_red1,upper_red1)
mask2 = cv2.inRange(hsv,lower_red2,upper_red2)
mask = mask1 + mask2
[m,n] = mask.shape[:2]

for i in range(m):
	for j in range(n):
		if(mask[i,j] == 255):
			hsv[i,j] = Red2Green(hsv[i,j])

img1 = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow('windows',img1)


New_file = r'C:/Users/lenovo/Documents/305_Projects/computer_Vision/material/fruit.jpg'
Background = cv2.imread(New_file)
berry = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
berry_gray = cv2.cvtColor(berry,cv2.COLOR_BGR2GRAY)
[y,x] = [300,300]
[col,row] = berry.shape[:2]

roi = Background[y:y+col ,x:x+row]
print(roi.shape)
for i in range(col):
	for j in range(row):
		if (berry_gray[i,j]>220):
			roi[i,j] = Background[y+i,x+j]
		else:
			roi[i,j] = berry[i,j]

Background[y:y+col ,x:x+row] = roi 
cv2.imshow('final',Background)


cv2.waitKey(0)
cv2.destroyAllWindows()


