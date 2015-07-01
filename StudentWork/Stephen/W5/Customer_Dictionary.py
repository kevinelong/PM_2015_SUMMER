__author__ = 'stephen'
#
# The Customer DICTIONARY is used to store Customer contact info.
import datetime

customer_list = []
# locations = ["Portland", "Vancouver"]
party_list = []


class Customer(object):

	def __init__(self, fname, lname, address, phone, email):
		self.fname = fname
		self.lname = lname
		self.address =address
		self.phone = phone
		self.email = email

	def __repr__(self):
	  return self.fname + " " + self.lname

	def set_fname(self, fname="john"):
		self.fname = fname

	def set_lname(self, lname="Davis"):
		self.lname = lname

	def set_address(self,address="Street City State Zip"):
		self.address = address

	def set_phone(self,phone=1233334444):
		"""
		May need function to remove dashes, dots, and paraenthesises from phonenumbers
		"""
	def set_email(self, email= "words@server.org"):
		self.email = email
	"""
	create a new user here
	"""

def add_customer(fname, lname, address, phone, email):
	customer = Customer(fname, lname, address, phone, email)
	customer_list.append(customer)

def add():
	fname = raw_input("Please enter the first name of your new Contact you are adding: ")
	lname = raw_input("Enter the last name of your new Contact: ")
	address = raw_input("Please enter your address here:   ")
	phone = raw_input("Enter the phone number of your new Contact here: ")
	email = raw_input("Enter the email of your new Contact:  ")
	print "this is the information you entered, is it correct?"
	print fname
	print lname
	print address
	print phone
	print email
	choice = raw_input("")
	if choice == "yes" or choice == "y":
		add_customer(fname, lname, address, phone, email)

add()
print customer_list




class Party(object):
	def __init__(self, location, date, time, party, qty_guests, primary_guest):
		self.location = []
		self.date = date
		self.time = time
		self.party = party
		self.qty_guests = qty_guests
		self.primary_guest = primary_guest

	def __repr__(self):
		return self.location + "\n" + self.date + "\n" + self.time + "\n" + self.party + "\n" + self.qty_guests + "\n" + self.primary_guest


	def set_location(self, location ):
		self.location = location
		# self.portland = portland
		# self.vancouver = vancouver

	def set_date(self, date="date from datetime"):
		self.date = date

	def set_time(self, time= "time from datetime"):
		self.time = time

	def set_party(self, party ="party"):
		self.party = party

	def set_qty_guests(self, qty_guests= 5):
		self.qty_guests = qty_guests

	def set_primary_guest(self, primary_guest ="name"):
		self.primary_guest = primary_guest

def add_party(location, date, time, party, qty_guests, primary_guest):
	party = Party(location, date, time, party, qty_guests, primary_guest)
	party_list.append(party)

def new_party():
	location = raw_input("Please enter the location you wish to use \n Portland\nVancouver\n:    ")
	date = raw_input("Enter the Date for your party\n :  ")
	time = raw_input("Please enter the time for your party to start:   ")
	party = raw_input("What type of party would you like? \n\nOpen Studio\nMessy Madness\nAdvanced Artistry\nPrivate Party\n  : ")
	qty_guests = raw_input("How many guest are attending? :  ")
	primary_guest = raw_input("Is there a Guest of Honor? Put in their name here\n: ")
	print "this is the information you entered, is it correct?"
	print location
	print date
	print time
	print party
	print qty_guests
	print primary_guest
	choice = raw_input("")
	if choice == "yes" or choice == "y":
		add_party(location, date, time, party, qty_guests, primary_guest)

new_party()
print party_list


















	#
	# def get_location_choices(self, portland, vancouver):
	# 	return ['Portland', 'Vancouver']
	#

	# class Locations(object):
	# 	def portland(self, portland):
	# 		self.portland = portland
	# 	def vancouver(self, vancouver):
	# 		self.vancouver = vancouver






		 # choice = raw_input("Thanks for choosing the Company to book your party with.\n Please choose the location you are interested in having your party at" \n Portland = Portland \n Vancouver = Vancouver)

	# def new_party():
	# 	location = raw_input("Please choose the location you are interested in having your party at  ")
	#
	# def add():
	# 	fname =
	# 	lname = raw_input("Enter the last name of your new Contact: ")
	# 	address = raw_input("Please enter your address here:   ")
	# 	phone = raw_input("Enter the phone number of your new Contact here: ")
	# 	email = raw_input("Enter the email of your new Contact:  ")


