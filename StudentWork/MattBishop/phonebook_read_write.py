# with open('/Users/OfficeMax/Desktop/test.txt', 'rw') as my_file:
#     my_file.write('Class is so fun even when the weather is hot\n')
#
#
# lots_file_path = '/Users/OfficeMax/Desktop/test.txt'
# with open(lots_file_path) as lots_file:
#     for line in lots_file:
#         print line,
#


with open('/Users/OfficeMax/Desktop/test.txt', 'rw') as my_file:
    my_file = '/Users/OfficeMax/Desktop/test.txt'
    choice = int(raw_input('Do you want to add a name and phone number (1) or search for a number in the list? (2)?  '))

    if choice == 2:
        name_requested = raw_input('Who is the person you are attempting to look up?  ')
        with open(my_file) as test_file:
            for line in test_file:
                name, number = line.split(',')
        if name_requested == name:
            print 'The phone number of {} is {}'.format(name_requested, number)

    elif choice == 1:
        new_name = raw_input('Which name would you like to the directory?  ')
        new_number = raw_input('And what is the phone number?  ')
        with open(my_file) as test_file:
            for line in test_file:
                test_file.write('{},{}\n'.format(new_name, new_number))

