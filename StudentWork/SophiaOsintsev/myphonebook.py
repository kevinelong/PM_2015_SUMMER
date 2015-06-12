# Dictionary of dictionaries to hold data.
phonebook = {
    "harbor": {"name": "Vicki Harbor", "phone": "503-123-5565"},
    "rich": {"name": "Kyle Rich", "phone": "503-789-4398"},
    "green": {"name": " Rachel Green", "phone": "503-413-9843"},
    "douglas": {"name": "Anna Douglas", "phone": "360-436-8451"}}


# Function to add a contact to the phonebook 
def add(): 
    last = raw_input("What is the contacts last name? >> ")
    if last.lower() in phonebook:
        print "\nThis contact already exists!\n"
    else:
        first = raw_input("What is the contacts first name? >> ")
        phone = raw_input("What is the contacts phone number? >> ")
        phonebook[last.lower()] = {"name": first + " " + last, "phone": phone}
    print "\nThe new contact has been added!\n"


# Function to edit a contact. User can either edit the last name, first name or phone number
def edit(): 
        last = raw_input("What is the last name of the contact you want to edit? >> ")
        if last.lower() not in phonebook:
            print "\nThis contact does not exist!\n" 
            return
        else: 
            first = phonebook[last.lower()]["name"].split()[0]
            phone = phonebook[last.lower()]["phone"]
            
        selection = raw_input("""
            What would you like to change?
            \t1. Last name
            \t2. First name
            \t3. Phone number
            Please enter a choice by number. >> """)
        if selection == '1':
            new = raw_input("What is the new last name? ")
            phonebook[new.lower()] = {"name": first + " " + new, "phone": phone}

            del phonebook[last.lower()]
            print "\nThe contact information has been changed!\n"

        elif selection == '2':
            new = raw_input("What is the new first name?")
            phonebook[last.lower()] = {"name": new + " " + last, "phone": phone}
            print "\nThe contact information has been changed!\n"

        elif selection == '3':
            new = raw_input("What is the new phone number?")
            phonebook[last.lower()] = {"name": first + " " + last, "phone": new}
            print "\nThe contact information has been changed!\n"

        else:
            print "\nThat's not a choice! Please try again.\n"


# Function to delete a contact entry
def delete(): 
    last = raw_input("What is the last name of the contact you want to delete? >> ").lower()
    if last not in phonebook:
        print "\nThis contact does not exist!\n"
        return
    else: 
        print phonebook[last]["name"] + ":" + phonebook[last]["phone"]
        response = raw_input("Are you sure you want to delete this contact information? >> ")
        if response == 'yes':
            del phonebook[last]
            print "\nContact information has been deleted!\n"
            
            
# Function to search for a contact entry
def search():
    last = raw_input("What is the contacts last name? >> ").lower()
    if last not in phonebook:
        print "\nThis contact does not exist!\n"
        return 
    else: 
        print phonebook[last]["name"] + " : " + phonebook[last]["phone"]


done = False

while not done:
    choice = raw_input("""
        Please make a selection:
        \t1. Search by last name
        \t2. Add a contact
        \t3. Edit a contact
        \t4. Delete a contact
        \t5. Exit the system
        Please enter a choice by number. >> """)
    if choice == '1':
        search()
    elif choice == '2':
        add()
    elif choice == '3':
        edit()
    elif choice == '4':
        delete()
    elif choice == '5':
        done = True
    else:
        print "\nThat is not a valid choice!\n"
