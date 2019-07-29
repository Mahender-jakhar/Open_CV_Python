import cv2
img =  cv2.imread('lena.jpg',1)
print(img)
cv2.imshow('mj',img)
k = cv2.waitKey()
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('copy_img.png',img)
    cv2.destroyAlWindows()