import time

# Create a dictionary of dictionaries to hold your data.
phonebook = [
    {"fname": "Dar", "lname": "Wright", "phone": "XXX-XXX-XXXX"},
    {"fname": "Luigi", "lname": "Mario", "phone": "505-123-4567"},
    {"fname": "Mario", "lname": "Mario", "phone": "555-123-4567"}
]


def add():
    fname = str.capitalize(raw_input("Please enter the first name: "))
    lname = str.capitalize(raw_input("Please enter the last name: "))
    phone = raw_input("Please enter the phone number in this format XXX-XXX-XXXX: ")
    choice = str.lower(raw_input("Is this the entry you wish to add? Yes or No: "))
    add_from_entries(fname, lname, phone, choice)
    mainmenu()

# add a new entry
def add_from_entries(fname, lname, phone, choice):
    # Function for adding entries
    while True:
        print "Add an entry:\n" \
              "~~~~~~~~~~~~"
        build_entry = {"fname": fname, "lname": lname, "phone": phone}
        make_sure_unique(build_entry)
        print build_entry["fname"], build_entry["lname"], build_entry["phone"]
        if choice == 'yes' or choice == 'y':
            phonebook.append(build_entry)
            print "Entry added.\n" \
                  "Returning to the main menu..."
            time.sleep(.5)
            return
        else:
            print "Add an entry canceled."
            return

def make_sure_unique(build_entry):
    return True

def test_add_from_entries():
    fname = 'Reina'
    lname = 'Abolofia'
    phone = '503-515-9787'
    choice = 'yes'
    add_from_entries(fname, lname, phone, choice)
    reina = {"fname": fname, "lname": lname, "phone": phone}
    assert(reina in phonebook)

    # check for duplicates
    # Reina was already added above, what happens when she's added again???
    # There should be an error message
    add_from_entries(fname, lname, phone, choice)
    reina_seen_times = 0
    for entry in phonebook:
        if entry['fname'] == 'Reina':
            reina_seen_times += 1
    assert(reina_seen_times == 1)


# change/update entry
def change():
    # Function to change entries
    while True:
        print "Update an entry:\n " \
              "~~~~~~~~~~~~~~~~\n" \
              "Loading Search Menu...\n"
        time.sleep(.5)
        entry_list = search()
        # checking to see if serch function returned more than 1 match
        if len(entry_list) == 1:
            for entry in entry_list:
                change_entry = str.lower(raw_input("This is the entry you wish to change Yes or No: ?"))
                if change_entry == 'yes' or change_entry == 'y':
                    change_type = int(raw_input("What field do you want to change?\n"
                                                "1 for first name.\n"
                                                "2 for last name.\n"
                                                "3 for phone number.\n"
                                                ">>"))
                    # change first name
                    if change_type == 1:
                        fname = str.capitalize(raw_input("Please enter the first name: "))
                        lname = entry["lname"]
                        phone = entry["phone"]
                        build_entry = {"fname": fname, "lname": lname, "phone": phone}
                        phonebook.remove(entry)
                        phonebook.append(build_entry)
                        print "Entry updated!\n" \
                              "Returning to the main menu..."
                        time.sleep(.5)
                        mainmenu()
                    # change last name
                    elif change_type == 2:
                        fname = entry["fname"]
                        lname = str.capitalize(raw_input("Please enter the last name: "))
                        phone = entry["phone"]
                        build_entry = {"fname": fname, "lname": lname, "phone": phone}
                        phonebook.remove(entry)
                        phonebook.append(build_entry)
                        print "Entry updated!\n" \
                              "Returning to the main menu..."
                        time.sleep(.5)
                        mainmenu()
                    # change phone number
                    elif change_type == 3:
                        fname = entry["fname"]
                        lname = entry["lname"]
                        phone = raw_input("Please enter the phone number in this format XXX-XXX-XXXX: ")
                        build_entry = {"fname": fname, "lname": lname, "phone": phone}
                        phonebook.remove(entry)
                        phonebook.append(build_entry)
                        print "Entry updated!\n" \
                              "Returning to the main menu..."
                        time.sleep(.5)
                        mainmenu()
                    else:
                        print "Please enter a valid option.\n"
                else:
                    print "Change entry canceled."
                    mainmenu()
        elif len(entry_list) > 1:
            print "Sorry, too many entries, please use a different search method to narrow the choice.\n"
        else:
            mainmenu()


# delete an entry function
def delete():
    # Function to delete entries
    while True:
        print "Delete an entry:\n" \
              "~~~~~~~~~~~~~~~~\n" \
              "Loading Search Menu...\n"
        time.sleep(.5)
        entry_list = search()
        # checking if there is only 1 item returned by search function
        if len(entry_list) == 1:
            for entry in entry_list:
                del_entry = str.lower(raw_input("This is the entry you wish to delete? Yes or No: ?"))
                if del_entry == 'yes' or del_entry == 'y':
                    phonebook.remove(entry)
                    print "Entry deleted!\n" \
                        "Returning to the main menu..."
                    time.sleep(.5)
                    mainmenu()
                elif del_entry == 'no' or del_entry == 'n':
                    mainmenu()
        elif len(entry_list) > 1:
            print "Sorry, too many entries, please use a different search method to narrow the choice.\n"


# first name search function
def search_fname(name):
    name = str.capitalize(name)
    found = []
    for n in phonebook:
        if name == n["fname"]:
            found.append(n)
    return found


# last name search function
def search_lname(name):
    name = str.capitalize(name)
    found = []
    for n in phonebook:
        if name == n["lname"]:
            found.append(n)
    return found


# phone search function
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
        # get first name to search by, pas to first name search
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
        # get last name to search by, pass to last name search
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
        # get phone number and pass to phone search
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
            mainmenu()
        else:
            print "Please enter a valid option.\n"


# main phone book menu function. drives all options. all options return here.
def mainmenu():
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
        time.sleep(.5)
        mainmenu()
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


test_add_from_entries()
mainmenu()
