import sys
from PyQt5.QtWidgets import *
import startui


app = QApplication(sys.argv)
self = QWidget()


def Quit():
    print("Hi")
    app.exit(0)

def Main():
    start = startui.startUI()
    app.aboutToQuit.connect(lambda: Quit())
    app.exec_()


if __name__ == '__main__':
    Main()
