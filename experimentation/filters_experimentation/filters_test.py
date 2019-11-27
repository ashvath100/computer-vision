import cv2
import numpy as np
import os

img = cv2.imread("D:\\UAV\\computer-vision\\data\\pictures\\Picture.jpeg")
imgBlur = cv2.GaussianBlur(img, (3, 3), 0)
imgBlur = cv2.GaussianBlur(imgBlur, (3, 3), 0)
cv2.imshow("image",imgBlur)

sobel_y_thin = np.array((
        [0,1,-1,0],
        [0,1,-1,0],
        [0,1,-1,0],
        [0,1,-1,0],
        [0,1,-1,0],
        [0,1,-1,0],
        [0,1,-1,0]),dtype="int")

edges_ = cv2.filter2D(imgBlur, -1, sobel_y_thin)
cv2.imshow("hu",edges_)

cv2.waitKey()
cv2.destroyAllWindows()

