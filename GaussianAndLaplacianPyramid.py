import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg',-1)
frame = img.copy()
gp = [frame]

for i in range(6):
    frame = cv2.pyrDown(frame)
    gp.append(frame)

#for i in range(6):
#   cv2.imshow(str(i),gp[i])

lp = [gp[5]]
for i in range(5,0,-1):
    gaux = cv2.pyrUp((gp[i]))
    lap = cv2.subtract(gp[i-1],gaux)
    cv2.imshow(str(i),lap)


cv2.waitKey(0)
cv2.destroyAllWindows()