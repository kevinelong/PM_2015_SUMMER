#Work in progress not working yet

# Create a dictionary of dictionaries to hold your data.
phonebook = {
    'anderson': {'name': 'Paul Anderson', 'phone': '503.799.0556'},
    'personman': {'name': 'Guy Personman', 'phone': '555.555.5555'},
    'duderson': {'name': 'Dude Duderson', 'phone': '555.666.7777'},
}


def add():
    first_name = raw_input("Enter your name: ")
    last_name = raw_input("Enter last name: ")
    phone = raw_input("Enter your phone: ")
    phonebook[surname]

def change():
    phonebook["name"][0] = raw_input("Name: ")
    phonebook["phone"][0] = raw_input("Phone: ")
    return


def delete(d, key):
    r = dict(d)
    del r[key]
    return r


def search():
    if name in phonebook:
    # Send a message if it's a valid user
        phonebook.users[user].send(socket.message)
    else:
    # Do nothing if it isn't
        pass


while True:
    choice = raw_input("press 1 to search, 2 to add....")
    if choice == '1':
        search()
    elif choice == '2':
        add()
    elif choice == '3':
        change()
    else:
        delete()