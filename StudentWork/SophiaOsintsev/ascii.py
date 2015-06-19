#turn letters into numbers
def ascii(letters):
    output = []
    for c in letters:
        output.append(ord(c))
    return output
#turn numbers into letters
def characters(numbers):
    output = ""
    for n in numbers:
        output += chr(n)
    return output

#add commas
def characters_two(numbers):
    output = []
    for n in numbers:
        output.append(chr(n))
    return ", ".join(output)

numbers = ascii("SopHia OsinTsev")
original = characters(numbers)
with_commas = characters_two(numbers)

print numbers
print original
print with_commas
