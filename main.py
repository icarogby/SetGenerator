from PyQt5.QtWidgets import QApplication
import sys
import ui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ui.Window()
    sys.exit(app.exec_())
    