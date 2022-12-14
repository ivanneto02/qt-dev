from pynput import keyboard

def calculate_cpm(chars, times):

    # in case we only really have one record
    if (len(chars) <= 1):
        return 0

    sum = 0
    # calculate cpm
    for i in range(1, len(times)):
        try:
            sum += ( (1 / ((times[i]-times[i-1]).microseconds / 1000000) ) * 60 )
        except:
            sum += 0.01

    return sum / len(times)

def calculate_wpm(chars, times):

    # in case we only really have one record
    if (len(chars) <= 1):
        return 0

    # calculate cpm
    sum_s = 0
    curr  = 0
    words = 1
    for i in range(1, len(times)):
        # if there has been a change in
        if (chars[i] == keyboard.Key.space) and (chars[i - 1] != keyboard.Key.space):
            sum_s += (curr / 1000000)
            words += 1
            curr   = 0
        else:
            curr += (times[i]-times[i-1]).microseconds
    if (sum_s == 0):
        return 0

    return (words / sum_s) * 60