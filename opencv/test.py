import cv2
import numpy as np

cap = cv2.VideoCapture('CARE_Video.mp4')
# img = cv2.imread('walpaper1.jpg', cv2.IMREAD_COLOR)

# Pixel manipulation
# img[50:100, 50:100] = [255, 255, 255]

# Drawing line
# cv2.line(img, (70,0), (150, 150), (255, 255, 255))
# wid = int(img.shape[1] * 0.4)
# heigh = int(img.shape[0] * 0.4)
# resized = cv2.resize(img, (wid, heigh), interpolation = cv2.INTER_AREA)

# cv2.imshow('edited', img)
# cv2.waitKey(0)

# Opening video
# print(img.shape)
while True:
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
#     cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()