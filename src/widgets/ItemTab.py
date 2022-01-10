from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ItemTab(QWidget):
    def __init__(self):
        super(ItemTab, self).__init__()
        # Create Item tab (ItemSlot.bin support)
        self.layout = QVBoxLayout(self)
        self.lp = QLabel()
        self.lp.setText("This is the Item tab")
        self.layout.addWidget(self.lp)
        self.setLayout(self.layout)
