import sys
from PyQt5.QtWidgets import *
import src.windows.StartUI as startUI
from src.windows.ProjectWindow import close


app = QApplication(sys.argv)
self = QWidget()


def Quit():
    print("Good-Bye")
    app.exit(0)


def Main():
    start = startUI.startUI()
    app.aboutToQuit.connect(lambda: Quit())
    sys.exit(app.exec_())


if __name__ == '__main__':
    Main()
