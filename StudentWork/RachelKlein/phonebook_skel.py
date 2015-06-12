# Create a dictionary of dictionaries to hold your data.
phonebook = {
    "klein": { "name": "Rachel Klein", "phone": "541-231-2603" },
    "hauck": { "name": "Buzzy Hauck", "phone": "541-231-2569" }
}

# Function for adding entries

def add():
    firstname = raw_input("Please enter a first name: ")
    lastname = raw_input("Please enter a last name: ")
    phonenum = raw_input("Please enter a phone number: ")
    phonebook[lastname.lower()] = { "name": firstname + " " + lastname, "phone": phonenum}
    print "Thank you. %s %s has been added." (firstname, lastname)

# Function to change entries

def change():
    pass

# Function to delete entries

def delete():
    print phonebook
    lastname = raw_input("Please enter the last name of the entry you want to delete from the phonebook: ")
    print phonebook[lastname]
    ifdel = raw_input("Are you sure you want to delete this entry? y/n ")
    if ifdel.lower() == "y" or ifdel.lower() == "yes":
        del phonebook[lastname]
    elif ifdel.lower == "n" or ifdel.lower == "no":
        return
    print phonebook

# Function to search for entries (return full name and phone)

def search():
    lastname = raw_input("Please enter the last name of the entry you want to find in the phonebook: ")
    print phonebook[lastname.lower()]

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