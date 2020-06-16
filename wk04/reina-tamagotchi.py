import random
import sys
import time

import asciiart


def activity(fn):
    """
    Decorator for any methods that represent an activity of daily living for an
    animal

    Deals with any needs including death and sleepiness
    """
    def deal_with_needs(animal, *args, **kwargs):

        return_val = fn(animal, *args, **kwargs)

        animal.age += 1
        animal.sleepiness += 1
        animal.hunger += 1

        if animal.sleepiness > animal.sleepiness_limit:
            print '{} fell asleep'.format(animal.name)
            time.sleep(animal.nap_length)
            animal.sleepiness = 0
            animal.excitement = 0
        if animal.hunger > animal.hunger_warning_limit:
            print '{} needs to eat or will die of hunger!'.format(animal.name)
        if animal.excitement < animal.excitement_warning_limit:
            print '{} needs your attention'.format(animal.name)

        # deal with death situations
        if animal.hunger > animal.hunger_death_limit:
            raise DeathException('{} died of hunger'.format(animal.name))
        elif animal.age > animal.age_limit + random.randint(-2, 2):
            raise DeathException(
                '{} lived a happy life and died of old age'.format(animal.name))
        elif not random.randrange(100):
            # 1 in 100 chance the animal will just die
            raise DeathException('{} died randomly'.format(animal.name))
        elif animal.excitement < animal.excitement_runaway_limit:
            raise RunAwayException('{} ran away'.format(animal.name))

        return return_val

    return deal_with_needs


class Animal(object):

    nap_length = 5
    sleepiness_limit = 5
    hunger_warning_limit = 5
    hunger_death_limit = 7
    age_limit = 10
    excitement_limit = 3

    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.sleepiness = 0
        self.excitement = 3
        self.age = 0
        print '{} is so excited to go home with you!'.format(self.name)

    @activity
    def feed(self):
        if self.hunger < 3:
            print '{} isn\'t hungry right now'.format(self.name)
        else:
            print 'Yum! {} ate the food all up!'.format(self.name)
            self.hunger -= 2

    @activity
    def pet(self):
        if self.hunger > 3:
            print '{} is too hungry to play'.format(self.name)
        else:
            print '{} is having so much fun being petted!'.format(self.name)
            self.sleepiness += 2
            self.excitement += 1

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.name)

    def get_choices(self):
        return ['pet', 'feed']



class Dog(Animal):

    nap_length = 3
    sleepiness_limit = 10
    hunger_warning_limit = 4
    hunger_death_limit = 7
    age_limit = 12

    @activity
    def give_bath(self):
        pass

    def get_choices(self):
        parent_choices = super(self.__class__, self).get_choices()
        dog_choices = ['give_bath']
        return parent_choices + dog_choices


class Cat(Animal):

    nap_length = 10
    sleepiness_limit = 4
    hunger_warning_limit = 6
    hunger_death_limit = 8
    age_limit = 20

    @activity
    def play_with_laser_pen(self):
        if self.hunger > self.hunger_limit:
            print '{} is too hungry to play'.format(self.name)
        else:
            self.excitement += 2
            self.sleepiness += 1

    def get_choices(self):
        parent_choices = super(self.__class__, self).get_choices()
        cat_choices = ['play_with_laser_pen']
        return parent_choices + cat_choices


class TamagotchiException(Exception):
    """
    Base exception class
    """


class DeathException(TamagotchiException):
    """
    Exception raised when an animal dies
    """


class RunAwayException(TamagotchiException):
    """
    Exception raised when an animal runs away because it is too bored with you
    """


def list_to_comma(mylist, conjunction='and'):
    """
    Given a list of strings, return a comma separated list of those strings
    """
    len_mylist = len(mylist)
    if len_mylist == 0:
        return ''
    elif len_mylist == 1:
        return mylist[0]
    elif len_mylist == 2:
        return mylist[0] + ' ' + conjunction + ' ' + mylist[1]
    else:
        return ', '.join(mylist[:-1]) + ', ' + conjunction + ' ' + mylist[-1]


if __name__ == '__main__':
    pet_type = raw_input(
        'Welcome to the pet store! What type of animal would '
        'you like?  '
    ).title()
    name = raw_input('What is your new pet\'s name?  ').title()

    # create the pet object
    try:
        pet = globals().pop(pet_type)(name)
    except KeyError:
        pet = Animal(name)

    while True:
        avail_choices = pet.get_choices()
        avail_choices_str = list_to_comma(avail_choices, conjunction='or')
        choice = raw_input(
            '\nWhat would you like to do with {}?  '
            '{}\n'.format(name, avail_choices_str))

        try:
            getattr(pet, choice)()
        except AttributeError:
            print '{} is not an available choice'.format(choice)
        except DeathException as err:
            print asciiart.death
            print err
            sys.exit(0)
        except RunAwayException as err:
            print ascciart.run_away
            print err
            sys.exit(0)
