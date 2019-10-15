import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 
img=np.zeros([16,16])
print(img.shape)
for i in range(16):
    for j in range(16):
        img[i,j]=i*16+j
print(img)
cv.imshow("GrayMatrix",img)
cv.waitKey(0)