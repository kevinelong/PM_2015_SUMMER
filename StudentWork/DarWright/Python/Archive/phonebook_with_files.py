# new phone book with name and phone number
# given name, get the number
# given the number, give the name

class PhoneBook(object):
    def __init__(self):
        self.file_name = '/Users/darwright/Python/phonebook.txt'
        self.ui()

    def get_name_number(self):
        name = raw_input("Please enter the name to add: ")
        name = name.capitalize()
        ph_number = raw_input("Please enter the phone number like XXX-XXX-XXXX: ")
        with open(self.file_name, 'a') as name_ph_num_file:
            name_ph_num_file.write('{},{}\n'.format(name, ph_number))
        self.ui()

    def find_number(self, namein):
        with open(self.file_name, 'r') as name_ph_num_file:
            for line in name_ph_num_file:
                name, ph_num = line.split(',')
                if namein == name:
                    print 'The phone number of {} is {}'.format(name, ph_num)
                    raw_input("Press Enter to continue:")
        self.ui()

    def find_name(self, numberin):
        with open(self.file_name, 'r') as name_ph_num_file:
            for line in name_ph_num_file:
                # the line[:-1] takes the \n off the imported line
                name, ph_num = line[:-1].split(',')
                if numberin == ph_num:
                    print 'The name associated with the phone number of {} is {}'.format(ph_num, name)
                    raw_input("Press Enter to continue:")
        self.ui()

    def ui(self):
        choice = int(raw_input("Welcome to the phone book!\n"
                               "Press 1 to enter a new name and number.\n"
                               "Press 2 to search for an entry by name\n"
                               "Press 3 to search for an entry by number\n"
                               "Press 4 to quit.\n"
                               ">>>"))

        if choice == 1:
            self.get_name_number()
        elif choice == 2:
            name = raw_input('Please enter a name to search for: ')
            name = name.capitalize()
            self.find_number(name)
        elif choice == 3:
            number = raw_input('Enter the number to search for (like XXX-XXX-XXXX): ')
            self.find_name(number)
        else:
            print "Goodbye!"
            exit()


pb = PhoneBook()

