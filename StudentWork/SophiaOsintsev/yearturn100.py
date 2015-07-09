#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
#tells them the year that they will turn 100 years old.

#from datetime import date
#print date.today()

#def greeting():
    #name = raw_input("Please enter your name: ")
   # age = int(raw_input("Please enter your age: "))
  #  year = str((2015 - age)+100)
 #   print(name + " will be 100 years old in the year " + year)
#greeting()

# or


from datetime import date

def usr_input():
    global name, age
    name = raw_input("Please enter your name: ")
    a = True
    while a:
        try:
            age = int(raw_input("Please enter your age: "))
            a = False
        except ValueError:
            print "That is not a valid age."

def message(user, usr_age):
    h_years = what_year(usr_age)
    print "Hello %s, you will be 100 in the year %s" % (user, h_years)
def what_year(year_age):
    x = date.today().year
    return (x - year_age) + 100

usr_input()
message(name, age)