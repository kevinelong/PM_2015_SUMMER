# Code challenge from 6-22 (attempting on my own since I was not in class).

# Sets the file I want to write to/read from later in this program to the variable 'phonebook'.

phonebook = '/Users/rachel/Projects/PM_2015_SUMMER/StudentWork/RachelKlein/phonebook.txt'

# The user chooses whether they want to write to the file (add a new entry) or read from the file (search past entries).

choice = int(raw_input('Do you want to (1) search the phonebook or (2) add an entry to the phonebook?  '))

# Appends a phonebook entry the user gives to the phonebook.txt file.

if choice == 2:
    name = raw_input('What is the name of the person you wish to add?\nPlease format like this: Last name, First name ')
    phone_num = raw_input('What is the phone numer of the person you wish to add?\n Please format like this: 222-333-4444 ')

    with open(phonebook, 'a') as updated_phonebook:
        updated_phonebook.write('{},{}\n'.format(name, phone_num))

# Loops through the existing phonebook.txt entries, finds a match for the name, and prints that out.

elif choice == 1:
    name_requested = raw_input('Whose phone number would you like to access? Please format like this: Last name, First name ')
    with open(phonebook) as searchable_phonebook:
        for line in searchable_phonebook:
            name, phone_num = line.split(',')
            if name_requested == name:
                print 'The phone number of {} is {}'.format(name, phone_num)
            else:
            	print 'Sorry, I cannot find that name. Please try again.'