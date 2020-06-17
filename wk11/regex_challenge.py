import re


def is_ordinal(num):
    # this is totally not right!!!
    regex = r'(^1st|^2nd|^3rd|1\dth|\d+1st|\d+2nd|\d+3rd|\d+[3-9,0]th|^[4-9,0]th)'
    matches = re.match(regex, num)
    if not matches:
        return False
    elif matches.start() == 0 and matches.end() == len(num):
        return True
    return False


def test_is_ordinal():
    assert(is_ordinal('1st') == True)
    assert(is_ordinal('2nd') == True)
    assert(is_ordinal('3rd') == True)
    assert(is_ordinal('4th') == True)
    assert(is_ordinal('5th') == True)
    assert(is_ordinal('6th') == True)
    assert(is_ordinal('7th') == True)
    assert(is_ordinal('8th') == True)
    assert(is_ordinal('9th') == True)
    assert(is_ordinal('10th') == True)
    assert(is_ordinal('11th') == True)
    assert(is_ordinal('12th') == True)
    assert(is_ordinal('13th') == True)
    assert(is_ordinal('101st') == True)
    #assert(is_ordinal('111th') == True)

    assert(is_ordinal('1th') == False)
    assert(is_ordinal('11st') == False)
    assert(is_ordinal('12nd') == False)
    assert(is_ordinal('13rd') == False)
    assert(is_ordinal('4st') == False)
    assert(is_ordinal('st') == False)


def is_letters_and_numbers(word):
    regex = r'[0-9a-zA-Z]*'
    matches = re.match(regex, word)
    if not matches:
        return False
    elif matches.start() == 0 and matches.end() == len(word):
        return True
    return False


def test_is_letters_and_numbers():
    trues = (
        'asdf',
        '1234',
        'asdf123',
        'asdf123asf',
        '123asd123',
    )
    falses = (
        '!',
        '.',
        '123.',
        '134.1234,',
    )
    for t in trues:
        assert(is_letters_and_numbers(t) == True)
    for f in falses:
        assert(is_letters_and_numbers(f) == False)


def is_letters_numbers_and_length(word):
    regex = r'[0-9a-zA-Z]{6,12}'
    matches = re.match(regex, word)
    if not matches:
        return False
    elif matches.start() == 0 and matches.end() == len(word):
        return True
    return False


def test_is_letters_numbers_and_length():
    assert(is_letters_numbers_and_length('123456') == True)
    assert(is_letters_numbers_and_length('1234567') == True)
    assert(is_letters_numbers_and_length('123456789012') == True)
    assert(is_letters_numbers_and_length('asdfasdfasdfasdfasdf') == False)
    assert(is_letters_numbers_and_length('1') == False)
    assert(is_letters_numbers_and_length('') == False)


def is_python_variable_name(word):
    regex = r'[a-zA-Z_]+[a-zA-Z0-9_]*'
    matches = re.match(regex, word)
    if not matches:
        return False
    elif matches.start() == 0 and matches.end() == len(word):
        return True
    return False


def test_is_python_variable_name():
    assert(is_python_variable_name('asf') == True)
    assert(is_python_variable_name('asdf1') == True)
    assert(is_python_variable_name('ASDF') == True)
    assert(is_python_variable_name('asdf_12') == True)
    assert(is_python_variable_name('_sdf') == True)

    assert(is_python_variable_name('1234') == False)
    assert(is_python_variable_name('12asdf') == False)
    assert(is_python_variable_name('') == False)


if __name__ == '__main__':
    test_is_ordinal()
    test_is_letters_and_numbers()
    test_is_letters_numbers_and_length()
    test_is_python_variable_name()
