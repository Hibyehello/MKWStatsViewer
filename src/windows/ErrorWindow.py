from PyQt5.QtWidgets import QMessageBox

errlist = ["kartParam.bin and/or driverParam.bin are modded"]


def error(index):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setStyleSheet("QLabel{min-width: 150px;}")
    msg.setText("Error")
    msg.setInformativeText(errlist[index])
    msg.setWindowTitle("Error")
    msg.exec_()
