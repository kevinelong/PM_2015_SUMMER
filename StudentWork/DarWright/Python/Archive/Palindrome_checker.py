# return true if the given string is a palindrome. Otherwise, return false.

def turns_strings_backwards(string_in):
    # backwards_string = string_in[::-1]  # reverse the string

    # another way of reversing the string
    backwards_list = []
    for x in string_in:
        backwards_list.insert(0, x)
        backwards_string = ''.join(backwards_list)  # put the list back into a string
    return backwards_string  # returned the reversed string

def check_strings(aword, anotherword):
    """
    compare the original string with the reversed string
    return True if they are the same, forwards and backwards
    return False if not
    """
    if aword == anotherword:
        return True
    else:
        return False

def gimmie_a_word():
    print "Welcome to the palindrome checker!"
    check_word = raw_input("Give me a word to check:\n>> ")
    check_word = check_word.lower()  # this takes the string and makes it all lower case
    if ' ' in check_word:  # this looks for the character of a space to make sure its just a word
        print "Please only enter one word."
        gimmie_a_word()
    # check the word now!
    checker = check_strings(check_word, turns_strings_backwards(check_word))
    if checker == True:
        print "{} is a palindrome!".format(check_word)
    elif checker == False:
        print "{} is not a palindrome. :( Bummer.".format(check_word)

gimmie_a_word()