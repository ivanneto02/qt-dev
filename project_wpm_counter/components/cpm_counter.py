from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout

from PyQt6.QtGui import QFont, QFontDatabase

class CPM_Counter(QWidget):
    '''
        Only function of this class is to display the CharsPerMinute to the user
    '''

    def __init__(self, count):
        super().__init__()

        id = QFontDatabase.addApplicationFont("./resources/fonts/Roboto/Roboto-Black.ttf")
        if id < 0: print("Font error.")

        self._count = 0

        self._window_c = []

        families = QFontDatabase.applicationFontFamilies(id)

        self.cpmtext = QLabel(f"CPM: {self._count:04}", self)
        self.cpmtext.setFont(QFont(families[0], 25))
        self.cpmtext.setStyleSheet("color: green; background: transparent;")
        self.cpmtext.adjustSize()

        layout = QHBoxLayout()
        layout.addWidget(self.cpmtext)

        self.setLayout(layout)
    
    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, count):
        self._count = count
        self.cpmtext.setText(f"CPM: {self._count:04}")