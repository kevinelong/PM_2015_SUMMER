#Return the provided string with the first letter of each word capitalized

def capcase(string):
# Turn sting into list
    list = string.split()
# Check to see if first letter is capital
    output = []
    for word in list:
        # if word[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        output.append(word.capitalize())
        # else:
        #     output.append(word)
    return " ".join(output)
# If its not capitalize it.
# Put list into string

print capcase('a man went Walking')