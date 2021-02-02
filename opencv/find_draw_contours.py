import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loading and resizing image
image = cv2.imread('Ash_Greninja1.jpg')
image = cv2.resize(image, (960, 540))

# Converting to gray scale and binary
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY_INV)

# Find and Draw Contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# In efficient way (choose the length of the contour or area)
# for contour in contours:
#     if len(contour) <= 50:
#         continue
#     cv2.drawContours(image, contour, -1, (0, 255, 0), 2)

cv2.imshow('Gray', gray_image)
cv2.imshow('Contours', image)
cv2.imshow('Threshold value', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()