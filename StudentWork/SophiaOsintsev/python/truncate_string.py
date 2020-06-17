# Truncate a string (first argument) if it is longer than the given maximum string length (second argument).
# Return the truncated string with a '...' ending.

def truncate(string, num):
# Take a length of a string and store in variable
    length = len(string)
# Compare len to num
    # if len is <= num return string
    if length <= num:
        return string
    else:
        return string[:num] + "..."
    # else return truncated string

sentence = raw_input("Please enter a sentence >>> ")
num = int(raw_input("Please enter a number >>> "))

print truncate(sentence, num)