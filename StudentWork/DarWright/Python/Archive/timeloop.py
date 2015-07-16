import time
import datetime

def timeloop(num):
    """
    Make a program that will bring out the time every second for ten seconds
    (must use a loop of some kind)
    """
    a = num
    b = a + 10
    while a < b:
        time.sleep(1)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print st
        a += 1

timeloop(15)
