import sys
import random

from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Data members
        self.hello = ["Hello", "hi", "HI", "HOWDY", "HELLOW"]

        self.button = QtWidgets.QPushButton('Click me!')
        self.text = QtWidgets.QLabel('Hello world', alignment = QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

def main():

    # Params
    title = "Test Application"
    style_sheet = '''background-color: black;
                     color: white;
                    '''

    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.showMaximized()
    widget.setWindowTitle(title)
    widget.setStyleSheet(style_sheet)
    widget.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
