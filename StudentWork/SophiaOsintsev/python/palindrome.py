#Return true if the given string is a palindrome. Otherwise, return false.

def palindrome(string):
    punct = """.,?'":;!()"""
    output = []
#lowercase a string
    string = string.lower().replace(" ","")
#remove white space
    # string = string.replace(" ","")
#remove punctuation
    for letter in string:
        if letter not in punct:
            output.append(letter)
#compare
    for item in output:
        if item == output[-1]:
            output.pop()
        else:
            return False
    return True

input = raw_input("Enter a string!")

print palindrome(input)



