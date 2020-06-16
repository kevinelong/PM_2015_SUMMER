__author__ = 'stephen'


"""
I'm trying to open the test file saved earlier.
"""

import cPickle as pickle

pickle_file ='/home/stephen/Desktop/pickle_project_sk/GurkinTesting'


def get_from_file(obj):
	with open('/home/stephen/Desktop/pickle_project_sk/GurkinTesting/new_pickle.txt')  as pfile:
		loaded_obj = pickle.load(pfile)