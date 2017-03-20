
from PyQt4 import QtCore, QtGui, uic
import sys, os
import cv2
import numpy as np
import threading
import time
import queue


running = False
capture_thread = None
form_class = uic.loadUiType("simple.ui")[0]
q = queue.Queue()
 

def grab(cam, q, width, height, fps, file=None):
    global running
    if file:
        capture = cv2.VideoCapture(file)
    else:
        capture = cv2.VideoCapture(cam)
    
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    capture.set(cv2.CAP_PROP_FPS, fps)

    while(running):
        frame = {}        
        capture.grab()
        retval, img = capture.retrieve(0)
        frame["img"] = img

        if q.qsize() < 10:
            q.put(frame)
        else:
            print(q.qsize())
        
        time.sleep(0.03)
        

class OwnImageWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(OwnImageWidget, self).__init__(parent)
        self.image = None

    def setImage(self, image):
        self.image = image
        sz = image.size()
        self.setMinimumSize(sz)
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QtCore.QPoint(0, 0), self.image)
        qp.end()



class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.videos_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'videos'))

        self.setupUi(self)

        self.cameraButton.clicked.connect(self.camera_clicked)
        self.fileButton.clicked.connect(self.file_clicked)
        self.stopButton.clicked.connect(self.stop_clicked)
        
        self.window_width = self.ImgWidget.frameSize().width()
        self.window_height = self.ImgWidget.frameSize().height()
        self.ImgWidget = OwnImageWidget(self.ImgWidget)       

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)


    def camera_clicked(self):
        global running
        global camera_thread
        running = True
        camera_thread = threading.Thread(target=grab, args = (0, q, 1920, 1080, 30))
        camera_thread.start()
        self.fileButton.setEnabled(False)
        self.cameraButton.setEnabled(False)
        

    def file_clicked(self):
        if not self.videos_dir:
            QtGui.QMessageBox.information(self, "错误", "没有发现视频文件目录")
            return
        
        file_name = QtGui.QFileDialog.getOpenFileName(self, "选取视频文件", self.videos_dir)
        global running
        global file_thread
        if file_name:
            running = True
            file_thread = threading.Thread(target=grab, args = (0, q, 1920, 1080, 30, file_name))
            file_thread.start()
            self.fileButton.setEnabled(False)
            self.cameraButton.setEnabled(False)
    
    def stop_clicked(self):
        global running
        global q
        global camera_thread
        global file_thread

        running = False
        q = queue.Queue() 
       
        self.fileButton.setEnabled(True)
        self.cameraButton.setEnabled(True)


    def update_frame(self):
        if not q.empty():
            self.cameraButton.setText('摄像头正在工作')
            frame = q.get()
            img = frame["img"]

            img_height, img_width, img_colors = img.shape
            scale_w = float(self.window_width) / float(img_width)
            scale_h = float(self.window_height) / float(img_height)
            scale = min([scale_w, scale_h])

            if scale == 0:
                scale = 1
            
            img = cv2.resize(img, None, fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, bpc = img.shape
            bpl = bpc * width
            image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)
            self.ImgWidget.setImage(image)

    def closeEvent(self, event):
        global running
        running = False






app = QtGui.QApplication(sys.argv)
w = MyWindowClass(None)
w.setWindowTitle('雷宇婷毕业设计')
w.show()
app.exec_()