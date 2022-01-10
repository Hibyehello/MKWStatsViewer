from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AccelTab(QWidget):
    def __init__(self):
        super(AccelTab, self).__init__()
        # Create Acceleration tab
        self.layout = QVBoxLayout(self)
        self.lp = QLabel()
        self.lp.setText("This is the Acceleration tab")
        self.layout.addWidget(self.lp)
        self.setLayout(self.layout)
