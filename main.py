import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Driver/Kart Param Editor")
        self.setMinimumSize(350, 150)
        self.setCentralWidget(TabWidget(self))

        self.show()

class TabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        style = """QTabWidget::tab-bar{
                alignment: left;
                }"""
  
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.writetab = QWidget()
        self.comparetab = QWidget()
        self.previewtab = QWidget()
        self.tabs.resize(300, 200)
  
        # Add tabs
        self.tabs.addTab(self.writetab, "Write")
        self.tabs.addTab(self.comparetab, "Compare")
        self.tabs.addTab(self.previewtab, "Preview")
  
        # Create write tab
        self.writetab.layout = QVBoxLayout(self)
        self.lw = QLabel()
        self.lw.setText("This is the write tab")
        self.writetab.layout.addWidget(self.lw)
        self.writetab.setLayout(self.writetab.layout)
  
        self.setStyleSheet(style)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)








def main():
    application = QApplication(sys.argv)
    app = mainWindow()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()