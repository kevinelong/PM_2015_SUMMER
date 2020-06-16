
string = raw_input("Please enter a string to flip the capitalization on: ")

reverse(string)

def reverse(input):
    global reverse_string
    reverse_string = input[::-1]
    return reverse_string

output = ""
for letter in reverse_string:
    if ord(letter) >= 97 and ord(letter) <= 122:
        output = output + chr(ord(letter) - 32)
    elif ord(letter) >= 65 and ord(letter) <= 90:
        output = output + chr(ord(letter) + 32)
    else:
        output = output + letter

print output