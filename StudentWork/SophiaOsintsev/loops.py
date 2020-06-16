# Write a program that will bring out the time every second for 10 secs (must use loop of some kind)
import time

start_time = time.time()
for t in range(10):
    time.sleep(1)
    print time.time()


# Write a program that wll print random numbers for a given length of time

import random
import datetime

print_time = datetime.datetime.now() + datetime.timedelta(seconds=3)
while print_time > datetime.datetime.now():
    print random.randint(0, 100)
print "I just printed a random number for 3 seconds!!!!!"