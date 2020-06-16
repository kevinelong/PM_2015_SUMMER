__author__ = 'stephen'
__author__ = "stephen"
# This is my contact list.


phonebook = {
    "king": {"fname":"Stephen", "lname":"King", "phone":"111-111-1111", "email":"dsiwi@wioenw.org"},
    "cottrell": {"fname": "James", "lname":"Cottrell", "phone":"222-222-2222", "email":"iwien@weoin.org"}
}


def search():
    lname = ""
    try:
        lname = raw_input("Please enter the last name of the person you wish to look up.: ")
        print ""
        print phonebook[lname.lower()]["fname","lname"]
        print phonebook[lname.lower()]["phone"]
        print phonebook[lname.lower()]["email"]
        print ""
    except:
        print "That name does not show up in your contacts"


def add():
    fname = raw_input("Please enter the first name of your new Contact you are adding: ")
    lname = raw_input("Enter the last name of your new Contact: ")
    phone = raw_input("Enter the phone number of your new Contact here: ")
    email = raw_input("Enter the email of your new Contact:  ")
    phonebook[lname.lower()] = {"name": fname + "" + lname, "phone": phone, "email": email}
    print "Thank you. %s %s has been added" % (fname, lname)


def delete():
    lname = raw_input("Enter the name of the Contact that you would like to remove.:  ")
    if lname.lower() in phonebook.keys():
        delete_choice = raw_input("Do you really want to remove %s?:" % phonebook[lname.lower()]["name"])
        if delete_choice.lower() == "y" or delete_choice.lower() == "yes":
            deleted_name = phonebook[lname.lname.lower()]["name"]
            del phonebook[lname.lname.lower()]

            print "The contact %s, has been deleted." % deleted_name
        else:
            print "The deletion has been Aborted"
    else:
        print "That person is not listed in your contacts.\n Did you miss-type the name of the person you want to find?"


def update():
    person_update = raw_input("What is the last name of the contact would you like to update?:  ")
    if person_update in phonebook.keys():
        fname = raw_input("Please enter the first name of the contact that you would like to update.:  ")
        lname = raw_input("Please enter the last name of the contact that you would like to update.:   ")
        phone = raw_input("Please enter the phone number of the contact that you would like to update.:   ")
        email = raw_input("Please enter the email of the contact that you would like to update.:   ")
        del phonebook[lname.lower()]
        phonebook[lname.lower()] = {"name": fname + "" + lname, "phone": phone, "email": email}
        print "You have updated the contact information for %s." % (fname, lname)


while True:
    choice = raw_input(
        "\t\t\t  Your Tiny Phone book 	\n 1 = search for a contact	\n 2 = add a contact \n 3 = delete an contact \n 4 = update a contacts info \n 5 = exit  ")
    if choice == "1":
        search()
    elif choice == "2":
        add()
    elif choice == "3":
        delete()
    elif choice == "4":
        update()
    elif choice == "5":
        exit()
    else:
        print "'%s' is not a valid choice. Please try again." % choice
