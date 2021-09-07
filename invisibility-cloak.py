import cv2 
import numpy as np
import time

cap = cv2.VideoCapture(0)

#Give time for camera to load
time.sleep(3)
background = 0

for i in range(30):
	ret, background = cap.read()

width, height = background.shape[0], background.shape[1]
background = np.flip(background, axis=1)

while True:
	ret, img = cap.read()

	img = np.flip(img, axis=1)

	#convert to HSV colour space
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	value = (35,35)
	blurred = cv2.GaussianBlur(hsv, value, 0)

	#Define lower range for colour
	# lower_col = np.array([100, 50, 50])
	# upper_col = np.array([140, 255, 255])
	# mask1 = cv2.inRange(hsv, lower_col, upper_col)
	# mask2 = 0

	#### THIS IS RED
	# Note: red wraps around 180 which will need two ranges as commented
	lower_col = np.array([0, 170, 80])
	upper_col = np.array([10, 255, 255])
	mask1 = cv2.inRange(hsv, lower_col, upper_col)

	#Define upper range for Colour - here we use red
	lower_col = np.array([170, 170, 80])
	upper_col = np.array([180, 255, 255])
	mask2 = cv2.inRange(hsv, lower_col, upper_col)

	mask = mask1 + mask2 
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

	#Replace colour pixel with background
	img[np.where(mask==255)] = background[np.where(mask==255)]
	cv2.imshow('Display', img)

	k = cv2.waitKey(10)
	if k == 27:
		break



