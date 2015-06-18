# Write a program that will bring out the time every second for 10 seconds (must use a loop of some kind)

import time
from datetime import datetime

def what_time_now():
    time_now = str(datetime.now())
    while True:
        print "The time is now %s." % time_now
        time.sleep(10)

what_time_now()