# Work along file to get concepts in my head.  Understanding of the greater concept is in process.

# Create a dictionary of dictionaries to hold your data.
phonebook = {
    'anderson': {'name': 'Paul Anderson', 'phone': '503.799.0556'},
    'personman': {'name': 'Guy Personman', 'phone': '555.555.5555'},
    'duderson': {'name': 'Dude Duderson', 'phone': '555.666.7777'},
}

def add():
    last = raw_input("What is your last name?: ").lower()
    if last in phonebook:
        print "\nThis contact already exist!\n"
    else:
        first = raw_input("Enter your first name: ").lower()
        phone = raw_input("Enter your phone: ")
        phonebook[last] = {"name": first + " " + last, "phone": phone}
    print "\nThis new contact has been added\n"

def change():
    last = raw_input("What is your last name?: ")
    if last.lower() in phonebook:
        print "\nThis contact already exists.\n"
    else:
        first = phonebook[last.lower()]["name"].split()
        phone = phonebook[last.lower()]["phone"]

        selection = raw_input("""
            What would you like to change?
            \t1. Last Name
            \t2. First Name
            \t3. Phone Number
            Enter your choice by number.""")

    if selection == '1':
        new = raw_input("What is the new last name? ")
        phonebook[last.lower()] = {"name": first + " " + new, "phone": phone }
        print "\nThe contact info has been changed"

    elif selection == '2':
        new = raw_input("What is the new first name? ")
        phonebook[last.lower()] = {"name": new + " " + last, "phone": phone }
        print "\nThe contact info has been changed"

    elif selection == '3':
        new = raw_input("What is the new phone? ")
        phonebook[last.lower()] = {"name": new + " " + last, "phone": new }
        print "\nThe contact info has been changed"

    else:
        print "\nThat's not a choice! Please try again."

def delete():
    last = raw_input("What is the last name of the contact you want to delete?: ").lower()
    if last not in phonebook:
        print "\nThis contact does not exist!\n"
        return
    else:
        print phonebook[last]["name"] + " : " + phonebook[last]["phone"]
        warning = raw_input("Are you sure you want to delete this?")
        if warning == 'Yes' or 'y' or 'Y':
            del phonebook[last]
        else:
            print "\nContact info has been deleted"



def search():
    last = raw_input("What is your last name?: ").lower()
    if last not in phonebook:
        print "\nThis contact doesn not exist!\n"
        return
    else:
        print phonebook[last]["name"] + " : " + phonebook[last]["phone"]




while True:
    choice = raw_input("Press 1 to search, 2 to add, 3 to change, 4 to delete, 5 to exit.: ")
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
        print "%s is not a valid choice.  Please Try Again." % choice
