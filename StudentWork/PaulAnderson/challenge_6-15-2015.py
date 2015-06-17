
# def to_reverse():
#     my_string = 'This is my string'
#     reversed = my_string[::-1]
#     print reversed
#
# to_reverse()

##### String reversal function #####
# def to_reverse(my_input):
#     reversed = []
#     for letter in my_input:
#         reversed.insert(0, letter)
#     return ''.join(reversed)
#
# to_reverse('reverse this')

##### quick version to swap upper and lower case letters #####
# def uncapitalize():
#     to_swap = "This Is SomEThing To SwAp!".swapcase()
#     print to_swap
#
# uncapitalize()


##### reverse a string #####
def reverse_input(input):
    flip_me = ''
    for letter in input:
        flip_me = letter + flip_me
    print flip_me

reverse_input("Flip this string!")

##### reverse a string version 2 #####
# def reverse_input(input):
#     global reverse
#     reverse = []
#     for letter in input:
#         reverse.insert(0, letter)
#     new_string = ''.join(reverse)
#     print new_string
#     return new_string

# string = raw_input("Please enter a string to flip the capitalization on: ")
#
#
#
# output = ""
# for letter in reverse:
#     if ord(letter) >= 97 and ord(letter) <= 122:
#         output = output + chr(ord(letter) - 32)
#     elif ord(letter) >= 65 and ord(letter) <= 90:
#         output = output + chr(ord(letter) + 32)
#     else:
#         output = output + letter
#
# print output

# def test_reverse_string():
#     assert(reverse_input("Petes Dragon") == "nogarD seteP")
#
# test_reverse_string()
# reverse_input(string)

#
# def reverse_test():
#     assert(to_reverse('Flip this') == 'siht pilF')
#
# def cap_test():
#     assert(uncapitalize("TeSt") == "TeSt")



