# watchdog #
基于OpenCV的视频监控检测程序

## 实现功能 ###
1. 视频文件导入
2. 摄像头视频捕获
3. 运动物体捕获截图
4. 运动跟踪

## 技术栈 ###
* OS：win10
* 开发语言： Python 3.6.0
* Qt：PyQt4
* OpenCV： OpenCV2

## 环境搭建 ###
* [PyQt4 安装]()
* [Windows下基于Python3的OpenCV安装](https://www.solarianprogrammer.com/2016/09/17/install-opencv-3-with-python-3-on-windows/)
* [Windows下Github Permission to denied to username解决方法](https://www.leeboonstra.com/developer/github-error-permission-to-userrepo-denied-to-userother-repo/)
手抄:control panel > user accounts > credential manager > Windows credentials > Generic credentials
Next remove the Github keys.

## 涉及算法 ###
* **meanshift**  
均值漂移算法，在聚类、图像平滑、分割、跟踪等方面有着广泛的应用。  
可以找到特征数据点密度最大区域  
```
cv2.meanShift(probImage, window, criteria) -> retval, window

probImage - 目标图像直方图的反向投影
window - 初始搜索窗口
criteria - 迭代搜索算法的结束条件
```

* **histogram**  
图片直方图  
直方图是一个简单的表，它给出了一幅图像或一组图像中拥有给定数值的像素数量。因此，灰度图像的直方图有256个条目（或称为容器）。
0号容器给出值为0的像素数目，1号容器给出值为1的像素个数，以此类推。
```

```





## 参考资料 ###
* [OpenCV-Python 教程（官方）](http://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
* [OpenCV API文档](http://docs.opencv.org/3.0-last-rst/)