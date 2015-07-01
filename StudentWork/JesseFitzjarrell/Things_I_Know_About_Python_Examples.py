__author__ = 'lenny'
"""
Jesse Fitzjarrell
6-29-15
Python examples to go with my study of what I know in Python
"""

from sys import argv

print "practicing print functions"
print "butter"
print 30
print "butter",30

print "practicing printing math"
print 9+5
print 8/2
print 4*2

print "looking at math operators"

print 10/4,"10/4"
print 10%3,"10%3"

print "Learing about variables"

peaunt_butter = "delicious"
bacon = "glorious"
burger = "Fatty Meat"
pbpb = 5.95

print "the", peaunt_butter, bacon, burger, "is", pbpb,  "at Killer burger"

favorite_food = "Pizza"
favorite_beverage = "Beer"
favorite_place = "outdoors"

print "I really like to drink %s and eat %s when I am %s" %(favorite_beverage, favorite_food, favorite_place)

#I'm at chapter 8

free_time = "%r %r %r"
print free_time % ("sun", "fun", "music")

print "What is your favorite color?",
color = raw_input()
print "Your favorite color is %r"%(color)

print "You can input more than one input into a string"
print "What is your favorite food?",
food = raw_input()
print "Your favorite color is %r, and your favorite food is %r" %(color, food)

#I'm on ex 12 now

favorite_Band =raw_input("What is your favorite band? ")
print "Your favorite band is %r"% favorite_Band

from sys import argv

script, user_name = argv
prompt = '> '
