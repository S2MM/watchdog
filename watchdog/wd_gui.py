# -*- coding: utf-8 -*-

'''
https://www.reddit.com/r/learnpython/comments/34jwlw/showing_opencv_live_video_in_pyqt_gui/
'''
import sys
import os
import queue
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui


def grab_video(src, queue, width, height, fps):
    global running

    ret, capture = cv2.VideoCapture(src)
    
    if not ret:
        print("can't get video")
        return 
    
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    capture.set(cv2.CAP_PROP_FPS, fps)

    while(running):
        frame = {}
        ret, img = capture.read()
        frame["img"] = img

        if queue.size < 10 :
            queue.put(frame)
        else:
            print queue.qsize()

    


'''
class WD_Opencv(QObject):
    run = False
    camera_port = 0
    video_path = ""
    image_signal = pyqtSignal(QImage)


    def __init__(self, parent = None):
        super(WD_Opencv, self).__init__(parent)

    def setVideo(self, video_path):
        self.video_path = video_path

    @pyqtSlot()
    def startVideo(self):
        self.run = True
        self.capturer = cv2.VideoCapture(self.video_path)
        while self.run:
            ret, image = self.capturer.read()
            if not ret:
                break
            print(ret)
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            rows, cols, _ = color_swapped_image.shape
            qt_image = QImage(color_swapped_image.data,
                                cols,
                                rows,
                                QImage.Format_RGB888)
            self.image_signal.emit(qt_image)
'''


"""
ImageViewer 自定义图像显示类
"""
class ImageViewer(QWidget):
    def __init__(self):
        super(ImageViewer, self).__init__()
        self.image = None
    
    def initUI(self):
        self.setGeometry(50,50, 1000, 1000)
        self.setWindowTitle("video")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0,0,self.image)
    
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.image = image



class WD_Window(QWidget):
    
    def __init__(self):
        self.videos_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'videos'))
        
        super(WD_Window, self).__init__()
        self.initUI()
    

    def initUI(self):

        self.projector = WD_Opencv()
        self.image_viewer = ImageViewer()

        self.projector.image_signal.connect(self.image_viewer.setImage)

        self.fileButton = QPushButton("导入视频文件")
        self.cameraButton = QPushButton("开启摄像头")

        self.fileButton.clicked.connect(self.get_video)
        self.cameraButton.clicked.connect(self.get_camera)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.fileButton)
        buttonLayout.addWidget(self.cameraButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(self.image_viewer)

        self.setLayout(mainLayout)
        self.setWindowTitle("Watch Dog")
        self.show()

    def paintEvent(self, event):
        return 

    def get_video(self):
        if not self.videos_dir:
            QMessageBox.information(self, "错误", "没有发现视频文件目录")
            return
        
        file_name, file_type = QFileDialog.getOpenFileName(self, "选取视频文件", self.videos_dir)
        if file_name:
            self.projector.setVideo(file_name)
            self.projector.startVideo()
        return 
    
    def get_camera(self):
        return

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WD_Window()
    sys.exit(app.exec_())
