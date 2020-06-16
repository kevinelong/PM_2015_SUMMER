__author__ = 'stephen'

"""
This is a pickle testing file.
I'm trying to save a file using the pickle module in python.
"""

import cPickle as pickle

pickle_file ='/home/stephen/Desktop/pickle_project_sk/GurkinTesting'

def write_to_file(obj):
	with open('/home/stephen/Desktop/pickle_project_sk/GurkinTesting/new_pickle.txt', 'w') as pfile:
		pickle.dump(obj, pfile)