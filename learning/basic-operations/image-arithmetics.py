import numpy as np
import cv2

import os

image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'images-source'))

img1_path = image_dir + '\\image2.jpg'
img2_path = image_dir + '\\image3.jpg'

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

img = cv2.add(img1, img2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()