__author__ = 'lenny'
"""
Jesse Fitzjarrell
Summer 2015 Phish Tour Planner User Interface File
6-29-15
My first real Python file, let's do it.
"""
from Phish_Tour_Planner_Model import *

print "Welcome to the Phish Summer Tour Planner."
print "Hope you are as excited as I am about tour starting !!"

print "Press\n\t  1 to see a list of shows\n \t  2 to see the distance between you and a show\n\t  3 To calculate distances between consecutive shows on tour\n\t  4 If you don't like Phish and are not interested in seeing a phish show"

print "\nIf it is a multiple show night enter as bend Night 1, as an example"

print "\npick a number, 1 or 2 or 3 or 4"
while True:
    a = int(raw_input("> "))
    if a == 1:
        for elem in phish_show_list:
            print elem
        print '\nPress esc to return to main menu'


    elif a == 2:
        print "that"

    elif a == 3:
        print "another"

    elif a == 4:
        print "Guess you don't like seeing fun music in the sun. I have terminated the program for you."
        break
    else:
        print "you have made an invalid choice, try again."