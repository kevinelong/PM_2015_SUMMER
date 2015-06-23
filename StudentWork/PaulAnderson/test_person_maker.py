from StudentWork.PaulAnderson.person_maker import Person

def test_person():
    ace = Person()
    assert(ace.legs == 2)
    assert(ace.arms == 2)
    assert(ace.nose == 1)

test_person()