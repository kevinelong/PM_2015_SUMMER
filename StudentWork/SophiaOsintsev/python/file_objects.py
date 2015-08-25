# with open('/Users/sophiaosintsev/Desktop/add-new-contacts.txt', 'wr') as my_file:
#     my_file.write('Adding new contacts to phonebook')


# add a name and phone numer to the file above
# given name search for the number

my_file = '/Users/sophiaosintsev/Desktop/add-new-contacts.txt'

choice = int(raw_input('Do you want to search for a contact (1) or add a contact (2)?  '))

if choice == 2:
    name = raw_input('What is the name of the contact you want to add? >> ')
    phone = raw_input('What is the contacts phone number? >> ')
    with open(my_file, 'a') as contact_file:
        contact_file.write('{},{}\n'.format(name, phone))

elif choice == 1:
    search_contact = raw_input('What is the name of the contact you want to find? >> ')
    with open(my_file) as contact_file:
        for contact in contact_file:
            name, phone = contact.split(',')
            if search_contact == name:
                print 'Here is the contact information you are looking for - {} : {}'.format(name, phone)
