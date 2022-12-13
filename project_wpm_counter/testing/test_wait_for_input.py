from pynput import keyboard
from datetime import datetime
import threading
import time

times  = []
counts = []
count  = 0

curr   = False

chars  = []
ts     = []

def commonIntervals():
    while(True):
        print(datetime.now())
        time.sleep(0.1)

def keyboardInput():
    while(True):
        with keyboard.Events() as events:
            for event in events:
                if isinstance(event, keyboard.Events.Press):
                    # print(f"{event.key}")
                    print(datetime.now())

if __name__ == "__main__":
    t1 = threading.Thread(target=commonIntervals)
    t2 = threading.Thread(target=keyboardInput)

    t1.start()
    t2.start()

    t1.join()
    t2.join()