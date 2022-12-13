from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt, QThread
import sys
from datetime import datetime
from pynput import keyboard
import threading

class Keylog(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        self.Listen()
    
    def Listen(self):
        while(True):
            with keyboard.Events() as events:
                for event in events:
                    if isinstance(event, keyboard.Events.Press):
                        print(f"{event.key}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mainwidget = QWidget()
        self.setCentralWidget(self.mainwidget)

        self.keylog = Keylog()
        self.keylog.start()

        # show main window
        self.show()
    
def main():
    app = QApplication([]) # no cmd args
    window = MainWindow()
    app.exec()

if __name__ == "__main__":
    main()