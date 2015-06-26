# UNIT Tests for virtual_pet.py
from virtual_pet import Animal, Cat, Dog, UI
import datetime
import time

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
test_create_animal()

def test_set_name():
    test = Animal()
    test.set_name('Garfield')
    assert(test.name == 'Garfield')
test_set_name()

def test_feed():  # base stats 5 health, 15 happiness, 0 hunger
    test = Animal()
    test.feed()  # health + 5, happy + 5, hunger -2
    assert(test.health == 10)
    assert(test.happiness == 20)
    assert(test.hunger == -2)
test_feed()

def test_walk():  # base stats 5 health, 15 happiness, 0 hunger
    test = Animal()
    test.walk()  # happy + 5, hungry + 2
    assert(test.health == 4)  # time passes - 1 health
    assert(test.happiness == 20)
    assert(test.hunger == 3)  # time passes + 1 to hunger
test_walk()

def test_bath():  # base stats 5 health, 15 happiness, 0 hunger
    test = Animal()
    test.bath()  # hunger + 1
    assert(test.health == 4)  # time passes -2 health
    assert(test.happiness == 15)
    assert(test.hunger == 2)  # time passes + 2 to hunger
test_bath()

def test_pet_the_pet():
    test = Animal()
    test.pet_the_pet()  # happiness + 10
    assert(test.health == 5)
    assert(test.happiness == 25)
    assert(test.hunger == 0)
test_pet_the_pet()

def pet_the_pet(self):
        """
        pets like being petted! YAY pet loving!
        """
        self.happiness += 10
        print "Aaaaahhh yea, that's the ticket, {} enjoys the pets".format(self.name)
        self.dot_time_passes(10)
        return "Snuggles are good."

def test_time_passed_20_seconds():
    test = Animal()
    time.sleep(20)
    test.time_passed()
    assert(test.health == 3)
    assert(test.hunger == 2)
test_time_passed_20_seconds()

def test_time_passed_10_seconds():
    test = Animal()
    time.sleep(10)
    test.time_passed()
    assert(test.health == 4)
    assert(test.hunger == 1)
test_time_passed_10_seconds()

def test_check_happy():
    test = Animal()
    test.happiness = 50
    test.check_happy()
    assert(test.how_happy == '\033[1;32msuper HAPPY')
    test.happiness = 49
    test.check_happy()
    assert(test.how_happy == '\033[0;36mHAPPY')
    test.happiness = 11
    test.check_happy()
    assert(test.how_happy == '\033[0;36mHAPPY')
    test.happiness = 10
    test.check_happy()
    assert(test.how_happy == '\033[0;31mUNHAPPY')
    test.happiness = 9
    test.check_happy()
    assert(test.how_happy == '\033[0;31mUNHAPPY')
test_check_happy()

def test_check_healthy():
    test = Animal()
    test.health = 25
    test.check_health()
    assert(test.how_healthy == '\033[1;32mexcellent HEALTH')
    test.health = 24
    test.check_health()
    assert(test.how_healthy == '\033[0;36mfair HEALTH')
    test.health = 11
    test.check_health()
    assert(test.how_healthy == '\033[0;36mfair HEALTH')
    test.health = 10
    test.check_health()
    assert(test.how_healthy == '\033[0;31mpoor HEALTH')
    test.health = 9
    test.check_health()
    assert(test.how_healthy == '\033[0;31mpoor HEALTH')
test_check_healthy()

def test_check_hunger():
    test = Animal()
    test.hunger = 10
    test.check_hunger()
    assert(test.how_hungry == '\033[1;32mreally HUNGRY')
    test.hunger = 9
    test.check_hunger()
    assert(test.how_hungry == '\033[0;36mHUNGRY')
    test.hunger = 3
    test.check_hunger()
    assert(test.how_hungry == '\033[0;36mHUNGRY')
    test.hunger = 0
    test.check_hunger()
    assert(test.how_hungry == '\033[0;31mnot HUNGRY')
    test.hunger = -1
    test.check_hunger()
    assert(test.how_hungry == '\033[0;31mnot HUNGRY')
test_check_hunger()

# UNIT test for Cat Class
def test_cat_walk():  # base stats 5 health, 15 happiness, 0 hunger
    test = Cat()
    test.walk()  # happy - 5, hungry + 1
    assert(test.health == 5)
    assert(test.happiness == 10)
    assert(test.hunger == 1)
test_cat_walk()

# UNIT Test for Dog class
def test_dog_walk():  # base stats 5 health, 15 happiness, 0 hunger
    test = Dog()
    test.walk()  # happy + 10, hungry + 2
    assert(test.health == 4)  # time passes - 1 health
    assert(test.happiness == 25)
    assert(test.hunger == 3)  # time passes + 1 to hunger
test_dog_walk()