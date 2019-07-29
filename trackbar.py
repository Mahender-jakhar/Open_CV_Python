import numpy as np
import cv2

def nothing(x):
    print(x)

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)

switch = 'OFF : 0 || ON : 1'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    k = cv2.waitKey(1) & 0XFF
    if k == 27:
        break

    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')

    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img[:] = [b,g,r]

    cv2.imshow('image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()