# Sample module for saving data to files to be loaded later. Fulfills the use
# case where a user may want to "save their game" for continuing later.
# Replaces the need for a simple database.
#
# -----
# Use:
#
# Given a "Cat" object:
#
#   class Cat(object):
#       def __init__(self, name):
#           self.name = name
#           self.age = 1
#           self.happiness = 5
#
#   my_cat = Cat('Pamina')
#
#
# It could be saved thus:
#
#   my_cat_dict = {
#       'type': 'Cat',
#       'name': my_cat.name,
#       'age': my_cat.age,
#       'happiness': my_cat.happiness,
#   }
#   write_to_file(my_cat_dict)
#
#
# And loaded thus:
#
#   my_cat_dict = get_from_file()
#   my_cat = Cat(my_cat_dict['name'])
#   my_cat.age = my_cat_dict['age']
#   my_cat.happiness = my_cat_dict['happiness']



import cPickle as pickle


pickle_file = '/Users/purple4reina/Desktop/pickle-test'


def write_to_file(obj):
    """
    An example function of how to save information to a file.

    `pickle_file`: The path to the file where the information will be stored.
        The user must have read/write permissions on the file. It does not need
        to have already existed before calling this function.

    `obj`: The stuff that will be stored, see
        https://docs.python.org/2.7/library/pickle.html#what-can-be-pickled-and-unpickled
        for what types of objects this can be.
    """
    with open(pickle_file, 'w') as pfile:
        pickle.dump(obj, pfile)


def get_from_file():
    """
    An example function of how to get saved information out of a file.

    `pickle_file`: the path to the file where the information was stored

    `loaded_obj`: the stuff that was saved in the file that is now loaded
    """
    with open(pickle_file) as pfile:
        loaded_obj = pickle.load(pfile)
    return loaded_obj
