import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Driver/Kart Param Editor")
        self.setMinimumSize(350, 150)
        self.setCentralWidget(TabWidget(self))

        #self.show()

class TabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        style = """QTabWidget::tab-bar{
                alignment: left;
                }"""
  
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.writetab = QWidget()
        self.comparetab = QWidget()
        self.previewtab = QWidget()
        self.tabs.resize(300, 200)
  
        # Add tabs
        self.tabs.addTab(self.writetab, "Write")
        self.tabs.addTab(self.comparetab, "Compare")
        self.tabs.addTab(self.previewtab, "Preview")
  
        # Create write tab
        self.writetab.layout = QVBoxLayout(self)
        self.lw = QLabel()
        self.lw.setText("This is the write tab")
        self.writetab.layout.addWidget(self.lw)
        self.writetab.setLayout(self.writetab.layout)

        # Create compare tab
        self.comparetab.layout = QVBoxLayout(self)
        self.lc = QLabel()
        self.lc.setText("This is the Compare tab")
        self.comparetab.layout.addWidget(self.lc)
        self.comparetab.setLayout(self.comparetab.layout)

        # Create preview tab
        self.previewtab.layout = QVBoxLayout(self)
        self.lp = QLabel()
        self.lp.setText("This is the Preview tab")
        self.previewtab.layout.addWidget(self.lp)
        self.previewtab.setLayout(self.previewtab.layout)
  
        self.setStyleSheet(style)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)