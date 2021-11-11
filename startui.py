import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from os.path import *
import main
import errorWindow
import mainwindow
import globalvars
import shutil
import hashlib


class selectUI(QWidget):
    def createwindow(self, windowWidth, windowHeight):
        super().__init__()
        if not os.path.isdir('./param'):
            os.mkdir('./param')

        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.resize(windowWidth, windowHeight)

        self.kartLabel = QLabel("Select kartParam.bin", self)
        self.kartLabel.move(85, 15)
        self.kartLabel.setToolTip("Find the kartParam.bin, it's not hard")
        
        self.driverLabel = QLabel("Select driverParam.bin", self)
        self.driverLabel.move(80, 70)
        self.driverLabel.setToolTip("Find the driverParam.bin, it's that easy")

        self.kartparambtn = QPushButton("Find kartParam.bin", self)
        self.kartparambtn.move(75, 35)
        self.kartparambtn.clicked.connect(lambda: self.kartparam())

        self.driverparambtn = QPushButton("Find driverParam.bin", self)
        self.driverparambtn.move(70, 90)
        self.driverparambtn.clicked.connect(lambda: self.driverparam())

        self.cancelbtn = QPushButton("done", self)
        self.cancelbtn.move(windowWidth-100, windowHeight-30)
        self.cancelbtn.clicked.connect(lambda: self.windowclose())

    def windowclose(self):
        self.close()

    def kartparam(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Bin Files (*.bin)", options=options)
        if fileName:
            shutil.copyfile(fileName, "./param/kartParam.bin")

    def driverparam(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Bin Files (*.bin)", options=options)
        if fileName:
            shutil.copyfile(fileName, "./param/driverParam.bin")


class startUI(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("StatsViewer")

        height = 250
        width = 450

        self.setFixedHeight(height)
        self.setFixedWidth(width)

        self.namelabel = QLabel("StatsViewer", self)
        self.namelabel.move(115, 50)
        self.namelabel.setFont(QFont("Arial", 40))

        self.quitbtn = QPushButton("Quit", self)
        self.quitbtn.move(375, 215)
        self.quitbtn.clicked.connect(lambda: QApplication.quit())

        self.startbtn = QPushButton("Start", self)
        self.startbtn.move(185, 100)
        self.startbtn.clicked.connect(self.firsttime)

    def firsttime(self):
        
        if exists("param/kartParam.bin") & exists("param/driverParam.bin"):
            karthash = globalvars.kart()
            driverhash = globalvars.driver()
            print(karthash, "\n", driverhash, "\n")
            if (karthash == globalvars.hashkart) & (driverhash == globalvars.hashdriver):
                self.winmain = mainwindow.mainWindow()
                self.winmain.show()
                self.close()
            else:
                errorWindow.error(0)
                self.selectui = selectUI()
                self.selectui.createwindow(300, 300)
                self.selectui.show()

        else:
            self.selectui = selectUI()
            self.selectui.createwindow(300, 300)
            self.selectui.show()
