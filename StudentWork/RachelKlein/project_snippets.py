# This file contains code I cut from projects, works in progress, etc.

	def check_alarm(self):
		"""
		Allows the user to check any alarms that are in effect.
		"""
		current_alarm_hour = str(self.current_hour)
		current_alarm_minute = 0
		if self.alarm_minute < 10:
			current_alarm_minute = "0" + str(self.alarm_minute)
		else:
			current_alarm_minute = str(self.alarm_minute)
		print "Your current alarm is: {}:{}".format(current_alarm_hour, current_alarm_minute)
