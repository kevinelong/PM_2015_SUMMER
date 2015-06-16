#I'm updating this on the fly.
phonebook_list = [
    {'name': 'james hennings', 'phone': '352-586-8888'},
    {'name': 'joe hennings', 'phone': '352-586-8975'},
    {'name': 'jp hennings', 'phone': '352-586-7789'},
    {'name': 'jones hennings', 'phone': '352-586-4567'},
    {'name': 'juan hennings', 'phone': '352-586-1234'},
    {'name': 'jennifer hennings', 'phone': '352-586-8520'}
]


# def add_entry():
#     fname = raw_input('Please enter the first name of the person you would like to add.: ')
#     lname = raw_input('Please enter the last name of the person you would like to add.: ')
#     phone = raw_input('Please enter the phone number of the person you would like to add.: ')
#     add(fname, lname, phone)
#     print 'Thank you. %s %s has been entered' % (fname, lname)
# def add():
#     phonebook[lname.lower()] = {'name': fname + ' ' + lname, 'phone': phone}
#     print 'Thank you. %s %s has been entered' % (fname, lname)
#
#
# def delete_entry():
#     lname = raw_input('Please enter the name of the person you would like to delete.: ')
#     if lname.lower() in phonebook.keys():
#         delete_choice = raw_input('Are you sure you would like to delete %s?: ' % phonebook[lname.lower()]['name'])
#         if delete_choice.lower() == 'y' or delete_choice.lower() == 'yes':
#             deleted_name = phonebook[lname.lower()]['name']
#             del phonebook[lname.lower()]
#             print "Thank you, %s has been deleted." % deleted_name
#         else:
#             print "Deletion aborted."
#     else:
#         print 'That entry does not exist.'
#
#
# def change_entry():
#     person_change = raw_input('What is the last name of the entry you would like to change?: ')
#     if person_change in phonebook.keys():
#         fname = raw_input('Please enter the first name of the person you would like to change.: ')
#         lname = raw_input('Please enter the last name of the person you would like to change.: ')
#         phone = raw_input('Please enter the phone number of the person you would like to change.: ')
#         del phonebook[lname.lower()]
#         phonebook[lname.lower()] = {'name': fname + ' ' + lname, 'phone': phone}
#         print 'Thank you. Your change has been made.'


def searched_with(searched, beginput):
    return beginput == searched[:len(beginput)]


def search_with_in_list(beginput):
    matches = []
    for item in phonebook_list:
        full_name = item["name"]
        parts = full_name.split(" ")
        fname = parts[0]
        lname = parts[1]
        if searched_with(lname, beginput):
            matches.append(item)
    return matches

while True:
    choice = raw_input("Enter 1 to search, 2 to add, 3 to change, 4 to delete or 5 to exit.: ")
    if choice == '1':
       # print search_with_in_list(raw_input("Input the first three letters of the person's last name:\n"))
        search_term = raw_input("Input the first three letters of the person's last name:\n")
        matching_items = search_with_in_list(search_term)
        print matching_items
    elif choice == '2':
        add_entry()
    elif choice == '3':
        change_entry()
    elif choice == '4':
        delete_entry()
    elif choice == '5':
        exit()
    else:
        print '"%s" is not a valid choice. Please Try again.' % choice