from PyQt5.QtWidgets import QMessageBox

global errlist

errlist = ["kartParam.bin and/or driverParam.bin are modded"]

def error(err):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setStyleSheet("QLabel{min-width: 150px;}")
    msg.setText("Error")
    msg.setInformativeText(errlist[0])
    msg.setWindowTitle("Error")
    msg.exec_()