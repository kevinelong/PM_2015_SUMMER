def return_string(my_list):
    """
    write a function to turn a list of strings into a single word with commas.
    ['Reina', 'Ollie', 'Rachel'] becomes 'Reina, Ollie and Rachel, but
    ['Stephen', 'Dar'] become 'Stephen and Dar'
    """
    if my_list.count < 2:
        myString = " and ".join(my_list)
    else:
        myString = ', '.join(my_list)
    return myString


my_list = ['Reina', 'Ollie', 'Rachel']
my_list = return_string(my_list)
print my_list

my_list = ['Stephen', 'Dar']
my_list = return_string(my_list)
print my_list
