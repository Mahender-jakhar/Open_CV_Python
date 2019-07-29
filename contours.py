import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('opencv-logo-white.png',-1)
img = cv2.pyrUp(img)
cv2.imshow('orig',img)
print(img.shape)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(imgray,127,255,0)
contours,hr = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print("number of contours : " + str(len(contours)))

cv2.drawContours(img,contours, -1,(0,255,0),1)



cv2.imshow('image',img)
cv2.imshow('thresh',thresh)
cv2.imshow('gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()