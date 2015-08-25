# My method to reverse caps and test
def test_reverse_caps():
    assert(sOphIA == reverse_caps())

def reverse_caps():
    string = "SoPHia"
    name = string.swapcase()
    return name
print reverse_caps()