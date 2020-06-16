"""
A simple module that gives some objects that might make up a phone book

Possible solution to phonebook challenge
"""


class PhoneBook(object):
    """
    A phone book
    """

    def __init__(self):
        self.entries = set()

    def add_person(self, person):
        self.entries.add(person)

    def remove_person(self, person):
        self.entries.remove(person)

    def get_person_by_last_name(self, last_name):
        for entry in self.entries:
            if entry.last_name == last_name:
                return entry
        raise EntryNotFound(
            'Ooops! Someone with last name "{}" is not in '
            'the phone book yet!'.format(last_name)
        )

    def get_person_by_first_name(self, first_name):
        for entry in self.entries:
            if entry.first_name == first_name:
                return entry
        raise EntryNotFound(
            'Ooops! Someone with first name "{}" is not in '
            'the phone book yet!'.format(first_name)
        )



class Person(object):
    """
    The person who will be an entry in the phone book
    """

    def __init__(self, first=None, last=None, number=None):
        self.first_name = first
        self.last_name = last
        self.phone_number = number


class EntryNotFound(Exception):
    """
    Just a regular old exception
    """
