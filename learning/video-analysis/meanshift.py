import numpy as np
import cv2
cap = cv2.VideoCapture(0)
# take first frame of the video
ret,frame = cap.read()
# 设置初始窗口坐标信息
r,h,c,w = 100,100,200,200  # simply hardcoded the values
print(frame.shape)
#初始化追踪窗口
track_window = (c,r,w,h)
#设置图片追踪区域
roi = frame[r:r+h, c:c+w]
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

'''
掩模图像
cv2.inRange(src, lowerb, upperb[,dst]) -> dst
src: 源图片数组
lowerb：下边界
upperb: 上边界
在Python中如果是单通道，假设lower=[0]，upper=[128]，那么，对每个数在0-128之间为255，否则为0；
如果是多通道，假设lower=[0, 0, 0]，upper=[128,128,128,128]，那么，对每一行，对任意一个数，
如果在范围内，则255，否则0，最后的几个数相与，因此如果都是255，为255，否则为0
'''
#(0., 60., 32.) 0., 60. 32.都是转换为浮点数的语法
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
'''
直方图
cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
1. images: 原图像（图像格式为uint8 或float32）。当传入函数时应该 用中括号[] 括起来，例如：[img]。  
2. channels: 同样需要用中括号括起来，它会告诉函数我们要统计那幅图 像的直方图。如果输入图像是灰度图，它的值就是[0]；
如果是彩色图像 的话，传入的参数可以是[0]，[1]，[2] 它们分别对应着通道B，G，R。 
3. mask: 掩模图像。要统计整幅图像的直方图就把它设为None。但是如果你想统计图像某一部分的直方图的话，你就需要制作一个掩模图像，
并使用它。掩模图像中空的部分（0的部分）会被忽略。  
4. histSize: BIN的数目（直方图x轴的取值范围数）。也应该用中括号括起来，例如：([256])。 
5. ranges: 像素值范围，通常为[0，256]
'''
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
while(1):
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',img2)
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite(chr(k)+".jpg",img2)
    else:
        break
cv2.destroyAllWindows()
cap.release()