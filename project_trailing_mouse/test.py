from msilib.schema import Property
from re import S
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Circle(QWidget):
    def __init__(self, parent, center, radius):
        super().__init__(parent)
        self._radius = radius
        self.center = center
    
    @pyqtProperty(float)
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, rad):
        self._radius = rad
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        self.draw_circle(qp)

    def draw_circle(self, qp):
        qp.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor("red"))
        pen.setWidth(10)
        qp.setPen(pen)
        qp.drawEllipse(self.center, self.radius, self.radius)


class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        self.anim_list = []

        self._radius = 1

        self.max_radius = 50000
        self.min_radius = 1
        self.duration = 25000

        anim = QPropertyAnimation(self, b"radius", self)
        anim.setDuration(self.duration)
        anim.setStartValue(self.min_radius)
        anim.setEndValue(self.max_radius)
        anim.setLoopCount(-1)
        anim.start()

    @pyqtProperty(int)
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, rad):
        for i in range(0, len(self.anim_list)):
            self.anim_list[i].radius = rad - self.anim_list[i].radius
        self.update()

    def paintEvent(self, event):
        # print("Painting all circles...")
        qp = QPainter(self)
        self.draw_circle(qp)

    def draw_circle(self, qp):
        qp.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor("red"))
        pen.setWidth(10)
        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        for i in range(0, len(self.anim_list)):
            # print(f"circle({i})({self.anim_list[i].radius}) ", end="")
            qp.drawEllipse(self.anim_list[i].center, self.anim_list[i].radius, self.anim_list[i].radius)
        # print("")

    def mousePressEvent(self, event):
        circle = Circle(self, event.pos(), self.radius)
        self.anim_list.append(circle)
        for i in range(0, len(self.anim_list)//2):
            if (self.anim_list[i].radius > ((self.width()**2 + self.height()**2)**0.5 + 1000)):
                self.anim_list.pop(i)
        print(f"Clicking ({event.pos().x()}, {event.pos().y()}), len: {len(self.anim_list)}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()

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