__author__ = 'lenny'

# write a function to turn a list of strings into a single word with commas (ie
# ['Reina', 'Ollie', 'Rachel'] becomes 'Reina, Ollie, and Rachel' but
# ['Stephen', 'Dar'] becomes 'Stephen and Dar'

def remove_oxford_comma(value):
    if len(value) ==2:
        return ["" "and"""]

    elif len(value) ==3:
            return  ["", "", "" ]

value = ['Reina', 'Ollie', 'Rachel']

