from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SettingsWin(QWidget):

    def __init__(self):

        super(SettingsWin, self).__init__()
        self.setWindowTitle("Settings")
        self.setWindowFlags(Qt.WindowStaysOnTopHint |
                            Qt.CustomizeWindowHint |
                            Qt.WindowCloseButtonHint |
                            Qt.WindowMaximizeButtonHint)
        self.show()
