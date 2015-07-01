__author__ = 'lenny'
"""
I made this file so I can sample one piece of code at a time
Jesse Fitzjarrell
6-29-15
"""

from sys import argv

script, favorite_car = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (favorite_car, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % favorite_car
likes = raw_input(prompt)

print "Where do you live %s?" % favorite_car
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)