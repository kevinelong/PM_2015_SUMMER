import time

# Create a dictionary of dictionaries to hold your data.
phonebook = [
            {"fname": "Dar", "lname": "Wright", "phone": "XXX-XXX-XXXX"},
            {"fname": "Luigi", "lname": "Mario", "phone": "505-123-4567"},
            {"fname": "Mario", "lname": "Mario", "phone": "555-123-4567"}
            ]


def add():
    # Function for adding entries
    while True:
        print "Add an entry:\n" \
              "~~~~~~~~~~~~"
        fname = str.capitalize(raw_input("Please enter the first name: "))
        lname = str.capitalize(raw_input("Please enter the last name: "))
        phone = raw_input("Please enter the phone number in this format XXX-XXX-XXXX: ")
        build_entry = {"fname": fname, "lname": lname, "phone": phone}
        print build_entry["fname"], build_entry["lname"], build_entry["phone"]
        choice = str.lower(raw_input("Is this the entry you wish to add? Yes or No: "))
        if choice == 'yes' or choice == 'y':
            phonebook.append(build_entry)
            break
        else:
            break


def change():
    # Function to change entries

    pass


def delete():
    # Function to delete entries
    while True:
        print "Delete an entry:\n" \
              "~~~~~~~~~~~~~~~~\n" \
              "Loading Search Menu...\n"
        time.sleep(1)
        entry_list = search()
        if len(entry_list) == 1:
            for entry in entry_list:
                del_entry = str.lower(raw_input("This is the entry you wish to delete? Yes or No: ?"))
                if del_entry == 'yes' or del_entry == 'y':
                    phonebook.remove(entry)
                elif choice == 'no' or choice == 'n':
                    break
        elif len(entry_list) > 1:
            print "Sorry, too many entries, please use a different search method to narrow the choice.\n"


def search_fname(name):
    name = str.capitalize(name)
    found = []
    for n in phonebook:
        if name == n["fname"]:
            found.append(n)
    return found


def search_lname(name):
    name = str.capitalize(name)
    found = []
    for n in phonebook:
        if name == n["lname"]:
            found.append(n)
    return found


def search_phone(phone):
    phone = phone
    found = []
    for n in phonebook:
        if phone == n["phone"]:
            found.append(n)
    return found


def search():
    # Function to search for entries
    while True:
        choice = raw_input("Search Menu:\n"
                           "~~~~~~~~~~~~\n"
                           "Press 1 to search by first name.\n"
                           "Press 2 to search by last name. \n"
                           "Press 3 to search by phone number.\n"
                           "Press 4 to quit.\n"
                           ">>\n")
        if choice == '1':
            name = raw_input("Please enter the first name: ")
            entries = search_fname(name)
            if not entries:
                print "\nNo match found.\n"
            else:
                for n in entries:
                    print "\n****Match found!****"
                    print n["fname"], n["lname"], n["phone"] + "\n"
            return entries
        elif choice == '2':
            name = raw_input("Please enter the last name: ")
            entries = search_lname(name)
            if not entries:
                print "\nNo match found.\n"
            else:
                for n in entries:
                    print "\n****Match found!****"
                    print n["fname"], n["lname"], n["phone"] + "\n"
            return entries
        elif choice == '3':
            phone = raw_input("Please enter the phone number in this format XXX-XXX-XXXX: ")
            entries = search_phone(phone)
            if not entries:
                print "\nNo match found.\n"
            else:
                for n in entries:
                    print "\n****Match found!****"
                    print n["fname"], n["lname"], n["phone"] + "\n"
            return entries
        elif choice == '4':
            exit()
        else:
            print "Please enter a valid option.\n"


while True:
    choice = raw_input("Phone Book Menu:\n"
                       "~~~~~~~~~~~~~~~~\n"
                       "Enter 1 to search\n"
                       "Enter 2 to add\n"
                       "Enter 3 to update\n"
                       "Enter 4 to delete\n"
                       "Enter 5 to quit\n"
                       ">> ")
    if choice == '1':
        search()
    elif choice == '2':
        add()
    elif choice == '3':
        change()
    elif choice == '4':
        delete()
    elif choice == '5':
        exit()
    else:
        print "Not a valid choice. Please try again.\n\n"
