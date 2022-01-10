from PyQt5.QtWidgets import *
from os.path import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import src.core as core
import src.dict as dict
import src.statbox as Statbox
import random
import time


class WriteTab(QWidget):
    def __init__(self, current_displayed, characters, character_icons, vehicles, vehicle_icons):
        super(WriteTab, self).__init__()
        # Create write tab
        self.layout = QGridLayout(self)

        self.Statbox = Statbox.StatBox(current_displayed)
        self.save = core.Save()

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

        for entry in range(0, len(characters)):
            if character_icons[entry] != '':
                if exists(character_icons[entry]):
                    icon = QIcon(character_icons[entry])
                    self.driverselect.addItem(icon, characters[entry])
                else:
                    self.driverselect.addItem(characters[entry])
            else:
                self.driverselect.addItem(characters[entry])

        self.driverselect.setCurrentIndex(1)

        for entry in range(0, len(vehicles)):
            if vehicle_icons[entry] != '':
                if exists(vehicle_icons[entry]):
                    icon = QIcon(vehicle_icons[entry])
                    self.kartselect.addItem(icon, vehicles[entry])
                else:
                    self.kartselect.addItem(vehicles[entry])
            else:
                self.kartselect.addItem(vehicles[entry])

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

        self.layout.addWidget(self.paramselect, 1, 1)
        self.layout.addWidget(self.kartselect, 2, 1)
        self.layout.addWidget(self.driverselect, 2, 1)
        self.layout.addWidget(self.cheatingOnline, 3, 1)
        self.layout.addWidget(self.editScroll, 4, 1)
        self.setLayout(self.layout)
        self.driverselect.hide()

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
