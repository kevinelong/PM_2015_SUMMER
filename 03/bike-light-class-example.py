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

    def is_on(self):
        return self.state != 0


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
