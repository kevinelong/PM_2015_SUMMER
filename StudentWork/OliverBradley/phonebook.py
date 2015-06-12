__author__ = 'Oliver'

# Create a dictionary of dictionaries to hold your data.
phonebook = {
    'jones': {'name': 'Chris Jones', 'phone': '503-277-9710'},
    'dover': {'name': 'Chelsea Dover', 'phone': '503-511-9981'},
    'bradley': {'name': 'Oliver Bradley', 'phone': '503-333-0475'}
}


def add():
    # Function for adding entries
    pass


def change():
    # Function to change entries
    pass


def delete():
    # Function to delete entries
    pass


def search():
    # Function to search for entries
    pass


while True:
    choice = raw_input("press 1 to search, 2 to add....")
    if choice == '1':
        search()
    elif choice == '2':
        add()
    # The rest of the menu code here