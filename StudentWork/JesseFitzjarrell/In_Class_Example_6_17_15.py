__author__ = 'lenny'
import time
import datetime
# time = time.now()
# for t in time():
#     print time
now = datetime.datetime.now()
localtime = datetime.time(now.hour, now.minute, now.second)
print "Local current time :", localtime
for t in range(5):
    print localtime
    time.sleep(1)