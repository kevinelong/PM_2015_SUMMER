__author__ = 'stephen'
#
# The Customer DICTIONARY is used to store Customer contact info.
#
class CustomerDictionary:
    def __init__(self):
        self.fname = " "
        self.lname = " "
        self.address = "Street City State Zip"
        self.phone = 1233334444
        self.email = "words@server.org"

    def __repr__(self):
      return self.name

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
    def add_customer(self,fname,lname,address,phone,email):
        self.fname = (fname)
        self.lname = (lname)
        self.address = (address)
        self.phone = (phone)
        self.email = (email)
        # return {fname + lname + address:address + phone:phone + email:email}



print CustomerDictionary









#
# class CustomerContactInfo:
#     def __init__(self):
#         self.numofusers = 0
#         self.customerlist = []
#
#     def add_customer(self, customer):
#         self.itemlist.append(item)
#         return self.itemlist
#
#     def remove_item(self):
#         # search through the customer list
#         # offer or print customer information
#         #
#         # remove the item
#         # for item in self.itemlist:
#             pass
#     def show_items(self):
#         print self.itemlist
#         #TODO make this look pretty
