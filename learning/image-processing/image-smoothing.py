import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'images-source'))

img = cv2.imread(image_dir + '\\image1.png')

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur1 = cv2.blur(img, (5,5))
blur2 = cv2.blur(img, (10, 10))

plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(blur1),plt.title('Blur5*5')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(blur2),plt.title('Blur10*10')
plt.xticks([]), plt.yticks([])

plt.show()