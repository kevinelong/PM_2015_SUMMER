import time
import datetime

class AlarmClock(object):

def __init__(self):
	"""
	These alarm clocks start out showing the current time. No need to set them! :)
	They don't have any alarm to start.
	"""
	current_datetime = datetime.datetime.now()
	self.current_hour = current_datetime.hour
	self.current_minute = current_datetime.minute
	self.alarm_hour = 0
	self.alarm_minute = 0
	# self.user_interface()

# INTERNAL METHODS

def set_alarm(self, new_alarm_hour, new_alarm_minute):
	"""
	Allows the user to set the time for a future alarm.
	"""
	self.alarm_hour = new_alarm_hour
	self.alarm_minute = new_alarm_minute

def run_alarm(self, alarm_hour, alarm_minute):
	"""
	Runs the alarm the user set so it checks the time every minute and goes off at the right time.
	In a future version of this program, we could make this process open in a different file when
	the alarm is set (so the loop doesn't stop everything else.)
	In the current form of this program it doesn't execute.
	"""
	# TODO: Make this work! Currently I can make the alarm go off immediately
	# but I cannot make it go off in one minute (test instance below).
	# FURTHER TODO: Make this do something cooler when the alarm goes off!
	# Maybe a "clock radio" setting that plays music by opening a webpage?
	while self.current_hour != alarm_hour or self.current_minute != alarm_minute:
		current_datetime = datetime.datetime.now()
		self.current_hour = current_datetime.hour
		self.current_minute = current_datetime.minute
		time.sleep(10)
		print "+"
	else:
		print "YOUR ALARM IS GOING OFF!!!!!! \n" * 10

def has_alarm_set(self):
	if self.alarm_hour != 0 and self.alarm_minute != 0:
		return True
	else:
		return False

# OUTPUT TO USER

def user_interface(self):
	self.get_current_time()

	alarm_choice = raw_input("Would you like to set an alarm? y/n ")
	if alarm_choice.lower() == "y" or alarm_choice.lower() == "yes":
		self.user_set_alarm()

	menu_choice = raw_input(
	"""Now what would you like to do?
	Press 1 to check the current time.
	Press 2 to set a new alarm.
	Press 3 to quit. """)
	if menu_choice == "1":
		self.get_current_time()
	elif menu_choice == "2":
		self.user_set_alarm()
	elif menu_choice == "3":
		exit()

def format_minutes(self, current_minute):
	"""
	Creates standard human-readable format for minutes (e.g. 7:02 rather than 7:2)
	"""
	if self.alarm_minute < 10:
		current_alarm_minute = "0" + str(self.alarm_minute)
	else:
		current_alarm_minute = str(self.alarm_minute)
	return current_alarm_minute

def get_current_time(self):
	"""
	Prints current time for the user.
	"""
	# TODO: Fix this! It's not printing out the correct time. Do we need to refresh?
	hour = self.current_hour
	minute = self.current_minute
	minute = self.format_minutes(minute)
	print "The current time is: {}:{}".format(hour, minute)

def user_set_alarm(self):
	"""
	Takes user input and sets alarm, then confirms alarm to user.
	"""
	user_alarm_hour = raw_input("""Please enter the hour of your new alarm
		(ex. 14 if you want the alarm to go off at 2:XX): """)
	user_alarm_minute = raw_input("""Please enter the minutes of your new alarm
		(ex. 02 if you want the alarm to go off at X:02): """)
	self.set_alarm(user_alarm_hour, user_alarm_minute)
	user_alarm_minute = self.format_minutes(user_alarm_minute)
	print "Your current alarm is set to {}:{}.".format(user_alarm_hour, user_alarm_minute)

alarmclock = AlarmClock()
alarmclock.user_interface()

# alarmclock.run_alarm(alarmclock.current_hour, alarmclock.current_hour + 1)

# def test_init_time():
# 	alarmclock = AlarmClock()
# 	current_datetime = datetime.datetime.now()
# 	assert(alarmclock.current_hour == current_datetime.hour)
# 	assert(alarmclock.current_minute == current_datetime.minute)

# def test_set_alarm():
# 	alarmclock = AlarmClock()
# 	assert(alarmclock.alarm_hour == 0)
# 	assert(alarmclock.alarm_minute == 0)

# 	alarmclock.set_alarm(7, 40)
# 	assert(alarmclock.alarm_hour == 7)
# 	assert(alarmclock.alarm_minute == 40)

# def test_has_alarm_set():
# 	alarmclock = AlarmClock()
# 	assert(alarmclock.has_alarm_set() == False)

# 	alarmclock.set_alarm(7, 40)
# 	assert(alarmclock.alarm_hour == 7)
# 	assert(alarmclock.alarm_minute == 40)

# 	assert(alarmclock.has_alarm_set() == True)


# print "Beginning of tests."
# test_init_time()
# test_set_alarm()
# test_has_alarm_set()
# print "End of tests."