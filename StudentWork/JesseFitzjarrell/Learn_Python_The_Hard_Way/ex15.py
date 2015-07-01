__author__ = 'lenny'

"""
Jesse Fitzjarrell
practicing learning python the hard way
Exercise 15: Reading Files
"""

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

