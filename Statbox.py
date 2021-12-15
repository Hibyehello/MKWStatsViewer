from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatBox:
    def __init__(self, index):
        self.index = index


    def stats(self, current_displayed):

        self.tires = ["4 Wheels", "3 Wheels", "2 Wheels (Quacker)", "2 Wheels"]
        self.drift = ["Outside", "Outside (Bike)", "Inside"]
        self.weight = ["Small", "Medium", "Large"]

        self.numWheelTT = "Number of tires:\n0 = 4 tires\n1 = 2 tires\n2 = 2 tires, closer to each other (used on Quacker)\n3 = 3 tires (used on Blue Falcon)."
        self.DriftTypeTT = "Drift type:\n0 = outside drift used on karts\n1 = outside drift used on bikes\n2 = inside drift"
        self.WeightClassTT = "Weight class (affects camera and trick rotation notably)\n0 = light\n1 = medium\n2 = heavy"

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

        self.numWheelLabel = QLabel("# of Wheels:")
        self.DriftTypeLabel = QLabel("Drift Type:")
        self.WeightClassLabel = QLabel("Weight Class:")

        self.numWheelbox = QComboBox()
        self.numWheelbox.addItems(self.tires)
        self.DriftTypebox = QComboBox()
        self.DriftTypebox.addItems(self.drift)
        self.WeightClassbox = QComboBox()
        self.WeightClassbox.addItems(self.weight)

        if current_displayed[0] == 0:
            self.numWheelbox.setCurrentIndex(0)
        elif current_displayed[0] == 1:
            self.numWheelbox.setCurrentIndex(3)
        elif current_displayed[0] == 2:
            self.numWheelbox.setCurrentIndex(2)
        else:
            self.numWheelbox.setCurrentIndex(1)

        if current_displayed[1] == 0:
            self.DriftTypebox.setCurrentIndex(0)
        elif current_displayed[1] == 1:
            self.DriftTypebox.setCurrentIndex(1)
        else:
            self.DriftTypebox.setCurrentIndex(2)

        if current_displayed[2] == 0:
            self.WeightClassbox.setCurrentIndex(0)
        elif current_displayed[2] == 1:
            self.WeightClassbox.setCurrentIndex(1)
        else:
            self.WeightClassbox.setCurrentIndex(2)

        '''self.numWheelText = QLineEdit(str(current_displayed[0]))
        self.numWheelLabel.setToolTip(self.numWheelTT)
        self.numWheelText.setToolTip(self.numWheelTT)

        self.DriftTypeLabel = QLabel("Drift Type:")
        self.DriftTypeText = QLineEdit(str(current_displayed[1]))
        self.DriftTypeLabel.setToolTip(self.DriftTypeTT)
        self.DriftTypeText.setToolTip(self.DriftTypeTT)

        self.WeightClassLabel = QLabel("Weight Class:")
        self.WeightClassText = QLineEdit(str(current_displayed[2]))
        self.WeightClassLabel.setToolTip(self.WeightClassTT)
        self.WeightClassText.setToolTip(self.WeightClassTT)'''


        self.SpeedLabel = QLabel("Speed:")
        self.SpeedText = QLineEdit(str(current_displayed[9]))

        self.WeightLabel = QLabel("Weight:")
        self.WeightText = QLineEdit(str(current_displayed[7]))

        self.SpeedInTurnLabel = QLabel("Speed in turn: (%)")
        self.SpeedInTurnText = QLineEdit(str(current_displayed[10]))


        # Add Widgets to the layout

        self.layout.addWidget(self.GeneralLabel, 1, 0)
        self.layout.addWidget(self.numWheelLabel, 2, 0)
        self.layout.addWidget(self.numWheelbox, 2, 1)
        self.layout.addWidget(self.DriftTypeLabel, 3, 0)
        self.layout.addWidget(self.DriftTypebox, 3, 1)
        self.layout.addWidget(self.WeightClassLabel, 4, 0)
        self.layout.addWidget(self.WeightClassbox, 4, 1)
        self.layout.addWidget(self.SpeedLabel, 5, 0)
        self.layout.addWidget(self.SpeedText, 5, 1)
        self.layout.addWidget(self.WeightLabel, 6, 0)
        self.layout.addWidget(self.WeightText, 6, 1)
        self.layout.addWidget(self.SpeedInTurnLabel, 7, 0)
        self.layout.addWidget(self.SpeedInTurnText, 7, 1)


        # Set editWidget's layout to self.layout
        self.pLayout.setAlignment(Qt.AlignTop)
        self.pLayout.addLayout(self.layout, 0, 0)
        self.editWidget.setLayout(self.pLayout)

        return self.editWidget