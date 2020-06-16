def get_something():
    something = raw_input('Give me something >> ')
    try:
        return int(something)
    except ValueError:
        return get_something()


try:
    print 'reina'
except NameError as err:
    print 'There was a problem and it was: {}'.format(err)
else:
    print 'else'
finally:
    print 'finally'


def do_something(athing):
    if athing == '0':
        raise ReinaError('I wanted something other than a 0')
    return True


class ReinaError(Exception):
    """
    When something goes wrong with Reina
    """


if __name__ == '__main__':
    athing = raw_input('Give me a thing >>  ')
    do_something(athing)
