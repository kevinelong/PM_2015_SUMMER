# Reverse a string and test
def test_reverse_string():
    assert(['Sophia', 'is', 'name', 'My'] == reverse_string())

def reverse_string():
    string = "My name is Sophia"
    words = string.split(" ")
    words.reverse()
    return words
print reverse_string()