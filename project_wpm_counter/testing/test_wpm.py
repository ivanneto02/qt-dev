from pynput import keyboard

from datetime import datetime

times = []
counts = []
count = 0

while(True):
    with keyboard.Events() as events:
        for event in events:
            if isinstance(event, keyboard.Events.Press):
                print(f"{event.key}")