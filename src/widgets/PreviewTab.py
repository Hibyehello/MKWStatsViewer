from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class PreviewTab(QWidget):
    def __init__(self):
        super(PreviewTab, self).__init__()
        # Create preview tab
        self.layout = QVBoxLayout(self)
        self.lp = QLabel()
        self.lp.setText("This is the Preview tab")
        self.layout.addWidget(self.lp)
        self.setLayout(self.layout)