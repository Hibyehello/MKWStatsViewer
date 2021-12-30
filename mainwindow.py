from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import WriteTab
import CompareTab
import PreviewTab
import AccelTab
import ItemTab
import SettingsWindow


class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._createMenuBar()
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle('StatsViewer')
        self.setMinimumSize(350, 150)
        self.setCentralWidget(TabWidget(self))

        self.show()

    def openSettings(self):
        self.settings = SettingsWindow.SettingsWin()

    def _createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.editMenu = QMenu('&File', self)
        self.menuBar.addMenu(self.editMenu)

        self.a_settings = QAction("​&Settings...", self)
        self.a_settings.triggered.connect(lambda: self.openSettings())
        self.a_newProject = QAction("&New Project", self)
        self.a_openProject = QAction("&Open Project...", self)

        self.editMenu.addAction(self.a_newProject)
        self.editMenu.addAction(self.a_openProject)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.a_settings)

        self.setMenuBar(self.menuBar)


    def closeEvent(self, a0: QCloseEvent) -> None:
        from main import Quit
        Quit()


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

        style = """QTabWidget::tab-bar{
                alignment: left;
                }"""

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.writetab = WriteTab.WriteTab(self.current_displayed, self.characters, self.character_icons,
                                         self.vehicles, self.vehicle_icons)
        self.comparetab = CompareTab.CompareTab()
        self.previewtab = PreviewTab.PreviewTab()
        self.acceltab = AccelTab.AccelTab()
        self.itemtab = ItemTab.ItemTab()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.writetab, "Write")
        self.tabs.addTab(self.comparetab, "Compare")
        self.tabs.addTab(self.itemtab, "Items")
        self.tabs.addTab(self.acceltab, "Graph")
        self.tabs.addTab(self.previewtab, "Preview")

        self.setStyleSheet(style)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

