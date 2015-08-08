phonebook_file = '/home/jay/Desktop/phone_book_dict.txt'


choice = int(raw_input('Select [1] to add a contact\n'
                       'Select [2] to remove a contact\n'))

if choice == 1:
    f_name = raw_input("First name?")
    l_name =  raw_input("Last name?")
    num = raw_input("Enter number")

    with open(phonebook_file, 'a') as phone_book_dict:
         phone_book_dict.write('{},{},{}\n'.format(f_name, l_name, num))

elif choice == 2:
    del_contact = raw_input("Input the last name of the contact you'd like to remove.\n")
    f = open(phonebook_file, 'r')
    lines = f.readlines()
    f.close()
    f = open(phonebook_file, 'w')
    for line in lines:
        if line!=del_contact + "\n":
            f.write(line)
    f.close()