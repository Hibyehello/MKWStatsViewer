from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import src.windows.StartUI

projectName = ""
close = 0


class ProjectWindow(QWidget):
    def __init__(self, parent=None):
        super(ProjectWindow, self).__init__(parent)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)

        # Create Layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.spacer = QSpacerItem(50, 50)

        self.nameLabel = QLabel("New Name:", self)
        self.nameInput = QLineEdit()
        self.layout.addWidget(self.nameLabel, 0, 0)
        self.layout.addWidget(self.nameInput, 0, 1)

        self.layout.addItem(self.spacer, 1, 0)

        self.create = QPushButton("Create", self)
        self.open = QPushButton("Open...", self)
        self.cancel = QPushButton("Cancel", self)
        self.temp = QPushButton("Temp", self)
        self.layout.addWidget(self.temp, 2, 1)
        self.layout.addWidget(self.cancel, 2, 0)
        self.layout.addWidget(self.open, 2, 2)
        self.layout.addWidget(self.create, 2, 3)

        self.temp.clicked.connect(lambda: self.tempfunc())
        self.cancel.clicked.connect(lambda: self.closefunc())
        self.create.clicked.connect(lambda: self.oncreate())

        self.show()

    def oncreate(self):
        global projectName
        projectName = self.nameInput.text()
        print(projectName)

    def closefunc(self):
        self.close()

    def tempfunc(self):
        import src.windows.MainWindow as mainwindow
        self.mainwin = mainwindow.mainWindow(self)
        self.destroy()
