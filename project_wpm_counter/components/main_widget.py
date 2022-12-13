# Import PyQt6 elements
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import Qt

# Import components
from .wpm_counter import WPM_Counter
from .cpm_counter import CPM_Counter
from .key_log import Keylog

from datetime import *

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self._count = 0

        self.wpmcounter = WPM_Counter(self._count)
        self.cpmcounter = CPM_Counter(self._count)

        self.char_gran = 50

        # Make char_gran-sized list to store characters
        self._chars = [''] * self.char_gran # '' in _chars means no character there
        self._chars_ts = [None] * self.char_gran # 0 means no timestamp there
        # We pass self._chars and self._charts_ts up to parent

        layout = QVBoxLayout()
        layout.addWidget(self.wpmcounter)
        layout.addWidget(self.cpmcounter)
        layout.setContentsMargins(0, 0, 0, 0)

        # self.keylog will take in both objects and update their 
        # values
        self.keylog = Keylog(self)
        self.keylog.start()

        self.setLayout(layout)

    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, count):
        print(f"    setting count to {self.count}")
        self._count = count
        self.wpmcounter.count = self._count
        self.cpmcounter.count = self._count

    def handleCharEvent(self, event, ts):
        '''
            In charge of handling a character event.
            Will compute words per minute, characters per minute,
            and give those values back to self.wpmcounter and
            self.cpmcounter
        '''
        self._chars = self._chars[1:] + [event.key]
        self._chars_ts = self._chars_ts[1:] + [ts]

        # compute sum of characters
        sum = 0
        for i in range(0, len(self._chars)):
            if self._chars[i] != '':
                sum += 1

        timedeltas = []
        for i in range(0, len(self._chars_ts)):
            if self._chars_ts[i]:
                timedeltas.append(self._chars_ts[i] - timedelta(0))
            else:
                timedeltas.append(timedelta(0))

        try:
            avg_timedelta = sum(timedeltas, timedelta(0)) / len(timedeltas)
            self.wpmcounter.count = sum / (avg_timedelta.seconds * 60)
        except:
            avg_timedelta = timedelta(0)
            self.wpmcounter.count = 0
