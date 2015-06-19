class NerfGun(object):
    """
    A toy gun that shoots pieces of foam with suction cups on the end
    """
    BULLET_COLORS = ('red', 'yellow', 'blue', 'green')
    can_load_mult_colors = False

    def __init__(self, bullet_color=None, autoload=True):
        self.total_available_bullets = 5
        # auto-load bullets on initialization
        self.bullets_loaded = 0
        if autoload:
            self.bullets_loaded = self.total_available_bullets

        # if bullet_color is given, set it to that, otherwise default to yellow
        self.bullet_color = bullet_color or 'yellow'

    def shoot(self):
        if self.bullets_loaded <= 0:
            raise NerfException('No bullets loaded')

        self.bullets_loaded -= 1

    def reload(self, bullet_color=None):
        # TODO: Consider bullet color when loading
        self.bullets_loaded = self.total_available_bullets

    def is_fully_loaded(self):
        return self.bullets_loaded == self.total_available_bullets

    def get_bullet_color(self):
        """
        Get the color of the bullets that are currently loaded
        """
        # TODO: implement this

    def is_loaded_bullets_same_color(self):
        """
        Boolean returns True if all the currently loaded bullets are the same
        color, otherwise False
        """
        # TODO: Implement this
        if not self.can_load_mult_colors:
            # if it can only load one color, then they must all be one color
            return True


class NerfException(Exception):
    """
    Nerf related exception
    """


def test_initial_bullets():
    nerfgun_autoloaded = NerfGun()
    assert(nerfgun_autoloaded.bullets_loaded == nerfgun_autoloaded.total_available_bullets)

    nerfgun_unloaded = NerfGun(autoload=False)
    assert(nerfgun_unloaded.bullets_loaded == 0)


def test_shoot():
    nerfgun = NerfGun()
    assert(nerfgun.bullets_loaded == 5)

    nerfgun.shoot()
    assert(nerfgun.bullets_loaded == 4)
    nerfgun.shoot()
    assert(nerfgun.bullets_loaded == 3)
    nerfgun.shoot()
    assert(nerfgun.bullets_loaded == 2)
    nerfgun.shoot()
    assert(nerfgun.bullets_loaded == 1)
    nerfgun.shoot()
    assert(nerfgun.bullets_loaded == 0)

    try:
        # cannot shoot an empty gun
        nerfgun.shoot()
    except NerfException:
        # this is what we expected
        pass
    else:
        raise AssertionError('Shooting should have failed')
