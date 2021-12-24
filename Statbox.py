from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class StatBox:
    def __init__(self, index):
        self.index = index

        self.tires = ["4 Wheels", "3 Wheels", "2 Wheels (Quacker)", "2 Wheels"]  # 4 Wheels = "Kart", 2 Wheels = "Bike"
        self.drift = ["Outside", "Outside (Bike)", "Inside"]
        self.weight = ["Small", "Medium", "Large"]

        # Define main Widget and Layout
        self.editWidget = QWidget()
        self.layout = QGridLayout()
        self.pLayout = QGridLayout()

        # Font
        self.Font = QFont()

        # TODO: Create a red asterisk with full transparency at the end of these labels
        # Add widgets here
        self.GeneralLabel = QLabel("General")
        self.numWheelLabel = QLabel("# of Wheels:")
        self.DriftTypeLabel = QLabel("Drift Type:")
        self.WeightClassLabel = QLabel("Weight Class:")
        self.numWheelbox = QComboBox()
        self.DriftTypebox = QComboBox()
        self.WeightClassbox = QComboBox()
        self.SpeedLabel = QLabel("Speed:")
        self.SpeedText = QLineEdit()
        self.WeightLabel = QLabel("Weight:")
        self.WeightText = QLineEdit()
        self.SpeedInTurnLabel = QLabel("Speed in turn: (%)")
        self.SpeedInTurnText = QLineEdit()

        self.line = QFrame()

        # Add stats combobox entries
        self.numWheelbox.addItems(self.tires)
        self.DriftTypebox.addItems(self.drift)
        self.WeightClassbox.addItems(self.weight)

    # Updates textboxes / dropdowns with entry's default values
    def update_entry_stats(self, current_displayed):

        # Font for some Category Labels
        self.Font.setPointSize(24)
        self.Font.setBold(True)

        # Edit Widgets here
        self.GeneralLabel.setFont(self.Font)

        self.SpeedText.setText(str(current_displayed[9]))
        self.WeightText.setText(str(current_displayed[7]))
        self.SpeedInTurnText.setText(str(current_displayed[10]))

        # We can probably do 1:1 correspondence here as well
        if current_displayed[0] == 0:
            self.numWheelbox.setCurrentIndex(0)
        elif current_displayed[0] == 1:
            self.numWheelbox.setCurrentIndex(3)
        elif current_displayed[0] == 2:
            self.numWheelbox.setCurrentIndex(2)
        else:
            self.numWheelbox.setCurrentIndex(1)

        self.DriftTypebox.setCurrentIndex(current_displayed[1])
        self.WeightClassbox.setCurrentIndex(current_displayed[2])

        # Create a horizontal divider line
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        # Add Widgets to the layout
        self.layout.addWidget(self.GeneralLabel, 1, 0)
        self.layout.addWidget(self.line, 2, 0)
        self.layout.addWidget(self.numWheelLabel, 3, 0)
        self.layout.addWidget(self.numWheelbox, 3, 1)
        self.layout.addWidget(self.DriftTypeLabel, 4, 0)
        self.layout.addWidget(self.DriftTypebox, 4, 1)
        self.layout.addWidget(self.WeightClassLabel, 5, 0)
        self.layout.addWidget(self.WeightClassbox, 5, 1)
        self.layout.addWidget(self.SpeedLabel, 6, 0)
        self.layout.addWidget(self.SpeedText, 6, 1)
        self.layout.addWidget(self.WeightLabel, 7, 0)
        self.layout.addWidget(self.WeightText, 7, 1)
        self.layout.addWidget(self.SpeedInTurnLabel, 8, 0)
        self.layout.addWidget(self.SpeedInTurnText, 8, 1)

        # Set editWidget's layout to self.layout
        self.pLayout.setAlignment(Qt.AlignTop)
        self.pLayout.addLayout(self.layout, 0, 0)
        self.editWidget.setLayout(self.pLayout)

        return self.editWidget
