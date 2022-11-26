from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import setGenerator as sg

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Generate button
        generate_button = QPushButton("Generate", self)
        generate_button.clicked.connect(self.generate_button_clicked)
        generate_button.move(10, 10)

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Set Generator")
        self.setWindowIcon(QIcon('Chess-Exibição atual.png')) # mudar
        self.show()

    def generate_button_clicked(self):
        sg.saveFiles(-10, 10, 10, True, False, True)
        print("generate button clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())