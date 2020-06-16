__author__ = 'stephen'
# Challenge: Tamagotchi app (virtual pets!)
# User can choose which kind of pet they want (dog, cat, fish, etc)
# They can have choices of what to do with their pet (feed, take on a walk, pet, give bath, etc)
# They will then get feedback on how their pet is doing (happiness, health, hunger, etc)
# Use at least one custom written exception class (ie TamagatchiException or TamagatchiHungerException)
# Bonuses: Write unit tests for your animals in a separate file. Be able to 'save game'. Make some fun ascii art for your pets, or add sounds!

import time

class Animals(object):

    def __init__(self):
        self.name = name
        self.hunger = 3
        self.sleepy = 5
        self.restless = 3
        self.dirty = 0
        self.hour = 0
        self.min = 0



    def clean_up_after(self):
        self.dirty -= 9

    def feed(self):
        self.hunger -= 8

    def play(self):
        self.sleepy += 3
        self.restless -= 2
        self.dirty += 3
        self.hunger += 4

    class Parrot(Animals):
        def feed(self):
            pass


    class Dog(Animals):
        def take_for_walk(self):
            pass


    class Cat(Animals):
        def play_with(self):
            pass
        def pet(self):
            pass


def greeting():
    print 'Welcome to The Pet Shop'

while True:
    choice = raw_input(
    \t\t\t 'Would you like a pet'
    )













# def user_pet():
#     pet_choice = raw_input('You are at the pet store, there is a parrot, gerble, rabbit , snake, cat, dog,\nwhat animal would your child like:   ')
#
#
#
# while True:




#
# class Animal(object):
#     def take_for_walk(self):
#         pass
#
#     def feed(self):
#
#     class Dog(Animal):
#
#         def take_for_walk(self):
#             super(Dog, self).take_for_walk()
#             pass
#
#         def take_bath(self):
#             pass
#
#     class Cat(Animal):
#
#         def take_for_walk(self):
#             pass