#!/usr/bin/env python
__author__ = "Paul Anderson"
__copyright__   = "Copyright 2015, Die Laughing Media"
__date__ = "6/12/2015"
__version__ = "1.0.1"

# Dictionary of Names
contacts = {
    "haghan": {"name": "doug haghan", "phone": "555.555.5555"},
    "anderson": {"name": "paul anderson", "phone": "666.666.6666"},
    "vangrunsven": {"name": "casey vangrunsven", "phone": "777.777.7777"}
}

# Add a new contact
def add_contact():
    last_name = raw_input("What is your last name?: ").lower()
    if last_name in contacts:
        print "That name is already in this directory."
    else:
        first_name = raw_input("What is your first name?: ").lower()
        phone_number = raw_input("What is your phone number?: ")
        contacts[last_name] = {"name": first_name + " " + last_name, "phone": phone_number}
    print "\nContact has been added\n"
    print (" ")
    start_over()

# Delete a contact
def delete_contact():
    last_name = raw_input("What is the name last name you want to delete?: ").lower()
    if last_name in contacts:
        print contacts[last_name]["name"] + " " + contacts[last_name]["phone"]
        warning = raw_input("Are you sure you want to delete this contact? Yes or No.")
        if warning == "Yes" or "yes" or "Y" or "y":
            del contacts[last_name]
        else:
            print "\nContact has been deleted\n"
    print (" ")
    start_over()

# Edit a contact's: First name, Last name, or Phone Number
def edit_contact():
    last_name = raw_input("What is the last name of the contact you wish to edit?: ").lower()
    if last_name not in contacts:
        print "That name is not in this directory. Try again"
    else:
        first = contacts[last_name.lower()]["name"].split()[0]
        phone = contacts[last_name.lower()]["phone"]

        selection = raw_input("""
                    What do you want to change?
                    \t1. First Name
                    \t2. Last Name
                    \t3. Phone
                    \tEnter your Choice by number: """)

        if selection == "1":
            print contacts[last_name]["name"].split()[0].capitalize()
            new_first = raw_input("What is your first name?: ")
            contacts[last_name] = {"name": new_first.capitalize() + " " + last_name.capitalize()}
            print "Contact has been changed to", contacts[last_name]["name"]

        elif selection == "2":
            print contacts[last_name]["name"].split()[1].capitalize()
            new_last = raw_input("What is your last name?: ")
            contacts[last_name] = {"name": first.capitalize() + " " + new_last.capitalize()}
            print "Contact has been changed to", contacts[last_name]["name"]

        elif selection == "3":
            print phone
            new_phone = raw_input("What is your phone number?: ")
            contacts[last_name] = {"phone": new_phone}
            print "Contact's phone number has been changed to", new_phone
        else:
            print "Are you lost?"
    print (" ")
    start_over()

# Search for a contact
def search_contact():
    last_name = raw_input("What is the last name of the contact you're searching for?: ").lower()
    if last_name not in contacts:
        print "That name isn't in this directory."
    else:
        print contacts[last_name]["name"] + " : " + contacts[last_name]["phone"]
    start_over()

# Prints out all contacts in a readable list
def show_contact_list():
    for key, info in contacts.iteritems():
        print info["name"] + " : " + info["phone"]
    print (" ")
    start_over()

# Send you back to the opening menu
def start_over():
    start_over = raw_input("Return to main menu? Yes or No: ").lower()
    if start_over == "yes" or "y":
        choice()

# Opening menu
def choice():
    new_choice = raw_input("1 for add\n2 for delete\n3 for edit\n4 for search\n5 to show all contacts\n6 to exit\nMake a choice: ")
    if new_choice == "1":
        add_contact()
    elif new_choice == "2":
        delete_contact()
    elif new_choice == "3":
        edit_contact()
    elif new_choice == "4":
        search_contact()
    elif new_choice == "5":
        show_contact_list()
    elif new_choice == "6":
        exit()
    else:
        print "%s is not an option.  Please try again." %(new_choice)

choice()


