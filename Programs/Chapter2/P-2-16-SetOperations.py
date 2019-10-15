import cv2 as cv
import numpy as np
filepath1="Ch2-images/eye_small.jpg"
filepath2="Ch2-images/flower.jpg"

img1=cv.imread(filepath1,0)
img2=cv.imread(filepath2,0)
print(img1.shape)
print(img2.shape)
cv.imwrite("Ch2-images/eye_small.jpg",cv.resize(img1,(225,225)))
# Union
img_union=img1
idxs=np.where(img2>img1)
img_union[idxs]=img2[idxs]
cv.imshow("",img_union)
cv.waitKey(0)
# Intersection
img_intersection=img1
idxs=np.where(img2<img1)
img_intersection[idxs]=img2[idxs]
cv.imshow("",img_intersection)
cv.waitKey(0)
# Set Complement
img_comp=255-img1
cv.imshow("",img_comp)
cv.waitKey(0)
# Set Difference
img_diff=img2-img1
cv.imshow("",img_diff)
cv.waitKey(0)
