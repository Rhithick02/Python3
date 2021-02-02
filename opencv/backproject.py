import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loading images
image = cv2.imread('img_tiger.jpg')
image = cv2.resize(image, (960, 540))

masked_img = cv2.imread('img_tigerRoi.jpg')

# Converting to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv_image_masked = cv2.cvtColor(masked_img, cv2.COLOR_BGR2HSV)

# Hue saturation output
hist_mask = cv2.calcHist([hsv_image_masked], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Gray scale output
mask = cv2.calcBackProject([hsv_image], [0, 1], hist_mask, [0, 180, 0, 256], 1)

plt.imshow(hist_mask)
plt.show()
cv2.imshow('mask', mask)

ret, mask = cv2.threshold(mask, 3, 255, cv2.THRESH_BINARY)
mask = cv2.merge([mask, mask, mask])
result = cv2.bitwise_and(image, mask)

cv2.imshow('orginal', image)
cv2.imshow('roi', masked_img)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()