from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout

from PyQt6.QtGui import QFont, QFontDatabase

class WPM_Counter(QWidget):
    '''
        Only function of this class is to display the WordsPerMinute to the user
    '''

    def __init__(self, count):
        super().__init__()

        id = QFontDatabase.addApplicationFont("./resources/fonts/Roboto/Roboto-Black.ttf")
        if id < 0: print("Font error.")

        self._count = 0

        self._window_c = []

        families = QFontDatabase.applicationFontFamilies(id)

        self.wpmtext = QLabel(f"WPM: {self._count:03}", self)
        self.wpmtext.setFont(QFont(families[0], 30))
        self.wpmtext.setStyleSheet("color: green; background: transparent;")
        self.wpmtext.adjustSize()

        layout = QHBoxLayout()
        layout.addWidget(self.wpmtext)

        self.setLayout(layout)
    
    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, count):
        self._count = count
        self.wpmtext.setText(f"WPM: {self._count:03}")