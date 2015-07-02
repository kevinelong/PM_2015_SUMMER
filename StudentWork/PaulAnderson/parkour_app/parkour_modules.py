__author__ = 'Paul Anderson'
__copyright__ = "Copyright 2015"
__version__ = "1.0"
__email__ = "andermation@gmail.com"
__status__ = "Production"

from parkour_run_db import runs
import webbrowser


class ParkourMove(object):
    def __init__(self, name, level, move_type, take_off):
        self.name = name
        self.level = level
        self.move_type = move_type
        self.take_off = take_off


#main menu for game
def main_menu():
    user_choice = int(raw_input("""Welcome to the run generator for Parkour and Free Running.\n
                            To start a run, type '1.\n
                            What exactly is the difference between Parkour and Free Running? type 2 to get learned!\n"""))

    if user_choice == 1:
        make_run()
    elif user_choice == 2:
        webbrowser.open('http://iontams.com/2012/03/13/parkour-vs-free-running/')
        make_run()


def make_run():
    user_name = raw_input("Enter a user name:  ")
    user_level = raw_input("Beginner (B) | Intermediate (I) | Advanced (A)\n"
                           "*****  What is your level?  ******\n"
                           ">>  ").lower()

    return user_name, user_level



# gets move name based on move type from users chosen level
def get_level_moves_types(level_moves_list, move_type):
    level_move_types = []
    for level_move in level_moves_list:
        if level_move["move_type"] == move_type:
            level_move_types.append(level_move)

    return level_move_types

# saves users run to db
def save_run():
    user_save = raw_input("Would you like to save this run?  Yes or NO:  ").lower()
    if user_save == "yes" or "y":
        runs[user_name] = {'level': user_level, 'obstacles': user_obsticles_list, 'run': generated_run, 'location': []}
        print "{}'s run data has been stored.".format(user_name)
    else:
        main_menu()







