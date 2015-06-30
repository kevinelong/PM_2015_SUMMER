__author__ = 'stephen'
#
# The Customer DICTIONARY is used to store Customer contact info.

customer_list =[]

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



    def __init__(self, location, date, time,ptype, numofguests, ):
        self.fname = fname
        self.lname = lname
        self.address =address
        self.phone = phone
        self.email = email




