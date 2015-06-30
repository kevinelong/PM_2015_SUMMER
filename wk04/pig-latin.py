import subprocess


def to_pig_latin(word):
    """
    Given a string, return it translated into pig latin.

    For words that begin with consonant sounds, the initial consonant or
    consonant cluster is moved to the end of the word, and "yay" is added.

    For words which begin with vowel sounds or silent letter, one just adds
    "yay" to the end.

    https://en.wikipedia.org/wiki/Pig_Latin

    Raises ValueError if the string is not only letters (ie has spaces or
    digits)
    """
    if not word.isalpha():
        raise ValueError('Word must be only letters, no numbers or spaces')

    word = word.lower()  # lower case for consistency

    if is_consonant(word[0]):  # the word starts with a consonant
        # get all the consonants at the beginning of the word
        starting_consonants = get_starting_consonants(word)
        # remove them from the front
        word = word.lstrip(starting_consonants)
        # put them at the end
        word += starting_consonants
        # add "ay" to the end
        word += 'ay'
    else:  # the word starts with a vowel
        # add "yay" to the end
        word += 'yay'
    return word


def get_starting_consonants(word):
    starting_consonants = ''
    for letter in word:
        if is_consonant(letter):
            starting_consonants += letter
        else:
            break
    return starting_consonants


def is_consonant(letter):
    """
    Boolean if a letter is a consonant or not.

    Raises ValueError if the string is not a letter or is not one character
    long.
    """
    if not letter.isalpha():
        raise ValueError('String must be a letter')
    elif not len(letter) == 1:
        raise ValueError('String must be a single character')
    return letter in 'bcdfghjklmnpqrstvwxyz'


def say_word(word):
    cmd = 'say "{}"'.format(word)
    status = subprocess.call(cmd, shell=True)
    return status


def test_to_pig_latin():
    assert to_pig_latin('reina') == 'einaray'
    assert to_pig_latin('eggs') == 'eggsyay'
    assert to_pig_latin('string') == 'ingstray'
    assert to_pig_latin('a') == 'ayay'
    assert to_pig_latin('j') == 'jay'


if __name__ == '__main__':
    test_to_pig_latin()
    while True:
        word = raw_input('\nEnter a word to translate:\n>>> ')

        try:
            pigged = to_pig_latin(word)
        except ValueError as err:
            print err
            continue

        print pigged
        say_word(pigged)
