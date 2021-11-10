import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import main


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Driver/Kart Param Editor")
        self.setMinimumSize(350, 150)
        self.setCentralWidget(TabWidget(self))

        # self.show()


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
        self.acceltab = QWidget()
        self.itemtab = QWidget()
        self.tabs.resize(300, 200)
  
        # Add tabs
        self.tabs.addTab(self.writetab, "Write")
        self.tabs.addTab(self.comparetab, "Compare")
        self.tabs.addTab(self.itemtab, "Items")
        self.tabs.addTab(self.acceltab, "Graph")
        self.tabs.addTab(self.previewtab, "Preview")
  
        # Create write tab
        self.writetab.layout = QVBoxLayout(self)
        self.lw = QLabel()
        self.lw.setText("This is the edit tab")

        # Need these Defined now
        self.driverselect = QComboBox(self)
        self.driverselect.addItems(["Mario", "Baby Peach", "Waluigi"])
        self.kartselect = QComboBox(self)
        self.kartselect.addItems(["Standard Kart S", "Standard Kart M", "Standard Kart L"])

        self.paramselect = QComboBox(self)
        self.paramselect.addItems(["Kart" , "Driver"])
        self.paramselect.currentTextChanged.connect(lambda: self.setEditWindow())

        self.writetab.layout.addWidget(self.lw)
        self.writetab.layout.addWidget(self.paramselect)
        self.writetab.layout.addWidget(self.kartselect)
        self.writetab.layout.addWidget(self.driverselect)
        self.writetab.setLayout(self.writetab.layout)
        self.driverselect.hide()

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

        # Create acceleration graph tab
        self.acceltab.layout = QVBoxLayout(self)
        self.la = QLabel()
        self.la.setText("This is the Graph tab")
        self.acceltab.layout.addWidget(self.la)
        self.acceltab.setLayout(self.acceltab.layout)

        # Create item tab (ItemSlot.bin support)
        self.itemtab.layout = QVBoxLayout(self)
        self.li = QLabel()
        self.li.setText("This is the Item tab")
        self.itemtab.layout.addWidget(self.li)
        self.itemtab.setLayout(self.itemtab.layout)
  
        self.setStyleSheet(style)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def setEditWindow(self):
        index = self.paramselect.currentIndex()
        if index == 0:
            self.driverselect.hide()
            self.kartselect.show()
        else:
            self.kartselect.hide()
            self.driverselect.show()
