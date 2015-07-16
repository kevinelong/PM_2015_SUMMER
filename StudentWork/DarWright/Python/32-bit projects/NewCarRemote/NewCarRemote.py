"""
This program requires pygame, and only works with a 32-bit version of python.
"""

import pygame
import time


class CarRemote(object):
    def __init__(self):
        """
        Program a car remote to lock, unlock, open trunk and honk the horn.
        state 0 = lock
        state 1 = unlock
        state 2 = open trunk
        state 3 = honk horn
        :return:
        """
        self.state = 0
        self.carnoise = ''
        #disable self.ui() for unit tests.
        self.ui()

    def set_car_lock_on(self):
        self.state = 0

    def set_car_lock_off(self):
        self.state = 1

    def set_trunk_open(self):
        self.state = 2

    def set_horn_honk(self):
        self.state = 3

    def cartart(self):
        # carart url: http://www.retrojunkie.com/asciiart/vehicles/cars.htm
        carart = "            .      ..\n" \
                 "    __..---/______//-----.        ((  )\n" \
                 " .\".--.```|    - /.--.  =:    ( VROOM! ))\n" \
                 "(.: {} :__L______: {} :__; __--( __- -_= )\n" \
                 "   *--*           *--*                     jnh\n"
        print carart


    def menu(self):
        menu = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" \
               ">>>>>>>>>>>>>>>>>Car Remote Menu<<<<<<<<<<<<<<<<\n" \
               "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" \
               "               1 ==> UNLOCK DOORS\n" \
               "               2 ==> LOCK DOORS\n" \
               "               3 ==> POP TRUNK\n" \
               "               4 ==> HONK HORN\n" \
               "               5 ==> QUIT\n"
        print menu
        choice = int(raw_input("            Enter choice: "))
        return choice

    def play_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.carnoise)
        pygame.mixer.music.play()
        time.sleep(5)

    def state_message(self):
        state_message = ''
        if self.state == 0:
            state_message = "*CLICK CLICK* Car is now LOCKED!"
            self.carnoise = 'beep-beep.wav'
        elif self.state == 1:
            state_message = "*CLICK CLICK* Car is now UNLOCKED"
            self.carnoise = 'Power_Door_Lock.wav'
        elif self.state == 2:
            state_message = "*CLICK POP* Trunk is OPEN!"
            self.carnoise = 'trunk.wav'
        elif self.state == 3:
            state_message = "aaaaahhhhhhOOOOOOOOOOOOOOOOOOOOOOOgggggaaaaaa!!!!!"
            self.carnoise = 'the-mask-horn.wav'
        return state_message

    def ui(self):
        self.cartart()
        while True:
            choice = self.menu()
            if choice == 1:
                self.set_car_lock_on()
                print self.state_message()
                self.play_sound()
            elif choice == 2:
                self.set_car_lock_off()
                print self.state_message()
                self.play_sound()
            elif choice == 3:
                self.set_trunk_open()
                print self.state_message()
                self.play_sound()
            elif choice == 4:
                self.set_horn_honk()
                print self.state_message()
                self.play_sound()
            elif choice == 5:
                self.cartart()
                self.carnoise = 'travels.wav'
                self.play_sound()
                print "~~~~~~~~~~~~~~~~Happy travels!~~~~~~~~~~~~~~~~~"
                exit()
            else:
                print "Not a valid choice."


carremote = CarRemote()

# UNIT TESTS
# def test_set_car_lock_on():
#     carremote = CarRemote()
#     carremote.set_car_lock_on()
#     assert(carremote.state == 0)
#
# def test_set_car_lock_off():
#     carremote = CarRemote()
#     carremote.set_car_lock_off()
#     assert(carremote.state == 1)
#
# def test_set_trunk_open():
#     carremote = CarRemote()
#     carremote.set_trunk_open()
#     assert(carremote.state == 2)
#
# def test_set_Horn_honk():
#     carremote = CarRemote()
#     carremote.set_horn_honk()
#     assert (carremote.state == 3)
#
# def test_state_message():
#     carremote = CarRemote()
#     carremote.set_car_lock_on()
#     print carremote.state_message()
#     carremote.set_car_lock_off()
#     print carremote.state_message()
#     carremote.set_trunk_open()
#     print carremote.state_message()
#     carremote.set_horn_honk()
#     print carremote.state_message()
#
# test_set_car_lock_on()
# test_set_car_lock_off()
# test_set_trunk_open()
# test_set_Horn_honk()
# test_state_message()







