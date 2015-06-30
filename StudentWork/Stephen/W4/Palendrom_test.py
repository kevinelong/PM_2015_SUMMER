__author__ = 'stephen'


word_test = 'hannah'

def palendrom_test(word_string):
    reversed_word = []
    for x in word_string:
        reversed_word.insert(0,x)
        reversed_string  = ''.join(reversed_word)
        print x

    return reversed_string

def check_strings(word1, word2):
    if word1 == word2:
        return True
    else:
        return False


reversed_string = palendrom_test(word_test)

print check_strings(word_test, reversed_string)



# palendrom_test(word_string)