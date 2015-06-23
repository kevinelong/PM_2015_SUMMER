from person_maker import Person, Dog


def test_person():
    reina = Person()
    assert(reina.name == 'Reina')
    assert(reina.birth_date == 'Feb 4')


def test_dog():
    fido = Dog()
    assert(fido.tails == 1)
    assert(fido.ears == 2)


test_person()
test_dog()
