from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QCheckBox, QFileDialog
import setGenerator as sg

# colocar try catch
# msg de erro e de concluido

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.aleatory = False
        self.ascending = False
        self.descending = False

        # Title
        title_label = QLabel("Set Generator", self)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        title_label.resize(200, 20)
        title_label.move(20, 20)

        # Floor input
        title_label = QLabel("Floor", self)
        title_label.move(20, 50)

        self.floor_line = QLineEdit(self)
        self.floor_line.resize(60, 30)
        self.floor_line.move(20, 80)

        # Ceiling input
        title_label = QLabel("Ceiling", self)
        title_label.move(100, 50)

        self.ceiling_line = QLineEdit(self)
        self.ceiling_line.resize(60, 30)
        self.ceiling_line.move(100, 80)

        # Length input
        title_label = QLabel("Length", self)
        title_label.move(180, 50)

        self.length_line = QLineEdit(self)
        self.length_line.resize(60, 30)
        self.length_line.move(180, 80)

        # Aleatory check button
        generate_button = QCheckBox("Aleatory", self)
        generate_button.move(20, 120)
        generate_button.stateChanged.connect(self.aleatoryState)

        # Ascending check button
        generate_button = QCheckBox("Ascending", self)
        generate_button.move(20, 140)
        generate_button.stateChanged.connect(self.ascendingState)

        # Descending check button
        generate_button = QCheckBox("Descending", self)
        generate_button.move(20, 160)
        generate_button.stateChanged.connect(self.descendingState)

        # Generate button
        generate_button = QPushButton("Generate", self)
        generate_button.move(140, 140)
        generate_button.clicked.connect(self.generate_button_clicked)

        self.setGeometry(50, 50, 260, 200)
        self.setWindowTitle("Set Generator")
        self.show()

    def generate_button_clicked(self):
        location = QFileDialog.getSaveFileName(self, "Save", self.length_line.text())[0]

        sg.saveFiles(
            int(self.floor_line.text()),
            int(self.ceiling_line.text()),
            int(self.length_line.text()),

            self.aleatory,
            self.ascending,
            self.descending,

            location
        )

    def aleatoryState(self, state):
        if state == Qt.Checked:
            self.aleatory = True
        else:
            self.aleatory = False

    def ascendingState(self, state):
        if state == Qt.Checked:
            self.ascending = True
        else:
            self.ascending = False

    def descendingState(self, state):
        if state == Qt.Checked:
            self.descending = True
        else:
            self.descending = False
