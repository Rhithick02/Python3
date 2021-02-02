import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loading and resizing image
image = cv2.imread('Ash_Greninja1.jpg')
image = cv2.resize(image, (960, 540))

# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

color = ['b', 'g', 'r']
# [(0, 'b'), (1, 'g') (2, 'r')]
for i, col in enumerate(color):
    histogram = cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot(histogram, color = col)
# histogram = cv2.calcHist([gray_image],[0], None, [256], [0, 256])
# plt.plot(histogram, color = 'k')
plt.show()