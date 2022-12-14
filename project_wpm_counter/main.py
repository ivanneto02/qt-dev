from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import QtGui
from components.main_widget import MainWidget
from datetime import datetime
from pynput import keyboard
from components.key_log import Keylog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._but_pressed = False
        self._curr_x = 100
        self._curr_y = 100
        self._drag_pos = QPoint()

        # Properties of main window
        self.setFixedSize(300, 100)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowTitle("Agile WPM Counter")
        self.setContentsMargins(0,0,0,0)
        self.setStyleSheet("background: black;")

        # move window
        self.move(100, 100)

        self.central_widget = MainWidget()
        self.setCentralWidget(self.central_widget)

        # show main window
        self.show()

    def keyPressEvent(self, event):
        # self.central_widget.count += 1
        pass

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self._drag_pos = a0.globalPosition().toPoint()
        self._but_pressed = True

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self._but_pressed = False

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        # only move window when we are pressing the left button
        if (a0.buttons() == Qt.MouseButton.LeftButton) and (self._but_pressed):
            self.move(self.pos() + a0.globalPosition().toPoint() - self._drag_pos)
            self._drag_pos = a0.globalPosition().toPoint()

def main():
    app = QApplication([]) # no cmd args
    window = MainWindow()
    app.exec()

if __name__ == "__main__":
    main()