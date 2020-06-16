# The phonebook is a dictionary of dictionaries.

phonebook = {
    "klein": { "name": "Rachel Klein", "phone": "541-231-2603" },
    "hauck": { "name": "Buzzy Hauck", "phone": "541-231-2569" }
}

# Function to add entries

def add():
    firstname = raw_input("Please enter a first name: ")
    lastname = raw_input("Please enter a last name: ")
    phonenum = raw_input("Please enter a phone number: ")
    if len(phonenum) != 12:
        print "Please use this format for phone numbers: 000-000-0000"
        add()
    else:
        print "Thank you. %s %s has been added." % (firstname, lastname)
    phonebook[lastname.lower()] = { "name": firstname + " " + lastname, "phone": phonenum }

# Function to change entries

def change():
    lastname = raw_input("Please enter the last name of the person whose phonebook entry you want to change: ")
    phone_key = lastname.lower()

    if phone_key not in phonebook:
        print "Sorry, that person does not exist in the phonebook."
        return

    else:
        firstname = phonebook[phone_key]["name"].split()[0]
        phonenum = phonebook[phone_key]["phone"]

        change = raw_input("Enter 1 to change last name, 2 to change first name, or 3 to change phone number: ")

        if change == '1':
            new_last = raw_input("Please enter the new last name: ")
            phonebook[new_last.lower()] = { "name": firstname + " " + new_last, "phone": phonenum}

        elif change == '2':
            new_first = raw_input("Please enter the new first name: ")
            phonebook[phone_key] = { "name": new_first + " " + lastname, "phone": phonenum}

        elif change == '3':
            new_num = raw_input("Please enter the new phone number: ")
            phonebook[phone_key] = { "name": firstname + " " + lastname, "phone": new_num}

        else:
            print "Sorry, I do not understand that."
            return

# Function to delete entries

def delete():
    lastname = raw_input("Please enter the last name of the entry you want to delete from the phonebook: ")
    print phonebook[lastname.lower()]
    delete_this = raw_input("Are you sure you want to delete this entry? y/n ")
    if delete_this.lower() == "y" or delete_this.lower() == "yes":
        del phonebook[lastname.lower()]
    elif delete_this.lower() == "n" or ifdel.lower == "no":
        return

# Function to search for entries (return full name and phone)

def search():
    lastname = raw_input("Please enter the last name of the entry you want to find in the phonebook: ")
    phone_key = lastname.lower()

    if phone_key in phonebook:
        print phonebook[lastname.lower()]
    else:
        print "Sorry, that person is not in the phonebook."

# Returning users to the menu.

while True:
    choice = raw_input("press 1 to search, 2 to add, 3 to delete, 4 to change ")
    if choice == '1':
        search()
    elif choice == '2':
        add()
    elif choice == '3':
        delete()
    elif choice == '4':
        change()
    else:
        print "Please choose from one of the options provided."