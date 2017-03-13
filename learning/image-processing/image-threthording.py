import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #消除图像噪声
    gray = cv2.medianBlur(gray, 5)

    ret,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
    cv2.imshow('Global Thresholding (v = 127)', th1)
    cv2.imshow('daptive Mean Thresholding', th2)
    cv2.imshow('Adaptive Gaussian Thresholding', th3)
    k = cv2.waitKey(80) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()