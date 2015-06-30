from time import time, strftime, sleep
import random

# This method prints out the hour, minute, and second every second
# for a number of seconds supplied by the user.

def timeout(number_seconds):
    for x in range(number_seconds):
        print strftime("%H:%M:%S")
        sleep(1)


# This method prints a random number between 1 and 100 every second
# for a number of seconds supplied by the user.

def random_number_time(range):
    for x in range(range):
        print random.randrange(1, 100)
        sleep(1)


# This method prints random numbers as fast as possible
# for a number of seconds supplied by the user.

def random_number_time_faster():
    start = time()
    now = 0.0
    while now - start <= 3:
        print random.randrange(1, 100)
        now = time()


# This is a stopwatch.

def stopwatch_start():
    global stopwatch_start_time
    stopwatch_start_time = 0.0
    raw_input("To start the stopwatch, please press enter > ")
    stopwatch_start_time = time()
    stopwatch_stop()


def stopwatch_stop():
    global stopwatch_stop_time
    stopwatch_stop_time = 0.0
    raw_input("To stop the stopwatch, please press enter > ")
    stopwatch_stop_time = time()
    stopwatch_tell_time()


def stopwatch_tell_time():
    stopwatch_total_time = stopwatch_stop_time - stopwatch_start_time
    print "Total time: %d seconds" % stopwatch_total_time


stopwatch_start()
