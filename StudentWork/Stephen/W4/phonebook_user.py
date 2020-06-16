__author__ = 'stephen'

user_phonebook1 = {'name':'name','phone':'phone'}

def user_phonebook():
    name = raw_input('What is your first name:  ')
    phone = raw_input('What is your phone number:  ')
    user_phonebook1[name.lower()] = {"name":"name", "phone":"phone"}

with open('/home/stephen/Documents/newTest/user_phonebook.txt', 'wr') as my_file:
    my_file.write('Write your name and phone number here')
        for


with open('/home/stephen/Documents/newTest/user_phonebook.txt', 'r') as my_newfile:
    for line in my_newfile:
       for letter in line:

    print user_phonebook1





user_phonebook()