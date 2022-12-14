from pynput import keyboard
from datetime import datetime
import time
import random

# we place a single character per half second
# expected to see 120 characters per minute <---- test success
def main():

    history_length = 30

    chars = []
    times = []
    count = 0

    l = 0
    while(True):
        count = len(chars)

        if (l % 5) == 0:
            chars.append(2)
            times.append(datetime.now())
        else:
            chars.append(1)
            times.append(datetime.now())

        l += 1

        # trim off the lists based on history_length
        if len(times) > history_length:
            chars = chars[1:]
            times = times[1:]

        # Now calculate the CPM
        cpm = calc_cpm(chars, times)
        wpm = calc_wpm(chars, times)
        
        print(f"WPM: {wpm}, CPM: {cpm}")

        time.sleep( 0.5 )

    return 0

def calc_cpm(chars, times):

    # in case we only really have one record
    if (len(chars) <= 1):
        return 0

    # print((times[1] - times[0]).microseconds)

    sum = 0
    # calculate cpm
    for i in range(1, len(times)):
        sum += ( (1 / ((times[i]-times[i-1]).microseconds / 1000000) ) * 60 )

    return sum / len(times)

def calc_wpm(chars, times):

    # in case we only really have one record
    if (len(chars) <= 1):
        return 0

    # calculate cpm
    sum = 0
    curr = 0
    words = 1
    for i in range(1, len(times)):
        # if there has been a change in
        if (chars[i] == 2) and (chars[i - 1] != 2):
            sum += (curr / 1000000)
            words += 1
            curr = 0
        else:
            curr += (times[i]-times[i-1]).microseconds

    return sum / words


if __name__ == "__main__":
    main()