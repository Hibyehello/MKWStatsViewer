import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mainwindow
import startui


def main():
    application = QApplication(sys.argv)
    start = startui.startui()
    start.show()
    sys.exit(application.exec_())
if __name__ == '__main__':
    main()