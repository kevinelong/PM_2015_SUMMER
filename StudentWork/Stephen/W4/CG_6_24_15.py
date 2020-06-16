
__author__ = 'stephen'


# def get_something():
#     something = raw_input('Type something here >>  ')
#     return int(something)
# try:
#     something = get_something()
# except ValueError:
#     print 'You just got served by me, the computer, silly human.\n You should have known that would happen.'
#
# except Exception:
#     print "Did you mean:  bla bla bla\n you should have entered a number"


try:
    print stephen
except NameError as err:
    print 'There is a problem and it is: {}'.format(err)

else:
    print 'else'
finally:
    print 'finally'


def do_something(anything):
    if anything == 0
        raise  ValueError('I wanted to give you something other than a 0')
    return  True

if __name__ == 'main':
    anything = raw_input('give me a thing:  ')