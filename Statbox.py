from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import core


class StatBox:
    def __init__(self, current_displayed):
        self.current_displayed = current_displayed

        self.save = core.Save

        self.tires = ["4 Wheels", "3 Wheels", "2 Wheels (Quacker)", "2 Wheels"]  # 4 Wheels = "Kart", 2 Wheels = "Bike"
        self.drift = ["Outside", "Outside (Bike)", "Inside"]
        self.weight = ["Small", "Medium", "Large"]

        # Define main Widget and Layout
        self.editWidget = QWidget()
        self.layout = QGridLayout()
        self.pLayout = QGridLayout()

        # Font
        self.Font = QFont()

        self.edited = "<font color='red'>*</font>"

        # Add widgets here
        self.textBoxes = []
        self.labels = []
        self.labelsText = ["# of Wheels:", "Drift Type:", "Weight Class:", "Unused", "Weight:", "Bump Deviation:",
                           "Speed:", "Speed in turn(%):", "Tilt", "Standard Acceleration(A0):",
                           "Standard Acceleration(A1):", "Standard Acceleration(A2):", "Standard Acceleration(A3):",
                           "Standard Acceleration(T1):", "Standard Acceleration(T2):", "Standard Acceleration(T3):",
                           "Drift Acceleration(A0):", "Drift Acceleration(A1):", "Drift Acceleration(T1):",
                           "Manual Handling Tightness:", "Automatic Handling Tightness:", "Handling Reactivity:",
                           "Manual Drift Tightness:", "Automatic Drift Tightness:", "Drift Reactivity:",
                           "Outside Drift Angle:", "Outside Drift Decrement:", "Mini-Turbo Duration:",
                           "Item X Distance:", "Item Z Distance:", "Item Y Distance:", "Other Item Value:",
                           "Maximum Normal Acceleration:", "Mega Mushroom Scale:", "Tire Distance:"]
        for _ in self.labelsText:
            self.labels.append(QLabel())

        for _ in range(len(self.labels)-3):
            self.textBoxes.append(QLineEdit())

        self.GeneralLabel = QLabel("General")

        for i in range(len(self.labels)):
            self.labels[i].setText(self.labelsText[i])

        self.numWheelbox = QComboBox()
        self.DriftTypebox = QComboBox()
        self.WeightClassbox = QComboBox()
        #self.SpeedText = QLineEdit()
        #self.WeightText = QLineEdit()
        #self.SpeedInTurnText = QLineEdit()
        self.line = QFrame()

        # Add stats combobox entries
        self.numWheelbox.addItems(self.tires)
        self.DriftTypebox.addItems(self.drift)
        self.WeightClassbox.addItems(self.weight)

    # Updates textboxes / dropdowns with entry's default values
    def update_entry_stats(self, current_displayed, clear=False):

        # Font for some Category Labels
        self.Font.setPointSize(24)
        self.Font.setBold(True)

        # Edit Widgets here
        self.GeneralLabel.setFont(self.Font)

        print(current_displayed)

        self.textBoxes[1].setText(str(current_displayed[7]))
        self.textBoxes[2].setText(str(current_displayed[8]))
        self.textBoxes[3].setText(str(current_displayed[9]))
        self.textBoxes[4].setText(str(current_displayed[10]))
        self.textBoxes[5].setText(str(current_displayed[11]))
        self.textBoxes[6].setText(str(current_displayed[12]))
        self.textBoxes[7].setText(str(current_displayed[13]))
        self.textBoxes[8].setText(str(current_displayed[14]))
        self.textBoxes[9].setText(str(current_displayed[15]))
        self.textBoxes[10].setText(str(current_displayed[16]))
        self.textBoxes[11].setText(str(current_displayed[17]))
        self.textBoxes[12].setText(str(current_displayed[18]))
        self.textBoxes[13].setText(str(current_displayed[19]))
        self.textBoxes[14].setText(str(current_displayed[20]))
        self.textBoxes[15].setText(str(current_displayed[21]))
        self.textBoxes[16].setText(str(current_displayed[22]))
        self.textBoxes[17].setText(str(current_displayed[23]))
        self.textBoxes[18].setText(str(current_displayed[24]))
        self.textBoxes[19].setText(str(current_displayed[25]))
        self.textBoxes[20].setText(str(current_displayed[26]))
        self.textBoxes[21].setText(str(current_displayed[27]))
        self.textBoxes[22].setText(str(current_displayed[28]))
        self.textBoxes[23].setText(str(current_displayed[29]))
        self.textBoxes[24].setText(str(current_displayed[30]))
        self.textBoxes[25].setText(str(current_displayed[95]))  # KCL multipliers between these values
        self.textBoxes[26].setText(str(current_displayed[96]))
        self.textBoxes[27].setText(str(current_displayed[97]))
        self.textBoxes[28].setText(str(current_displayed[98]))
        self.textBoxes[29].setText(str(current_displayed[99]))
        self.textBoxes[30].setText(str(current_displayed[100]))
        self.textBoxes[31].setText(str(current_displayed[101]))

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
        self.numWheelbox.currentIndexChanged.connect(lambda: self.onUpdate(0))
        self.DriftTypebox.currentIndexChanged.connect(lambda: self.onUpdate(1))
        self.WeightClassbox.currentIndexChanged.connect(lambda: self.onUpdate(2))
        self.textBoxes[0].editingFinished.connect(lambda: self.onUpdate(3))
        self.textBoxes[1].editingFinished.connect(lambda: self.onUpdate(4))
        self.textBoxes[2].editingFinished.connect(lambda: self.onUpdate(5))

        # Add Widgets to the layout
        self.add_to_layout()

        # Set editWidget's layout to self.layout
        self.pLayout.setAlignment(Qt.AlignTop)
        self.pLayout.addLayout(self.layout, 0, 0)
        self.editWidget.setLayout(self.pLayout)

        if clear:
            self.clear()

        return self.editWidget

    def onUpdate(self, index):
        self.unsaved_progess = True
        self.labels[index].setText(self.labelsText[index] + self.edited)

    def clear(self):
        self.unsaved_progess = False
        for x in range(len(self.labels)):
            self.labels[x].setText(self.labelsText[x])


    def add_to_layout(self):
        self.layout.addWidget(self.GeneralLabel, 1, 0)
        self.layout.addWidget(self.line, 2, 0)
        self.layout.addWidget(self.labels[0], 3, 0)
        self.layout.addWidget(self.numWheelbox, 3, 1)
        self.layout.addWidget(self.labels[1], 4, 0)
        self.layout.addWidget(self.DriftTypebox, 4, 1)
        self.layout.addWidget(self.labels[2], 5, 0)
        self.layout.addWidget(self.WeightClassbox, 5, 1)
        self.layout.addWidget(self.labels[6], 6, 0)
        self.layout.addWidget(self.textBoxes[3], 6, 1)
        self.layout.addWidget(self.labels[4], 7, 0)
        self.layout.addWidget(self.textBoxes[1], 7, 1)
        self.layout.addWidget(self.labels[7], 8, 0)
        self.layout.addWidget(self.textBoxes[4], 8, 1)
        self.layout.addWidget(self.labels[8], 9, 0)
        self.layout.addWidget(self.textBoxes[5], 9, 1)
        self.layout.addWidget(self.labels[5], 10, 0)
        self.layout.addWidget(self.textBoxes[2], 10, 1)
        self.layout.addWidget(self.labels[9], 11, 0)
        self.layout.addWidget(self.textBoxes[6], 11, 1)
        self.layout.addWidget(self.labels[10], 12, 0)
        self.layout.addWidget(self.textBoxes[7], 12, 1)
        self.layout.addWidget(self.labels[11], 13, 0)
        self.layout.addWidget(self.textBoxes[8], 13, 1)
        self.layout.addWidget(self.labels[12], 14, 0)
        self.layout.addWidget(self.textBoxes[9], 14, 1)
        self.layout.addWidget(self.labels[13], 15, 0)
        self.layout.addWidget(self.textBoxes[10], 15, 1)
        self.layout.addWidget(self.labels[14], 16, 0)
        self.layout.addWidget(self.textBoxes[11], 16, 1)
        self.layout.addWidget(self.labels[15], 17, 0)
        self.layout.addWidget(self.textBoxes[12], 17, 1)
        self.layout.addWidget(self.labels[16], 18, 0)
        self.layout.addWidget(self.textBoxes[13], 18, 1)
        self.layout.addWidget(self.labels[17], 19, 0)
        self.layout.addWidget(self.textBoxes[14], 19, 1)
        self.layout.addWidget(self.labels[18], 20, 0)
        self.layout.addWidget(self.textBoxes[15], 20, 1)
        self.layout.addWidget(self.labels[19], 21, 0)
        self.layout.addWidget(self.textBoxes[16], 21, 1)
        self.layout.addWidget(self.labels[20], 22, 0)
        self.layout.addWidget(self.textBoxes[17], 22, 1)
        self.layout.addWidget(self.labels[21], 23, 0)
        self.layout.addWidget(self.textBoxes[18], 23, 1)
        self.layout.addWidget(self.labels[22], 24, 0)
        self.layout.addWidget(self.textBoxes[19], 24, 1)
        self.layout.addWidget(self.labels[23], 25, 0)
        self.layout.addWidget(self.textBoxes[20], 25, 1)
        self.layout.addWidget(self.labels[24], 26, 0)
        self.layout.addWidget(self.textBoxes[21], 26, 1)
        self.layout.addWidget(self.labels[25], 27, 0)
        self.layout.addWidget(self.textBoxes[22], 27, 1)
        self.layout.addWidget(self.labels[26], 28, 0)
        self.layout.addWidget(self.textBoxes[23], 28, 1)
        self.layout.addWidget(self.labels[27], 29, 0)
        self.layout.addWidget(self.textBoxes[24], 29, 1)
        self.layout.addWidget(self.labels[28], 32, 0)
        self.layout.addWidget(self.textBoxes[25], 32, 1)
        self.layout.addWidget(self.labels[29], 33, 0)
        self.layout.addWidget(self.textBoxes[26], 33, 1)
        self.layout.addWidget(self.labels[30], 34, 0)
        self.layout.addWidget(self.textBoxes[27], 34, 1)
        self.layout.addWidget(self.labels[31], 35, 0)
        self.layout.addWidget(self.textBoxes[28], 35, 1)
        self.layout.addWidget(self.labels[32], 36, 0)
        self.layout.addWidget(self.textBoxes[29], 36, 1)
        self.layout.addWidget(self.labels[33], 37, 0)
        self.layout.addWidget(self.textBoxes[30], 37, 1)
        self.layout.addWidget(self.labels[34], 38, 0)
        self.layout.addWidget(self.textBoxes[31], 38, 1)
