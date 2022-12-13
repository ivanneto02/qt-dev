from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QWidget, QLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QFont, QPalette, QColor

FONT = QFont("Times")
PALETTE = QPalette(QColor().black())  # Color black

# Layouts
TOP_BAR_LAYOUT = QHBoxLayout()
TIMER_LAYOUT = QHBoxLayout()
TIMER_BUTTON_LAYOUT = QHBoxLayout()


class Timer(QWidget):
    def __init__(self):
        super().__init__()

        # variables
        self.timer = TimerTime()
        self.timerButton = TimerButton()
        self.label = QLabel("00:00:00")

        # Connect to the TimerTime child's
        self.timer.timeout.connect(self.show_time)

        # set the button
        self.timerButton.clicked.connect(self.execute_button)

        # set layout
        layout = QHBoxLayout()
        layout.addWidget(self.timer)
        layout.addWidget(self.timerButton)
        self.setLayout(layout)

    def execute_button(self):
        print(f"TimerButton pressed. Status {self.timer.isEnabled()}", end="")
        if self.timer.isEnabled():
            self.start_time()
        else:
            self.stop_time()

    def show_time(self):
        time = QDateTime().currentDateTime()
        time_text = time.toString("hh:mm:ss")
        self.label.setText(time_text)

    def start_time(self):
        print(f" time started.")
        self.timer.start_timer(1000)    # Call the TimerTime child's start_timer(int interval)
        self.timer.setEnabled(False)

    def stop_time(self):
        print(f" time stopped.")
        self.timer.stop_timer()         # Call the TimerTime child's stop_timer()
        self.timer.setEnabled(True)


class TimerButton(QWidget):
    def __init__(self):
        super().__init__()

        # variables
        text = "start/end"
        self.button = QPushButton(text)
        self.clicked = self.button.clicked

        # Set layout
        self.setLayout(TIMER_BUTTON_LAYOUT)         # Set layout to TimerButton layout
        self.layout().addWidget(self.button)  # Add the TimerButton


class TimerTime(QWidget):
    def __init__(self):
        super().__init__()

        # variables
        self.label = QLabel("00:00:00")
        self.timer = QTimer()
        self.timeout = self.timer.timeout

        # Set the layout
        self.setLayout(TIMER_LAYOUT)           # Set layout to Timer layout
        self.layout().addWidget(self.label)    # Add QLabel widget to Timer

    def start_timer(self, inter):
        self.timer.start(inter)

    def stop_timer(self):
        self.timer.stop()


class InformationBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(TOP_BAR_LAYOUT)  # Set the layout of this widget
        self.setFont(FONT)              # Set font
        self.setPalette(PALETTE)        # Set palette

        self.layout().addWidget(Timer())  # Add Timer() to the layout
        # self.layout().addWidget(TimerTime())  # Add Timer to layout
        # self.layout().addWidget(TimerButton())  # Add TimerButton to layout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        print("Beginning application...")

        # Make the button
        button = QPushButton("Please Click Me!")
        top_bar = InformationBar()

        # Set the title
        self.setWindowTitle("Information App")
        self.setMenuWidget(top_bar)
        self.setCentralWidget(button)

        # Show the main window widget


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
