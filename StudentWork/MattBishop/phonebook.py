# testing minor change

phone_book = {
    'smith': {'name': 'Adam Smith', 'phone': '555-555-5541'},
    'washington': {'name': 'George Washington', 'phone': '555-555-5542'},
    'rossum': {'name': 'Guido Rossum', 'phone': '555-555-5543'}
}

def add():
    new_name = raw_input("Please enter the full name of the person you wish to add: ")
    new_phone = raw_input("Please enter the telephone number for the entry: ")
    new_key = new_name.split()
    phone_book[new_key[1].lower()] = {'name': new_name, 'phone': new_phone}

def change():
    alter_name = raw_input("Enter the last name of the person whose record you'd like to change: ").lower()
    if alter_name not in phone_book:
        print ("That name does not exist - please make another selection.")
        change()
    else:
        for key in phone_book:
            if key == alter_name:
                print "Returned a match..."
                edit_choice = raw_input("Please enter 1 to change the name or 2 to change the phone number: ")
                if edit_choice == "1":
                    edit_name = raw_input("What do you wish to change the name to? ")
                    edit_key = edit_name.split()
                    phone_book[key]["name"] = edit_name
                    phone_book[edit_key[1].lower()] = phone_book.pop(alter_name)
                    print ("Change saved successfully.")
                elif edit_choice == "2":
                    edit_phone = raw_input("What do you want to change the phone number to? ")
                    phone_book[key]["phone"] = edit_phone
                    print ("Phone number changed successfully.")
                else:
                    print ("That is not a valid option. Please choose again.")
                    change()

def delete():
    delete_name = raw_input("Please enter the last name of the person you wish to delete: ").lower()
    print delete_name
    phone_book.pop(delete_name, None)
    print ("Record successfully deleted!")


def search():
        search_last = raw_input("Enter last name to search: ").lower()
        if search_last not in phone_book:
            print ("That name does not exist!")
            search()
        else:
            print ("Record found...")
            print phone_book[search_last]


while True:
    choice = raw_input("""                      Welcome to the main menu.
                           --------------------------
                            Press 1 to search for an entry
                                2 to add an entry to the phone book
                                    3 to change an entry in the phone book,
                                        4 to delete an entry from the system
                                            5 to exit the system
                                                Please make a selection: """)
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


