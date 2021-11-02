import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from os.path import *
import os
import shutil

class selectui(QWidget):
    def createwindow(self,windowWidth,windowHeight):
        parent = None
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.resize(windowWidth,windowHeight)

        self.kartLabel = QLabel("Select kartParam.bin",self)
        self.kartLabel.move(15,15)

        self.driverparambtn = QPushButton("Find KartParam.bin", self)
        self.driverparambtn.move(-3,35)
        self.driverparambtn.clicked.connect(lambda: self.kartparam())



        self.cancelbtn = QPushButton("cancel", self)
        self.cancelbtn.move(windowWidth-100,windowHeight-30)
        self.cancelbtn.clicked.connect(lambda: self.windowclose())

    def windowclose(self):
        self.close()

    def kartparam(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            shutil.copyfile(fileName, "./param/kartParam.bin")

class startui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StatsViewer")

        height = 250
        width = 450

        self.setFixedHeight(height)
        self.setFixedWidth(width)

        namelabel = QLabel("StatsViewer", self)
        namelabel.move(115,50)
        namelabel.setFont(QFont("Arial", 40))

        startbtn = QPushButton("Start",self)
        startbtn.move(185, 100)
        startbtn.clicked.connect(self.firsttime)


    def firsttime(self):
        if(exists("param/kartParam.bin") & exists("param/driverParam.bin")):
            print("Yep")
        else:
            self.selectui = selectui()
            self.selectui.createwindow(300,300)
            self.selectui.show()

            
        