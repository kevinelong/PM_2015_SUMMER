"""
Work in Progress - Need to figure out how to make alarm work
"""


from datetime import datetime, date, time, timedelta
import time

class Alarm(object):

    def __init__(self):
        """
            Grabs current time by hour and minute
        """
        self.current_time = datetime.now().strftime('%-I:%M%p')
        # self.current_time = time.localtime()

    def wake_time(self, user_time):
        print user_time
        print self.current_time
        if user_time == self.current_time:
            print "Gooood Morning?"
            # new_snooze = raw_input("Or snooze (Type Snooze): ").lower()
            # if new_snooze == "snooze":
            #     alarm_snooze = Alarm()
            #     alarm_snooze.snooze()
            # else:
            #     new_alarm()
        else:
            print "Your alarm is set for " + user_time
            """
                Looking for a solution
            """

    # def snooze(self):
    #     more_sleep = raw_input("Do you want to snooze? Yes or No: ").lower()
    #     if more_sleep == "yes" or "y":
    #         snooze_time = self.current_time + datetime.timedelta(minutes=15)
    #         new_alarm(snooze_time)

def new_alarm():
    current_time = Alarm()
    alarm_time = raw_input("The time now is {}. Enter your alarm time (00:00 AM): ".format(current_time.current_time))
    current_time.wake_time(alarm_time)

new_alarm()

# now = time.localtime()
# print now.tm_hour, now.tm_min

