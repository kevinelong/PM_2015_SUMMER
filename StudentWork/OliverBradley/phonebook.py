__author__ = 'Oliver'

# Create a dictionary of dictionaries to hold your data.
phonebook = {
    'jones': {'name': 'Chris Jones', 'phone': '503-277-9710'},
    'dover': {'name': 'Chelsea Dover', 'phone': '503-511-9981'},
    'bradley': {'name': 'Oliver Bradley', 'phone': '503-333-0475'}
}


def add():
    # Function for adding entries
    new_name = raw_input("Please enter the full name of the new phonebook entry: ")
    new_phone = raw_input("Please enter the corresponding phone number as 555-555-5555: ")
    new_key = new_name.split()
    phonebook[new_key[1].lower()] = {'name': new_name, 'phone': new_phone}

def change():
    # Function to change entries
    pick_name = raw_input("Enter the last name of the person whose record you would like to change: ").lower()
    if pick_name not in phonebook:
        print ("That name does not exist!")
        change()
    else:
        for key in phonebook:
            if key == pick_name:
                print "Found name!"
                edit_choice = raw_input("Please enter 1 to change a name or 2 to change a phone number: ")
                if edit_choice == "1":
                    edit_name = raw_input("What do you want to change the name to? ")
                    edit_key = edit_name.split()
                    phonebook[key]["name"] = edit_name
                    phonebook[edit_key[1].lower()] = phonebook.pop(pick_name)
                    print ("Name changed successfully!")
                    print phonebook
                elif edit_choice == "2":
                    edit_phone = raw_input("What do you want to change the phone number to? ")
                    phonebook[key]["phone"] = edit_phone
                    print ("Phone number changed successfully!")
                    print phonebook
                else:
                    print ("That is not a valid choice!")
                    change()


def delete():
    # Function to delete entries
    delete_name = raw_input("Please enter the last name of the person you want to remove: ").lower()
    print delete_name
    phonebook.pop(delete_name, None)


def search():
    # Function to search for entries
    pass


while True:
    choice = raw_input("press 1 to search, 2 to add, 3 to change, 4 to delete and 5 to exit: ")
    if choice == '1':
        search()
    elif choice == '2':
        add()
    elif choice == '3':
        change()
    elif choice == '4':
        delete()
    else:
        break
