import cv2
import numpy as np

import os

image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'images-source'))
image_path = image_dir + '\\image1.jpg'
print(image_path)

img = cv2.imread(image_path)

img1 = img[:,:,:]

#[B,G,R]
px = img[100, 100]
print(px)

print(img.shape)
#总像素数
print(img.size)
print(img.dtype)



eye = img[280:340, 580:640]
img[0:60, 0:60] = eye

cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()