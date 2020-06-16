import datetime

from virtual_pet.virtual_pet import Animal

test = Animal()
test.type = 'save'
test.name = 'George'
test.health = 10
test.how_healthy = '\033[1;32mexcellent HEALTH'
test.happiness = 20
test.how_happy = '\033[1;32msuper HAPPY'
test.hunger = 5
test.how_hungry = '\033[1;32mreally HUNGRY'
test.age = datetime.datetime.now()

# don't need milliseconds in file name datestamp.
filename = 'vp_{}_{}.vps'.format(test.name, str(datetime.datetime.now()).replace(' ', '_')[:-7])
filename = filename.replace('/', '').replace(':', '')
# print filename
# with open(filename, 'a') as save_file:
#         save_file.write('{}|{}|{}|{}|{}\n'.format(test.name, test.health, test.happiness, test.hunger, test.age))

# loads a file and sets the stats, then runs the checks
path_list = '/Users/darwright/Python/PM_2015_SUMMER/StudentWork/DarWright/'
load_filename = path_list + 'vp_George_2015-06-26_111415.vps'
# print load_filename
with open(load_filename) as load_pet_file:
    for line in load_pet_file:
        test.name, test.health, test.happiness, test.hunger, test.age = line.split('|')
    # print test.name, test.health, test.happiness, test.hunger, test.age
test.show_checks()

# test.age = test.age[:-1]
# print test.age
# print datetime.datetime.strptime(test.age, "%Y-%m-%d %H:%M:%S.%f")
