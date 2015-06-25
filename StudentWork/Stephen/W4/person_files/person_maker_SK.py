__author__ = 'stephen'


class Person(object):
    def __init__(self):
        self.age = 30
        self.name ="Jessica"
        self.height = int(5)

person = Person()

if True:
    person.age == 30
    print "you are the same age as Jessica"