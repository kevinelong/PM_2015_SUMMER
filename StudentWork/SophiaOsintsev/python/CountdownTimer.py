import time

class CountdownTimer(object):
    def __init__(self):
        self.start = time.sleep

    def start_timer(self):
        start = raw_input("Start Timer? >>>  ")
        if start == "yes":
            for t in range(0,10):
                print 10 - t
                time.sleep(1)

    def stop_timer(self):
        self.end = time.time()


t = CountdownTimer()
t.start_timer()
time.sleep(1)
t.stop_timer()

print "Time is Up!!"