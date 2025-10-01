import sys
from PyQt6.QtWidgets import *
import src.windows.StartUI as startUI
from src.windows.ProjectWindow import close


app = QApplication(sys.argv)
self = QWidget()

def Main():
    start = startUI.startUI()
    sys.exit(app.exec())


if __name__ == '__main__':
    Main()
