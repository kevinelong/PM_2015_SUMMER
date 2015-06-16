def reverse_a_string(word):
    new_word = ''
    for letter in word:
        new_word = letter + new_word
    return new_word

def test_reverse_a_string():
    assert(reverse_a_string('Reina') == 'anieR')
    assert(reverse_a_string('r e i n a') == 'a n i e r')

test_reverse_a_string()
