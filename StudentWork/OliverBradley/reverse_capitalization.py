def test_reverse_caps():
    assert(reverse_caps('SoMeThInG') == 'sOmEtHiNg')

test_reverse_caps()

def reverse_caps(input):
    return input.swapcase()

string = raw_input("Please enter a string to flip the capitalization on: ")

print reverse_caps(string)


