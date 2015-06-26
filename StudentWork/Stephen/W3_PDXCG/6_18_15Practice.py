__author__ = 'Stephen'

import time
class Bike_Light(object):




    def __init__(self):
        self.state = 0

    def toggle_switch(self):
        self.state =(self.state +1) % 4

    def auto_off(self):
        pass
        #take user_time = raw_input(x time.seconds) -= time.time

    def is_on(self):
        return  self.state != 0

    def get_blink1(self):
        self.state = 1
        print "BLINK"
        time.sleep(4)
        print "BLINK"

    # def get_blink2(self):
    #     print "BLINK"
    #     time.sleep(3)
    #     print "BLINK"
    #
    # def get_blink3(self):
    #     print "BLINK"
    #     time.sleep(2)
    #     print "BLINK"

bikelight = Bike_Light()

while True:
    user_choice = raw_input("Press 1 to turn your light on, press 0 to turn light off.  ")
    # ADD TIMERS FOR LIGHT TO TURN OFF AFTER A GIVEN TIME
    #
    if user_choice == "1":
            bikelight.toggle_switch()
            print bikelight.state
    elif user_choice == "0":
        bikelight.state = 0
        break

#def test_init():
 #   bikelight = Bike_Light()
  #  assert(bikelight.state == 0)

#def test_toggle_switch():
 #   bikelight