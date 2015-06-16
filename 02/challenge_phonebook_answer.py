# RECREATE THE PHONEBOOK APP AS A PHONEBOOK CLASS AND ALSO REPLACE THE ENTRIES WITH INSTANCES OF A NEW PHONEENTRY CLASS
# Write test code at the bottom of the file. No User input/interaction is required.
class PhoneEntry():
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name() + " " + self.phone_number


class PhoneBook():
    def __init__(self):
        self.phone_book_list = {}
        max_id = 1

    def addEntry(self, entry):
        self.phone_book_list[self.max_id] = entry
        self.max_id += 1

    def __str__(self):
        output = ""
        for entry in self.phone_book_list:
            output += str(entry) + "\n"
        return output


phone_book = PhoneBook()

# add using named parameters
entry1 = PhoneEntry(first_name="Kevin", last_name="Long", phone_number="555-1111")
phone_book.addEntry(entry1)

# add using ordered parameters
entry2 = PhoneEntry("Bob", "Smith", "555-2222")
phone_book.addEntry(entry2)

print(phone_book)