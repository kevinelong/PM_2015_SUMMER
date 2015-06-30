__author__ = 'Paul Anderson'
__copyright__ = "Copyright 2015"
__version__ = "1.0"
__email__ = "andermation@gmail.com"
__status__ = "Production"

from parkour_db import catalog
import random


# Parkour run maker - an app to randomly generate runs based off chosen obstacles.

# Dictionary of Parkour moves


created_run = []

class ParkourMove(object):
    def __init__(self, name, level, move_type, take_off):
        self.name = name
        self.level = level
        self.move_type = move_type
        self.take_off = take_off



# print move["dash_vault"]["move_type"]
# for key in move:
# random_list = move[move.keys()[int(random.random()*len(move.keys()))]]
# random_list = move[move.keys()[int(random.random())]]
# random_list = random_list['level']
# for move in catalog.itervalues():
#     if move['level'] == 1:
#         print move




