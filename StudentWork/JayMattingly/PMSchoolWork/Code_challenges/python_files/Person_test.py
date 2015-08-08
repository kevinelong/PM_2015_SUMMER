from StudentWork.JayMattingly.PMSchoolWork import Person_maker

def test_person():
    jay = Person_maker()
    assert(jay.age == 10)

test_person()
