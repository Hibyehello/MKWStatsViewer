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

        self.characters = ["---Small---", "Baby Peach", "Baby Daisy", "Dry Bones", "Baby Mario",
                      "Toad", "Baby Luigi", "Toadette", "Koopa Troopa", "Small Mii", "---Medium---",
                      "Mario", "Luigi", "Yoshi", "Daisy", "Peach", "Birdo", "Diddy Kong", "Bowser Jr.",
                      "Medium Mii", "---Large---", "Waluigi", "Bowser", "Donkey Kong", "Wario", "King Boo",
                      "Dry Bowser", "Funky Kong", "Rosalina", "Large Mii"]

        self.vehicles = ["---Small---", "Standard Kart S", "Baby Booster", "Mini Beast", "Cheep Charger",
                    "Tiny Titan", "Blue Falcon", "Standard Bike S", "Bullet Bike", "Bit Bike", "Quacker",
                    "Magikruiser", "Jet Bubble", "---Medium---", "Standard Kart M", "Classic Dragster",
                    "Wild Wing", "Super Blooper", "Daytripper", "Sprinter", "Standard Bike M", "Mach Bike",
                    "Sugarscoot", "Zip Zip", "Sneakster", "Dolphin Dasher", "---Large---", "Standard Kart L",
                    "Offroader", "Flame Flyer", "Piranha Prowler", "Jetsetter", "Honeycoupe", "Standard Bike L",
                    "Flame Runner", "Wario Bike", "Shooting Star", "Spear", "Phantom"]

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
        self.driverselect.addItems(self.characters)
        self.driverselect.setCurrentIndex(1)
        self.kartselect = QComboBox(self)
        self.kartselect.addItems(self.vehicles)
        self.kartselect.setCurrentIndex(1)

        self.lastselecteddriver = self.driverselect.currentIndex()
        self.lastselectedkart = self.driverselect.currentIndex()

        font = QFont("Arial", 15, QFont.Bold)

        item = self.driverselect.model()
        item.item(0, 0).setFont(font)
        item.item(10, 0).setFont(font)
        item.item(20, 0).setFont(font)
        item = self.kartselect.model()
        item.item(0, 0).setFont(font)
        item.item(13, 0).setFont(font)
        item.item(26, 0).setFont(font)

        self.paramselect = QComboBox(self)
        self.paramselect.addItems(["Kart", "Driver"])
        self.paramselect.currentTextChanged.connect(lambda: self.setEditWindow())
        self.driverselect.currentTextChanged.connect(lambda: self.canBeSelected())
        self.kartselect.currentTextChanged.connect(lambda: self.canBeSelected())

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

    def canBeSelected(self):
        self.unselectable = ["---Small---", "---Medium---", "---Large"]
        if not(self.driverselect.currentText() in self.unselectable):
            self.lastselecteddriver = self.driverselect.currentIndex()
        else:
            self.driverselect.setCurrentIndex(self.lastselecteddriver)
        if not(self.kartselect.currentText() in self.unselectable):
            self.lastselectedkart = self.kartselect.currentIndex()
        else:
            self.kartselect.setCurrentIndex(self.lastselectedkart)

