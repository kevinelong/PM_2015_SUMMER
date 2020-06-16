__author__ = 'stephen'
def age_check():
    age = raw_input("what is your age:  ")
    if age < 18:
        print "You are too young to buy something here!"
    else age >= 18:
        print"You can check out at anytime"

age_check()