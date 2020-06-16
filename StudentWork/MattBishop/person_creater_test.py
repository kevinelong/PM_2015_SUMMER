from person_creater import Person

def test_person():
        matt = Person('Matt', 32, "5'10", 200)
        assert matt.name == 'Matt'
        assert matt.age == 32
        assert matt.height == "5'10"
        assert matt.weight == 200

test_person()
