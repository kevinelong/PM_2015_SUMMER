from time import time
import random


# print number everysecond for 10 seconds
# for i in range(100):
#     print "Time every second: %s" % time.strftime("%S")
#     time.sleep(1)

#
def random_num():
    start = time()
    while time() < start + 5:
        print random.randint(1, 5000)

# stop watch

def stopwatch():
    start = time()
    while time() < start + 5:
        print random.randint(1, 5000)


stopwatch()



