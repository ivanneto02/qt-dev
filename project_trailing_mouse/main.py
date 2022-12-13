from msilib.schema import Property
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.center = self.pos()
        self._radius = 1

        self.max_radius = 2500
        self.min_radius = 1
        self.duration = 1500

    @pyqtProperty(float)
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, rad):
        self._radius = rad
        self.update()

    def mousePressEvent(self, event):
        self.center = event.pos()
        self.anim = QPropertyAnimation(self, b"radius", self)
        self.anim.setDuration(self.duration)
        self.anim.setStartValue(self.min_radius)
        self.anim.setEndValue(self.max_radius)
        self.anim.start()
        print(f"Clicking ({self.center.x()}, {self.center.y()})")
    
    def paintEvent(self, event):
        qp = QPainter(self)
        self.draw_circle(qp)
    
    def draw_circle(self, qp):
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QColor("red"))
        qp.drawEllipse(self.center, self.radius, self.radius)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1080, 720)

        canvas = Canvas()
        self.setCentralWidget(canvas)

        # Set palette
        #   - Background color set to black
        myPalette = self.palette()
        myPalette.setColor(self.backgroundRole(), QColor("black"))
        self.setPalette(myPalette)
    

def main():
    app = QApplication([])
    
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()