# return true if the given string is a palindrome. Otherwise, return false.

# string == string

# string1 = 'Hello'
some_word_is = 'eye'


def turns_strings_backwards(string_in):
    backwards_string = string_in[::-1]  # reverse the string
    return backwards_string  # returned the reversed string

def check_strings(aword, awnotherword):
    """
    compare the orignal string with the reversed string
    return True if they are the same, forwards and backwards
    return False if not
    """
    if aword == awnotherword:
        return True
    else:
        return False


backwards_string = turns_strings_backwards(some_word_is)
print check_strings(some_word_is, backwards_string)