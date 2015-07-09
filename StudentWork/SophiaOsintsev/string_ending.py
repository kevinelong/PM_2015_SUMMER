# Check if a string (first argument) ends with the given target string (second argument).

def string_end(string1, string2):
    length = len(string2)
    snip = string1[-length:]
    print snip
    if snip == string2:
        return True
    else:
        return False

print string_end("Sebastian", "ian")