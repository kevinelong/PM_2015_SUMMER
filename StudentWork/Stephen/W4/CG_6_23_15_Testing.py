__author__ = 'stephen'

with open('/home/stephen/Documents/newTest/class_is_fun.txt', 'wr') as my_file:
    my_file.write('class is fun\n')


with open('/home/stephen/Documents/newTest/class_is_fun.txt', 'r') as my_newfile:
    for line in my_newfile:
       for letter in line:
           print letter