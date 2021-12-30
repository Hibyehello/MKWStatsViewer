import sys
from PyQt5.QtWidgets import *
import startui
from ProjectWindow import close


app = QApplication(sys.argv)
self = QWidget()

def Quit():
    print("Good-Bye")
    app.exit(0)

def Main():
    start = startui.startUI()
    app.aboutToQuit.connect(lambda: Quit())
    sys.exit(app.exec_())


if __name__ == '__main__':
    Main()
