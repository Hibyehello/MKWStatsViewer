import sys
from os.path import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import core
import main
import dict
import Statbox
import random
import time


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle('StatsViewer')
        self.setMinimumSize(350, 150)
        self.setCentralWidget(TabWidget(self))

        # self.show()


class TabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.characters = ["---Small---", "Baby Mario", "Baby Luigi", "Baby Peach", "Baby Daisy",
                           "Toad", "Toadette", "Koopa Troopa", "Dry Bones", "Small Mii", "---Medium---",
                           "Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Birdo", "Diddy Kong", "Bowser Jr.",
                           "Medium Mii", "---Large---", "Wario", "Waluigi", "Donkey Kong", "Bowser", "King Boo",
                           "Rosalina", "Funky Kong", "Dry Bowser", "Large Mii"]

        self.character_icons = ['', 'icons/bmr.png', 'icons/blg.png', 'icons/bpc.png', 'icons/bds.png', 'icons/ko.png',
                                'icons/kk.png', 'icons/nk.png', 'icons/ka.png', 'icons/mii.png', '', 'icons/mr.png',
                                'icons/lg.png', 'icons/pc.png', 'icons/ds.png', 'icons/ys.png', 'icons/ca.png',
                                'icons/dd.png', 'icons/jr.png', 'icons/mii.png', '', 'icons/wr.png', 'icons/wl.png',
                                'icons/dk.png', 'icons/kp.png', 'icons/kt.png', 'icons/rs.png', 'icons/fk.png',
                                'icons/bk.png', 'icons/mii.png']

        self.vehicles = ["---Small---", "Standard Kart S", "Baby Booster", "Mini Beast", "Cheep Charger",
                         "Tiny Titan", "Blue Falcon", "Standard Bike S", "Bullet Bike", "Bit Bike", "Quacker",
                         "Magikruiser", "Jet Bubble", "---Medium---", "Standard Kart M", "Classic Dragster",
                         "Wild Wing", "Super Blooper", "Daytripper", "Sprinter", "Standard Bike M", "Mach Bike",
                         "Sugarscoot", "Zip Zip", "Sneakster", "Dolphin Dasher", "---Large---", "Standard Kart L",
                         "Offroader", "Flame Flyer", "Piranha Prowler", "Jetsetter", "Honeycoupe", "Standard Bike L",
                         "Flame Runner", "Wario Bike", "Shooting Star", "Spear", "Phantom"]

        self.vehicle_icons = ['', 'icons/sdf_kart.png', 'icons/sa_kart.png', 'icons/sb_kart.png', 'icons/sc_kart.png',
                              'icons/sd_kart.png', 'icons/se_kart.png', 'icons/sdf_bike.png', 'icons/sa_bike.png',
                              'icons/sb_bike.png', 'icons/sc_bike.png', 'icons/sd_bike.png', 'icons/se_bike.png', '',
                              'icons/mdf_kart.png', 'icons/ma_kart.png', 'icons/mb_kart.png', 'icons/mc_kart.png',
                              'icons/md_kart.png', 'icons/me_kart.png', 'icons/mdf_bike.png', 'icons/ma_bike.png',
                              'icons/mb_bike.png', 'icons/mc_bike.png', 'icons/md_bike.png', 'icons/me_bike.png', '',
                              'icons/ldf_kart.png', 'icons/la_kart.png', 'icons/lb_kart.png', 'icons/lc_kart.png',
                              'icons/ld_kart.png', 'icons/le_kart.png', 'icons/ldf_bike.png', 'icons/la_bike.png',
                              'icons/lb_bike.png', 'icons/lc_bike.png', 'icons/ld_bike.png', 'icons/le_bike.png']

        self.current_displayed = []

        self.save = core.Save()

        self.Statbox = Statbox.StatBox(self.current_displayed)

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
        self.writetab.layout = QGridLayout(self)

        # Need these Defined now
        self.editScroll = QScrollArea(self)
        self.driverselect = QComboBox(self)
        self.kartselect = QComboBox(self)

        random.seed(time.time())
        easteregg = random.randint(0, 10000)

        if easteregg > 11:
            self.cheatingOnline = QLabel("NOTE: Changing these values for online cheating is bannable and should not "
                                         "be attempted.")
        elif easteregg > 1 < 11:
            self.cheatingOnline = QLabel("NOTE: Changing these values for online cheating is based and should "
                                         "be attempted.")
        elif easteregg == 0:
            self.cheatingOnline = QLabel("NOTE: Jaden is Based")
        self.cheatingOnline.setWordWrap(True)
        self.cheatingOnline.setAlignment(Qt.AlignLeft)

        for entry in range(0, len(self.characters)):
            if self.character_icons[entry] != '':
                if exists(self.character_icons[entry]):
                    icon = QIcon(self.character_icons[entry])
                    self.driverselect.addItem(icon, self.characters[entry])
                else:
                    self.driverselect.addItem(self.characters[entry])
            else:
                self.driverselect.addItem(self.characters[entry])

        self.driverselect.setCurrentIndex(1)

        for entry in range(0, len(self.vehicles)):
            if self.vehicle_icons[entry] != '':
                if exists(self.vehicle_icons[entry]):
                    icon = QIcon(self.vehicle_icons[entry])
                    self.kartselect.addItem(icon, self.vehicles[entry])
                else:
                    self.kartselect.addItem(self.vehicles[entry])
            else:
                self.kartselect.addItem(self.vehicles[entry])

        self.kartselect.setCurrentIndex(1)
        self.current_displayed = dict.vehicle[0]

        self.lastselecteddriver = self.driverselect.currentIndex()
        self.lastselectedkart = self.driverselect.currentIndex()

        self.kartselect.currentIndexChanged.connect(self.onKartChange)
        self.driverselect.currentIndexChanged.connect(self.onDriverChange)

        font = QFont("Arial", 15, QFont.Bold)

        self.cheatingOnline.setStyleSheet("color: rgb(255,0,0)")

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
        self.editScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.editScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.editScroll.setWidgetResizable(True)
        self.editScroll.setWidget(self.Statbox.update_entry_stats(self.current_displayed))

        self.writetab.layout.addWidget(self.paramselect, 1, 1)
        self.writetab.layout.addWidget(self.kartselect, 2, 1)
        self.writetab.layout.addWidget(self.driverselect, 2, 1)
        self.writetab.layout.addWidget(self.cheatingOnline, 3, 1)
        self.writetab.layout.addWidget(self.editScroll, 4, 1)
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

        self.saveSC = QShortcut(QKeySequence.Save, self)

        if self.paramselect.currentIndex() == 0:
            self.saveSC.activated.connect(lambda: self.KartSave())
        else:
            self.saveSC.activated.connect(lambda: self.DriverSave())

    def setEditWindow(self):
        index = self.paramselect.currentIndex()
        if index == 0:
            self.driverselect.hide()
            self.kartselect.show()
            self.current_displayed = dict.vehicle[0]
            self.editScroll.setWidget(self.Statbox.update_entry_stats(self.current_displayed, True))
        else:
            self.kartselect.hide()
            self.driverselect.show()
            self.current_displayed = dict.character[0]
            self.editScroll.setWidget(self.Statbox.update_entry_stats(self.current_displayed, True))

    def canBeSelected(self):
        self.unselectable = ["---Small---", "---Medium---", "---Large---"]
        if not(self.driverselect.currentText() in self.unselectable):
            self.lastselecteddriver = self.driverselect.currentIndex()
        else:
            self.driverselect.setCurrentIndex(self.lastselecteddriver)
        if not(self.kartselect.currentText() in self.unselectable):
            self.lastselectedkart = self.kartselect.currentIndex()
        else:
            self.kartselect.setCurrentIndex(self.lastselectedkart)

    # Update the speed textbox when kartselect index changes
    # NOTE: This will probably suck to implement everything this way
    def onKartChange(self, i):
        i -= 1
        if i > 13:
            i -= 1
            if i > 26:
                i -= 1

        self.current_displayed = dict.vehicle[i]

        print(self.current_displayed)
        self.editScroll.setWidget(self.Statbox.update_entry_stats(self.current_displayed, True))

    def onDriverChange(self, i):
        i -= 1
        if i > 10:
            i -= 1
            if i > 20:
                i -= 1

        self.current_displayed = dict.character[i]
        self.editScroll.setWidget(self.Statbox.update_entry_stats(self.current_displayed, True))

    def KartSave(self):
        self.save.save_to_json(self.current_displayed,
                               'kart',
                               self.kartselect.currentIndex(),
                               self.kartselect.currentText())
        self.Statbox.clear()

    def DriverSave(self):
        self.save.save_to_json(self.current_displayed,
                                'driver',
                                self.driverselect.currentIndex(),
                                self.driverselect.currentText())
        self.Statbox.clear()
