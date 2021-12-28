import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from os.path import *
import main
import errorWindow
import globalvars
import shutil
import hashlib


class selectUI(QWidget):
    def __init__(self, windowWidth, windowHeight):
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

        self.show()

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
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)

        height = 250
        width = 450

        self.setFixedHeight(height)
        self.setFixedWidth(width)
        self.layout = QGridLayout(self)

        try:
            oImage = QImage("Background.png")
            sImage = oImage.scaled(QSize(width, height))                   # resize Image to widgets size
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(sImage))
            self.setPalette(palette)
        except ValueError:
            pass

        self.namelabel = QLabel("StatsViewer", self)
        self.namelabel.setFont(QFont("Arial", 40))

        '''self.quitbtn = QPushButton("Quit", self)
        self.quitbtn.clicked.connect(lambda: QApplication.quit())'''

        self.startbtn = QPushButton("Start", self)
        self.startbtn.clicked.connect(self.firsttime)

        self.spacer = QSpacerItem(100, 25)

        self.layout.addItem(self.spacer, 0, 1)
        self.layout.addItem(self.spacer, 1, 0)
        self.layout.addItem(QSpacerItem(100, 75), 2, 3)
        self.layout.addItem(QSpacerItem(100, 75), 3, 1)
        self.layout.addWidget(self.namelabel, 1, 1)
        self.layout.addWidget(self.startbtn, 2, 1)

    def firsttime(self):
        
        if exists("param/kartParam.bin") & exists("param/driverParam.bin"):
            karthash = globalvars.kart()
            driverhash = globalvars.driver()
            print(karthash, "\n" + driverhash, "\n")
            if (karthash == globalvars.hashkart) & (driverhash == globalvars.hashdriver):
                '''import mainwindow
                self.winmain = mainwindow.mainWindow()
                self.winmain.show()
                self.close()'''
                import ProjectWindow
                self.projWin = ProjectWindow.ProjectWindow()
                self.projWin.show()
                self.close()
            else:
                errorWindow.error(0)
                self.selectui = selectUI(300, 300)

        else:
            self.selectui = selectUI(300, 300)
