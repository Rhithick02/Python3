import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Ash_Greninja1.jpg')
image = cv2.resize(image, (960, 540))

# Converting to gray scale and binary
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY_INV)

# Find and Draw Contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contours[224], -1, (0, 255, 0), 2)
cv2.imshow('test', image)

m = cv2.moments(contours[224])
# print(m)
# To find the centroid of the object
cx = m['m10'] / m['m00']
cy = m['m01'] / m['m00']
print(cx, cy)
cv2.waitKey(0)
cv2.destroyAllWindows()