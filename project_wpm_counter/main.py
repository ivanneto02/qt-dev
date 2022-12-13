from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import Qt
import sys
from components.main_widget import MainWidget
from datetime import datetime
from pynput import keyboard
import threading
from components.key_log import Keylog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Properties of main window
        self.setFixedSize(250, 100)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowTitle("Agile WPM Counter")
        self.setContentsMargins(0,0,0,0)
        self.setStyleSheet("background: black;")

        self.central_widget = MainWidget()
        self.setCentralWidget(self.central_widget)

        # show main window
        self.show()

    def keyPressEvent(self, event):
        # self.central_widget.count += 1
        pass

def main():
    app = QApplication([]) # no cmd args
    window = MainWindow()
    app.exec()

if __name__ == "__main__":
    main()