from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CompareTab(QWidget):
    def __init__(self):
        super(CompareTab, self).__init__()
        # Create compare tab
        self.layout = QVBoxLayout(self)
        self.lc = QLabel()
        self.lc.setText("This is the Compare tab")
        self.layout.addWidget(self.lc)
        self.setLayout(self.layout)