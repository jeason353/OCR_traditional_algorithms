import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/house_2.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200)
#hough transform
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=60, maxLineGap=10)
lines1 = lines[:,0,:]   # 提取为二维
for x1,y1,x2,y2 in lines1[:]: 
    cv2.line(img, (x1,y1), (x2,y2), (0, 255, 0), 1)

cv2.imshow('image', img)
cv2.waitKey(0)