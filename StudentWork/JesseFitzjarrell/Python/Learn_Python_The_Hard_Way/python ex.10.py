__author__ = 'lenny'

"""
Jesse Fitzjarrell
practicing learning python the hard way
Exercise 10: What Was That?
"""

"I am 6'2\" tall." # escape double-quote inside string
'I am 6\'2" tall. ' # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat Food
\t* fishies
\t* catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
     for i in ["/", "-", "|", "\\", ",", "|" ]:
         print "%s\r" %i