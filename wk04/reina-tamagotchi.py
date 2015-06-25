import random
import time


class Animal(object):

    nap_length = 5
    sleepiness_limit = 5
    hunger_warning_limit = 5
    hunger_death_limit = 7
    age_limit = 10

    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.sleepiness = 0
        self.excitement = 3
        self.age = 0
        print '{} is so excited to go home with you!'.format(self.name)

    def feed(self):
        if self.hunger < 3:
            print '{} isn\'t hungry right now'.format(self.name)
        else:
            print 'Yum! {} ate their food!'.format(self.name)
            self.hunger -= 1
            self.sleepiness += 2
            self.excitement -= 1
        self.deal_with_needs()

    def pet(self):
        if self.hunger > 3:
            print '{} is too hungry to play'.format(self.name)
        else:
            print '{} is having so much fun being petted!'.format(self.name)
            self.hunger += 1
            self.sleepiness += 2
            self.excitement += 1
        self.deal_with_needs()

    def print_status(self):
        print (
            '{}\'s hunger is {}, sleepiness is {}, and excitement '
            'is {}'.format(
                self.name, self.hunger, self.sleepiness, self.excitement)
        )

    def deal_with_needs(self):
        if self.sleepiness > self.sleepiness_limit:
            print '{} fell asleep'.format(self.name)
            time.sleep(self.nap_length)
            self.sleepiness = 0
        if self.hunger > self.hunger_warning_limit:
            print '{} needs to eat or will die of hunger!'.format(self.name)

        # deal with death situations
        if self.hunger > self.hunger_death_limit:
            raise DeathException('{} died of hunger'.format(self.name))
        elif self.age > self.age_limit + random.randint(-2, 2):
            raise DeathException(
                '{} lived a happy life and died of old age'.format(self.name))
        elif not random.randrange(100):
            # 1 in 100 chance the animal will just die
            raise DeathException('{} died randomly'.format(self.name))

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.name)


class Dog(Animal):

    nap_length = 3
    sleepiness_limit = 10
    hunger_warning_limit = 4
    hunger_death_limit = 7
    age_limit = 12

    def give_bath(self):
        pass


class Cat(Animal):

    nap_length = 10
    sleepiness_limit = 4
    hunger_warning_limit = 6
    hunger_death_limit = 8
    age_limit = 20

    def play_with_laser_pen(self):
        pass


class TamagotchiException(Exception):
    """
    Base exception class
    """


class DeathException(TamagotchiException):
    """
    Exception raised when an animal dies
    """


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
