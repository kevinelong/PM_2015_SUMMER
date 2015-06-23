# To facilitate a discussion on using dictionaries vs classes to represent the
# attributes on an object


# Using a class
class Person(object):
    def __init__(self, name=None, age=None, height=None):
        self.name = name
        self.age = age
        self.height = height  # in inches

    def __repr__(self):
        return 'Person: {}'.format(self.name if self.name else 'Nada')

person = Person(name='Reina', age=33, height=64)
print "\033[93m person:  ",  person, "\033[0m"


# Using a dictionary
person = {'name': 'Reina', 'age': 33, 'height': 64}
print "\033[93m person:  ",  person, "\033[0m"


# Sample usage
def grow_taller(person, growth):
    if isinstance(person, object):
        # if person is a class
        person.height += growth
    elif isinstance(person, dict):
        # if person is a dictionary
        person['height'] += growth

    return person


reina = Person(name='Reina')
dar = Person(name='Dar')
stephen = Person(name='Stephen')

our_class = [reina, dar, stephen]
