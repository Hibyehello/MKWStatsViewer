import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from os.path import *

import src.windows.ProjectWindow as ProjectWindow
import src.windows.ErrorWindow as ErrorWindow
import src.globalvars as globalvars
import shutil


class selectUI(QWidget):
    def __init__(self, windowWidth, windowHeight):
        super().__init__()
        if not os.path.isdir('./param'):
            os.mkdir('./param')

        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowStaysOnTopHint)
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

        self.show()

    def windowclose(self):
        self.close()

    def kartparam(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Bin Files (*.bin)", options=QFileDialog.Option.DontUseNativeDialog)
        if fileName:
            shutil.copyfile(fileName, "./param/kartParam.bin")

    def driverparam(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Bin Files (*.bin)", options=QFileDialog.Option.DontUseNativeDialog)
        if fileName:
            shutil.copyfile(fileName, "./param/driverParam.bin")


class startUI(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("StatsViewer")
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint)

        self.height = 250
        self.width = 450

        self.setFixedHeight(self.height)
        self.setFixedWidth(self.width)
        self.layout = QGridLayout(self)

        try:
            self.oImage = QImage("Background.png")
            self.sImage = self.oImage.scaled(QSize(self.width, self.height))                   # resize Image to widgets size
            self.palette = QPalette()
            self.palette.setBrush(QPalette.Window, QBrush(self.sImage))
            self.setPalette(self.palette)
        except:
            pass

        self.namelabel = QLabel("StatsViewer", self)
        self.namelabel.setFont(QFont("Arial", 40))

        self.startbtn = QPushButton("Start", self)
        self.startbtn.clicked.connect(self.firsttime)

        self.errorWindow = QErrorMessage()

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(2, 1)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(3, 1)

        self.layout.addWidget(self.namelabel, 1, 1)
        self.layout.addWidget(self.startbtn, 2, 1)

        self.show()

    def firsttime(self):
        if exists("param/kartParam.bin") & exists("param/driverParam.bin"):
            karthash = globalvars.kart()
            driverhash = globalvars.driver()
            print(karthash, "\n" + driverhash, "\n")
            if (karthash != globalvars.hashkart) & (driverhash != globalvars.hashdriver):
                self.projWin = ProjectWindow.ProjectWindow()
                self.close()
            else:
                self.errorWindow.showMessage("Non-Vanilla Param Files!")
                self.selectui = selectUI(300, 300)

        else:
            self.selectui = selectUI(300, 300)

    def closefunc(self):
        self.close()
