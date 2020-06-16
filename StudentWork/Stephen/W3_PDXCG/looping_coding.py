__author__ = 'stephen'
import time


def ten_second_change():
   for seconds in range(10):
       if seconds > -1:
        time.sleep(1)
        print time.time()


ten_second_change()