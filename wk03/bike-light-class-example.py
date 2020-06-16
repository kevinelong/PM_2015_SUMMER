import time
import os

import testingtools.colors as colors


def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')


class BikeLight(object):

    def __init__(self):
        self.state = 0

    def toggle_switch(self):
        """
        Value will be 0, 1, 2, or 3

        (0 + 1) % 4 = 1
        (1 + 1) % 4 = 2
        (2 + 1) % 4 = 3
        (3 + 1) % 4 = 0
        """
        self.state = (self.state + 1) % 4

    def get_state_display(self):
        """
        Get the human readable display name for the current state of the bike
        light
        """
        if self.state == 0:
            return 'Off'
        elif self.state == 1:
            return 'Solid On'
        elif self.state == 2:
            return 'Flashing On'
        elif self.state == 3:
            return 'Night Rider On'

    def is_on(self):
        return self.state != 0

    def get_light_output(self):
        return getattr(self, 'get_{}_output'.format(self.state))()

    def draw_light(self):
        pass

    def get_0_output(self):
        return ("     ",)

    def get_1_output(self):
        return ("*****",)

    def get_2_output(self):
        return ("*****", "     ")

    def get_3_output(self):
        return (
            colors.RED + "*    ",
            " *   ",
            "  *  ",
            "   * ",
            "    *",
            "   * ",
            "  *  ",
            " *   " + colors.COLOR_OFF,
        )


def test_init():
    bikelight = BikeLight()
    assert(bikelight.state == 0)

def test_toggle_switch():
    bikelight = BikeLight()
    assert(bikelight.state == 0)

    bikelight.toggle_switch()
    assert(bikelight.state == 1)

    bikelight.toggle_switch()
    assert(bikelight.state == 2)

    bikelight.toggle_switch()
    assert(bikelight.state == 3)

    bikelight.toggle_switch()
    assert(bikelight.state == 0)


test_init()
test_toggle_switch()


bikelight = BikeLight()
while True:
    entry = raw_input('\nPush 1 to click the switch, 2 to see the light  ')
    if entry != '1' and entry != '2':
        # they did something wrong, so ask again
        print '{} is not a recognized entry'.format(entry)
        continue

    if entry == '1':
        bikelight.toggle_switch()
        print 'The bike is currently set to state {}'.format(
            bikelight.get_state_display())
    elif entry == '2':
        while True:
            try:
                for out in bikelight.get_light_output():
                    print out
                    time.sleep(0.1)
                    clear_term()
            except KeyboardInterrupt:
                break
