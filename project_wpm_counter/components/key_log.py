from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import Qt, QThread

from pynput import keyboard
from datetime import *

class Keylog(QThread):
    def __init__(self, parent):
        super().__init__()
        # Save the parents
        self.parent = parent

        # just for testing
        self._count = 0 # testing

    def run(self):
        self.Listen()
    
    def Listen(self):
        with keyboard.Events() as events:
            for event in events:
                if isinstance(event, keyboard.Events.Press):
                    l = datetime.now()
                    print(f"{event.key}")

                    self.parent.handleCharEvent(event, l)
                    # Don't want to change the parent through here, maybe
                    # self.parent.central_widget.count = self.wpm