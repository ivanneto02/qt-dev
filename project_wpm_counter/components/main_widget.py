# Import PyQt6 elements
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import Qt

# Import components
from .wpm_counter import WPM_Counter
from .cpm_counter import CPM_Counter
from .key_log import Keylog

from datetime import *

import sys
import os
sys.path.append(os.path.abspath(os.path.join(".", "helpers")))

# import helpers
from cpm_wpm_calculation import calculate_cpm, calculate_wpm

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self._wpmcount = 0
        self._cpmcount = 0

        self.wpmcounter = WPM_Counter(self._wpmcount)
        self.cpmcounter = CPM_Counter(self._cpmcount)

        self._char_hist_len = 50

        # Make char_hist_len list to store characters
        self._chars = [] # empty, will do nothing until size > 1
        self._chars_ts = [] # empty, will do nothing until size > 1
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
    def cpmcount(self):
        return self._cpmcount

    @property
    def wpmcount(self):
        return self._wpmcount
    
    @cpmcount.setter
    def cpmcount(self, count):
        self._cpmcount = count
        self.cpmcounter.count = self._cpmcount

    @wpmcount.setter
    def wpmcount(self, count):
        self._wpmcount = count
        self.wpmcounter.count = self._wpmcount

    def handleCharEvent(self, event, ts):
        '''
            In charge of handling a character event.
            Will compute words per minute, characters per minute,
            and give those values back to self.wpmcounter and
            self.cpmcounter
        '''
        # if (len(self._chars) >= 1):
        #     i = len(self._chars_ts) - 1
        #     tims = self._chars_ts
        #     if (tims[i] - tims[i - 1]).microseconds >= (1 * 10E6):
        #         # reset the characters and timestamps if we wait
        #         # for longer than 3 seconds
        #         self._chars = []
        #         self._chars_ts = []

        self._chars.append(event.key)
        self._chars_ts.append(ts)

        if len(self._chars) >= self._char_hist_len:
            self._chars = self._chars[1:]
            self._chars_ts = self._chars_ts[1:]

        # update CPM counter
        self.cpmcount = calculate_cpm(self._chars, self._chars_ts)
        self.wpmcount = calculate_wpm(self._chars, self._chars_ts)