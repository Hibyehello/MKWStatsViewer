from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatBox:
    def __init__(self, index):
        self.index = index

    def stats(self, current_displayed):

        # Define main Widget and Layout
        self.editWidget = QWidget()
        self.layout = QGridLayout()

        # Font for some Category Labels
        self.Font = QFont()
        self.Font.setPointSize(24)
        self.Font.setBold(True)

        # Add Widgets here
        self.GeneralLabel = QLabel("General")
        self.GeneralLabel.setFont(self.Font)
        self.SpeedLabel = QLabel("Speed:")
        self.SpeedText = QLineEdit(str(current_displayed[9]))

        self.WeightLabel = QLabel("Weight:")
        self.WeightText = QLineEdit(str(current_displayed[7]))

        self.SpeedInTurnLabel = QLabel("Speed in turn: (%)")
        self.SpeedInTurnText = QLineEdit(str(current_displayed[10]))


        # Add Widgets to the layout
        self.layout.addWidget(self.GeneralLabel, 0, 0)
        self.layout.addWidget(self.SpeedLabel, 1, 0)
        self.layout.addWidget(self.SpeedText, 1, 1)
        self.layout.addWidget(self.WeightLabel, 2, 0)
        self.layout.addWidget(self.WeightText, 2, 1)
        self.layout.addWidget(self.SpeedInTurnLabel, 3, 0)
        self.layout.addWidget(self.SpeedInTurnText, 3, 1)

        # Set editWidget's layout to self.layout
        self.editWidget.setLayout(self.layout)

        return self.editWidget