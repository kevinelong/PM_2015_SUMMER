phonebook = {
    'blake': {'name': 'taylor blake', 'phone': '503-927-4482'},
    'henning': {'name': 'james hennings', 'phone': '352-586-7789'}
    'hennin': {'name': 'joe hennings', 'phone': '352-586-7789'}
    'henni': {'name': 'jp hennings', 'phone': '352-586-7789'}
    'hen': {'name': 'jones hennings', 'phone': '352-586-7789'}
    'henningsive': {'name': 'juan hennings', 'phone': '352-586-7789'}
    'hennkings': {'name': 'jennifer hennings', 'phone': '352-586-7789'}
}


def add_entry():
    fname = raw_input('Please enter the first name of the person you would like to add.: ')
    lname = raw_input('Please enter the last name of the person you would like to add.: ')
    phone = raw_input('Please enter the phone number of the person you would like to add.: ')
    add(fname, lname, phone)
    print 'Thank you. %s %s has been entered' % (fname, lname)
def add():
    phonebook[lname.lower()] = {'name': fname + ' ' + lname, 'phone': phone}
    print 'Thank you. %s %s has been entered' % (fname, lname)


def delete_entry():
    lname = raw_input('Please enter the name of the person you would like to delete.: ')
    if lname.lower() in phonebook.keys():
        delete_choice = raw_input('Are you sure you would like to delete %s?: ' % phonebook[lname.lower()]['name'])
        if delete_choice.lower() == 'y' or delete_choice.lower() == 'yes':
            deleted_name = phonebook[lname.lower()]['name']
            del phonebook[lname.lower()]
            print "Thank you, %s has been deleted." % deleted_name
        else:
            print "Deletion aborted."
    else:
        print 'That entry does not exist.'


def change_entry():
    person_change = raw_input('What is the last name of the entry you would like to change?: ')
    if person_change in phonebook.keys():
        fname = raw_input('Please enter the first name of the person you would like to change.: ')
        lname = raw_input('Please enter the last name of the person you would like to change.: ')
        phone = raw_input('Please enter the phone number of the person you would like to change.: ')
        del phonebook[lname.lower()]
        phonebook[lname.lower()] = {'name': fname + ' ' + lname, 'phone': phone}
        print 'Thank you. Your change has been made.'


def search_with(beginput):
    for key, item in phonebook:
        if beginput == key[:len(beginput)]:
            return True
    return False


while True:
    choice = raw_input("Enter 1 to search, 2 to add, 3 to change, 4 to delete or 5 to exit.: ")
    if choice == '1':
        search_with()
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