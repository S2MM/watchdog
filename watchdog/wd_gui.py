# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox,QHBoxLayout, QVBoxLayout

class WD_Window(QWidget):

    def __init__(self):
        super(WD_Window, self).__init__()
        self.initUI()
    

    def initUI(self):
        self.inputLabel = QLabel("输入你的名字")  
        self.editLine = QLineEdit()
        self.printButton = QPushButton("输入")
        self.clearButton = QPushButton("清除")

        self.printButton.clicked.connect(self.printText)
        self.clearButton.clicked.connect(self.clear_text)

        inputLayout = QHBoxLayout()
        inputLayout.addWidget(self.inputLabel)
        inputLayout.addWidget(self.editLine)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.printButton)
        buttonLayout.addWidget(self.clearButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("Watch Dog")
        self.show()

    
    def printText(self):
        text = self.editLine.text()
        if text == '':
            QMessageBox.information(self, "有个问题", "还没输入内容")
        else:
            QMessageBox.Information(self, "成功了", "输入成功 %s" % text)

    def clear_text(self):
        text = self.editLine.text()
        if text == '':
            return
        else:
            self.editLine.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WD_Window()
    sys.exit(app.exec_())
