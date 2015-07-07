__author__ = 'stephen'
#
# The Customer DICTIONARY is used to store Customer contact info.
import datetime
import cPickle as pickle
pickle_file = '/home/stephen/Desktop/party_reg_save/'

customer_list = []
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
	print "\n\n\n\t\t\tThis is the information you entered, is it correct?\n Please enter yes or no."
	print fname
	print lname
	print address
	print phone
	print email
	choice = raw_input("")
	if choice == "yes" or choice == "y":
		add_customer(fname, lname, address, phone, email)
	elif choice == "no" or choice =="n":
		exit()
# 	I would like to add a choice to change a particular entry, but for now I will make this just exit out of the add option.
add()




class Party(object):
	def __init__(self, party, location, date, time, qty_guests, primary_guest):
		self.party = party
		self.location = location
		self.date = date
		self.time = time
		self.qty_guests = qty_guests
		self.primary_guest = primary_guest

	def __repr__(self):
		return  self.party + " " + self.location +" " + self.date +" " + self.time + " "+self.qty_guests + " " + self.primary_guest

	def set_party(self, party ="party"):
		self.party = party

	def set_location(self, location ):
		self.location = location
		# self.portland = portland
		# self.vancouver = vancouver

	def set_date(self, date="date from datetime"):
		self.date = date

	def set_time(self, time= "time from datetime"):
		self.time = time

	def set_qty_guests(self, qty_guests= 5):
		self.qty_guests = qty_guests

	def set_primary_guest(self, primary_guest ="name"):
		self.primary_guest = primary_guest

def add_party(party, location, date, time, qty_guests, primary_guest):
	party = Party(party, location, date, time, qty_guests, primary_guest)
	party_list.append(party)

def new_party():
	party = raw_input("Choose a party type. \n\nOpen Studio\nMessy Madness\nAdvanced Artistry\nPrivate Party\n: ")
	location = raw_input("Please enter the location you wish to use \n Portland\nVancouver\n:    ")
	date = raw_input("Enter the Date for your party\n :  ")
	time = raw_input("Please enter the time for your party to start:   ")
	qty_guests = raw_input('How many guest are attending? :  ')
	primary_guest = raw_input("Is there a Guest of Honor? Put in their name here\n: ")
	print "This is the information you entered, is it correct?\n Please enter yes or no."
	print party
	print location
	print date
	print time
	print qty_guests
	print primary_guest
	choice = raw_input("")
	if choice == "yes" or choice == "y":
		add_party(party, location, date, time, qty_guests, primary_guest)
	elif choice == "no" or choice =="n":
		exit()

new_party()
print "Thanks for booking your party with AAC :)"
print "Your party has been information has been added to our list."
print "We will get back to you within 24hrs."

print customer_list
print party_list

def

def search_customer_list(customer_list):
	while True:
		choice = raw_input("Customer Search:\n")
							"====================\n"
							"Enter 1 to lookup by First Name.\n"
							"Enter 2 to lookup by Last Name.\n""
							"Enter 3 to lookup by Phone Number.\n"
							"Enter 4 to exit the search option.\n"
							":  \n"
		if choice == "1":
			search1 = customer_list[0]
		elif choice =="2":
			search2 = customer_list[1]
		elif choice =="3":
			search3 = customer_list[3]
		else:
			exit()



		else:
			print "That is not an option. Lets try again."


def get_customer_by_name(customer_list, party_list):
	if customer_list != 0:
		print customer_list[0]
		print party_list[0]



get_customer_by_name(customer_list, party_list)