one_string = ['Jay']
two_strings = ['Stephen', 'Dar']
three_strings = ['Reina', 'Ollie', 'Rachel']

# This prints a list of items as a string with the Oxford comma.
# If I could do this method again I would make it a lot simpler so the same code would handle any length of list.

def list_to_string(list):
    length = len(list)
    if length == 2:
        return str(list[0]) + " and " + str(list[1])
    elif length >= 3:
        new_string = ''
        for x in xrange(length):
            new_string += (str(list[x])) + ", "
        new_string += "and " + str(list[1])
        return new_string
    else:
        return str(list[0])

print list_to_string(one_string)
print list_to_string(two_strings)
print list_to_string(three_strings)