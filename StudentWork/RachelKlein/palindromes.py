def is_palindrome(string):
    word = string.lower()
    word_backwards = word[::-1]
    if word == word_backwards:
        return True
    else:
        return False


def is_also_palindrome(string):
    word = string.lower()
    word_backwards = ''
    for x in reversed(word):
        word_backwards += x
    if word == word_backwards:
        return True
    else:
        return False


assert is_palindrome("Hannah") is True
assert is_palindrome("Paul") is False

assert is_also_palindrome("Hannah") is True
assert is_also_palindrome("Paul") is False
