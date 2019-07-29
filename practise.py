from cv2 import *
import numpy as np

img1 = cv2.imread('lena.jpg',-1)
img2 = cv2.imread('messi5.jpg',-1)
cv2.imshow('mj0',img1)
b,g,r = cv2.split(img1)
img1 = cv2.merge((b,g,r))
cv2.imshow('mj',img1)

#COPY A PORTION OF IMAGE TO ANOTHER PLACE IN SAME IMAGE
#ball = img2[280:340,330:390]
#img2[273:333,100:160]= ball
#cv2.imshow('mj0',img2)


img1 = cv2.resize(img1,(512,512))
img2 = cv2.resize(img2,(512,512))


#img3 = add(img1,img2)
img3 = addWeighted(img1,1,img2,1,0)
#cv2.imshow('mj',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()