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
        self.pLayout = QGridLayout()

        # Font for some Category Labels
        self.Font = QFont()
        self.Font.setPointSize(24)
        self.Font.setBold(True)

        # Add Widgets here
        self.GeneralLabel = QLabel("General")
        self.GeneralLabel.setFont(self.Font)
        self.GeneralLabel.setMaximumHeight(20)
        self.SpeedLabel = QLabel("Speed:")
        self.SpeedText = QLineEdit(str(current_displayed[9]))

        self.WeightLabel = QLabel("Weight:")
        self.WeightText = QLineEdit(str(current_displayed[7]))

        self.SpeedInTurnLabel = QLabel("Speed in turn: (%)")
        self.SpeedInTurnText = QLineEdit(str(current_displayed[10]))


        # Add Widgets to the layout
        self.layout.addWidget(self.GeneralLabel, 1, 0)
        self.layout.addWidget(self.SpeedLabel, 2, 0)
        self.layout.addWidget(self.SpeedText, 2, 1)
        self.layout.addWidget(self.WeightLabel, 3, 0)
        self.layout.addWidget(self.WeightText, 3, 1)
        self.layout.addWidget(self.SpeedInTurnLabel, 4, 0)
        self.layout.addWidget(self.SpeedInTurnText, 4, 1)

        # Set editWidget's layout to self.layout
        self.pLayout.setAlignment(Qt.AlignTop)
        self.pLayout.addLayout(self.layout, 0, 0)
        self.editWidget.setLayout(self.pLayout)

        return self.editWidget