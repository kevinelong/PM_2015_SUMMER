# UNIT Tests for virtual_pet.py
from virtual_pet import Animal, Cat, Dog, UI
import datetime

# class animal tests

def test_create_animal():
    test = Animal()
    assert(test.type == '')
    assert(test.name == '')
    assert(test.health == 5)
    assert(test.how_healthy == '')
    assert(test.happiness == 15)
    assert(test.how_happy == '')
    assert(test.hunger == 0)
    assert(test.how_hungry == '')
    assert(isinstance(test.age, datetime.datetime))
# test_create_animal()

def test_set_name():
    test = Animal()
    test.set_name('Garfield')
    assert(test.name == 'Garfield')
# test_set_name()

def test_feed():
    test = Animal()
    test.feed()
    assert(test.health == 10)
    assert(test.happiness == 20)
    assert(test.hunger == -2)
# test_feed()

def test_walk():
    test = Animal()
    test.walk()
    assert(test.health == 5)
    assert(test.happiness == 20)
    assert(test.hunger == 2)
# test_walk()

def test_bath():
    test = Animal()
    test.bath()
    assert(test.health == 5)
    assert(test.happiness == 15)
    assert(test.hunger == 1)
test_bath()