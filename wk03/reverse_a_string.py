def reverse_a_string(word):
    new_word = ''
    for letter in word:
        new_word = letter + new_word
    return new_word

def test_reverse_a_string():
    assert(reverse_a_string('Reina') == 'anieR')
    assert(reverse_a_string('r e i n a') == 'a n i e r')

def swap_a_case(word):
    new_word = ''
    for letter in word:
        if is_it_upper(letter):
            new_word += letter.lower()
        else:
            new_word += letter.upper()
    return new_word

def test_swap_a_case():
    assert(swap_a_case('ReInA') == 'rEiNa')

def is_it_upper(letter):
    return letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

test_reverse_a_string()
test_swap_a_case()
