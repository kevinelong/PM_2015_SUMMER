from parkour_game_concept import catalog
import random
import types


# Allows user to choose level
user_level = raw_input("Beginner (B) | Intermediate (I) | Advanced (A)\n"
                       "*****  What is your level?  ******\n"
                       ">>  ").lower()

# assigns number value to user_level
if user_level == "beginner":
    user_level = 1
elif user_level == "intermediate":
    user_level = 2
elif user_level == "advanced":
    user_level = 3

# stores list of moves from chosen level
level_moves_list = []

# store list of move names from level_moves_list
level_moves_names = []

# store list of move types from level_moves_list
level_moves_types = []

# loops through catalog to find moves based off user_level
for move in catalog.itervalues():
    if move['level'] == user_level:
        level_moves_list.append(move)

for move_option in level_moves_list:
    level_moves_names.append(move_option['name'])

for move_option in level_moves_list:
    level_moves_types.append(move_option['move_type'])


print ', '.join(level_moves_names)


# takes in users obstacles
user_input = raw_input("Create a list of obstacles.\n"
                        "AKA:Vault, Rail, Platform, Jump, Wall\n"
                       ">>  ").lower()


# takes user_input obstacles and adds items to a new list
user_obstacle_list = []

user_obstacle_list.append(user_input)


# run generated from user_obstacle_list
generated_run = []

# grabs items based off user_obstacle_list and assigns each item a random move
for obstacle in user_obstacle_list:
    if obstacle == "rail":
        generated_run.append("{} the {}".format(random.choice(level_moves_names), obstacle))
    elif obstacle == "vault":
        generated_run.append("{} the {}".format(random.choice(level_moves_names), obstacle))
    elif obstacle == "jump":
        generated_run.append("{} the {}".format(random.choice(level_moves_names), obstacle))
    elif obstacle == "wall":
        generated_run.append("{} the {}".format(random.choice(level_moves_names), obstacle))

print level_moves_list
print level_moves_names
print level_moves_types
# print ', '.join(generated_run)





