import random
import time

def one_in_six():

    result = random.randint(1, 6)
    time.sleep(1)
    if result == 1:
        print 1
        return result
    if result == 2:
        print 2
        return result
    if result == 3:
        print 3
        return result
    if result == 4:
        print 4
        return result
    if result == 5:
        print 5
        return result
    if result == 6:
        print 6
        return result

def run():
    x = []
    while sum(x) <= 50:
        y = one_in_six()
        x.append(y)

print "This will generate random numbers (1-6) until the combined sum reaches 50."
time.sleep(1)
run()