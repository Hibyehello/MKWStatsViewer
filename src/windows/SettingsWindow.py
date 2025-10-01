from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class SettingsWin(QWidget):

    def __init__(self):

        super(SettingsWin, self).__init__()
        self.setWindowTitle("Settings")
        self.setWindowFlags(Qt.WindowStaysOnTopHint |
                            Qt.CustomizeWindowHint |
                            Qt.WindowCloseButtonHint |
                            Qt.WindowMaximizeButtonHint)
        self.show()
