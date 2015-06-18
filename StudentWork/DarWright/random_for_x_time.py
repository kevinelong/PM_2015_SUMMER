import time
import random

def random_for_x_time(num):
    """
    write a program that will print random numbers for a given length of time (in seconds):
    """
    start = time.time()
    end = start + num
    while start < end:
        ran = random.randint(1000, 100000000000)
        start = time.time()
        print ran


random_for_x_time(5)

