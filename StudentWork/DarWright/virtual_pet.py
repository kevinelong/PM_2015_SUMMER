# Make a Tamogatchi app
# choose what kind of pet (dog, cat, fish etc) (dog, cat done.
# Things to do: feed, take for walk, give bath, etc (Three basic things done)
# get feedback on how pet is doing: Happiness, health, hunger, etc (three basic stats done)
# one custom exception class (NameTooLong)
# Bonus: write unit test for your animals in a separate file. Be able to "save" game.
# Bonus: Make fun ascii art or add sounds.
#
# TODO add fish sub class
# TODO add more interactions like Pet, brush, goto vet
# TODO work on stats more
# TODO Unit tests
# TODO update save to indicate subclass or update load to change subclass based on self.type
import datetime
import time

class Animal(object):
    """
    Main class for virtual pet.
    """
    def __init__(self):
        self.type = ''
        self.name = ''
        self.health = 5
        self.how_healthy = ''
        self.happiness = 15
        self.how_happy = ''
        self.hunger = 0
        self.how_hungry = ''
        self.age = datetime.datetime.now()

    def set_name(self, name):
        """
        Names the pets, increases happiness
        """
        self.name = name
        self.happiness += 2

    def feed(self):
        """
        Feeds the pet, increases health, happiness, and decreases hunger.
        """
        self.health += 5
        self.happiness += 5
        print 'Feeding pet.',
        self.dot_time_passes(10)
        self.hunger -= 2
        return 'Pet has been feed'

    def walk(self):
        """
        exercise is important, mmmk? increases happiness and hunger.
        """
        self.happiness += 5
        self.hunger += 2
        print 'Walking pet.',
        self.dot_time_passes(30)
        return "Pet has been walked."

    def bath(self):
        """
        Pets should be clean! Increased hunger.
        """
        self.hunger += 1
        print "Bathing pet.",
        self.dot_time_passes(20)
        return "Pet has been bathed."

    def pet_the_pet(self):
        """
        pets like being petted! YAY pet loving!
        """
        self.happiness += 10
        print "Aaaaahhh yea, that's the ticket, {} enjoys the pets".format(self.name)
        self.dot_time_passes(10)
        return "Snuggles are good."

    def time_passed(self):
        """
        As time passes, pet health decreases and hunger increases
        """
        if (datetime.datetime.now() - self.age) > datetime.timedelta(seconds=19):
            self.health -= 2
            self.hunger += 2
        elif (datetime.datetime.now() - self.age) > datetime.timedelta(seconds=9):
            self.health -= 1
            self.hunger += 1

    def check_happy(self):
        """
        Little function to show how happy the pet is.
        """
        happy_list = ['\033[1;32msuper HAPPY', '\033[0;36mHAPPY', '\033[0;31mUNHAPPY']
        if self.happiness >= 50:
            self.how_happy = happy_list[0]
        elif self.happiness < 50 and self.happiness > 10:
            self.how_happy = happy_list[1]
        else:
            self.how_happy = happy_list[2]

    def check_health(self):
        """
        Little function to show how healthy the pet is.
        """
        health_list = ['\033[1;32mexcellent HEALTH', '\033[0;36mfair HEALTH', '\033[0;31mpoor HEALTH']
        if self.health >= 25:
            self.how_healthy = health_list[0]
        elif self.health < 25 and self.health > 10:
            self.how_healthy = health_list[1]
        else:
            self.how_healthy = health_list[2]

    def check_hunger(self):
        """
        Little function to show how hungry the pet is.
        """
        hunger_list = ['\033[1;32mreally HUNGRY', '\033[0;36mHUNGRY', '\033[0;31mnot HUNGRY']
        if self.hunger >= 10:
            self.how_hungry = hunger_list[0]
        elif self.hunger < 10 and self.hunger > 2:
            self.how_hungry = hunger_list[1]
        else:
            self.how_hungry = hunger_list[2]

    def show_checks(self):
        """
        shows the basics stats in a pretty way.
        """
        self.check_happy()
        self.check_health()
        self.check_hunger()
        print "\nYour pet is %s\033[0m, in %s\033[0m, and %s\033[0m" \
              % (self.how_hungry, self.how_healthy, self.how_happy)

    def show_stats(self):
        """
        Little function to show the basic stats. Useful for testing.
        """
        print "\nHealth: %d\n" \
              "Happiness: %d\n" \
              "Hunger: %d\n" % (self.health, self.happiness, self.hunger)

    def dot_time_passes(self, num):
        """
        Useful timer, dot adds and moves across the screen based on number of seconds input
        """
        art = '.'
        for x in range(0, num):
            time.sleep(.5)
            print art,
        self.time_passed()
        self.show_checks()

    def ascii_art(self):
        """
        wanted to have ascii art for the sub class, might put something here later.
        """
        # TODO generic class art?
        pass

    def save_a_pet(self):
        """
        Save your pet! Saves the main stats of the pet in a .vps ( virtual pet save) file.
        """
        choice = raw_input("Do you want to save the pet in a different location? y/n >> ").lower()
        if choice == 'y':
            path = raw_input("Please enter the exact path:\n>> ") + '/'
        else:
            path = ''
        # don't need milliseconds in file name timestamp.
        filename = 'vp_{}_{}.vps'.format(self.name, str(datetime.datetime.now()).replace(' ', '_')[:-7])
        filename = path + filename.replace('/', '').replace(':', '')
        # print filename
        with open(filename, 'a') as save_file:
                save_file.write('{}|{}|{}|{}|{}\n'.format(self.name, self.health,
                                                          self.happiness, self.hunger, self.age))
        print "Pet has been saved with filename: " + filename
        #TODO Add some error handling for file not found, or open etc

    def load_a_pet(self):
        """
        load a pet from a save file
        """
        choice = raw_input("Is the save file in a different location? y/n >>").lower()
        if choice == 'y':
            path = raw_input("Please enter the exact path:\n>> ") + '/'
            filename = raw_input("Please type in the exact, case sensitive filename: \n>>")
            filename = path + filename
        else:
            filename = raw_input("Please type in the exact, case sensitive filename: \n>>")
        # path_list = '/Users/darwright/Python/PM_2015_SUMMER/StudentWork/DarWright/'
        # load_filename = path_list + 'vp_George_2015-06-26_111415.vps'
        # print filename
        with open(filename) as load_pet_file:
            for line in load_pet_file:
                self.name, self.health, self.happiness, self.hunger, self.age = line.split('|')
                self.health = int(self.health)
                self.happiness = int(self.happiness)
                self.hunger = int(self.hunger)
                self.age = self.age[:-1]  # take out the new line command at the end.
                self.age = datetime.datetime.strptime(self.age, "%Y-%m-%d %H:%M:%S.%f")
        #TODO Add some error handling for file not found, or open etc

class Cat(Animal):

    def walk(self):
        """
        cats dislike walking, decreases happiness, increase hunger
        """
        self.happiness -= 5
        self.hunger += 1
        print 'Walking {0}, {0} dislikes walking.\n'.format(self.name)
        self.dot_time_passes(5)
        return "Pet has been walked."

    def ascii_art(self):
        """
        Cute little ascii art of a cat
        """
        # art from http://user.xmission.com/~emailbox/ascii_cats.htm
        print "   ____\n" \
              "   (.  \\\n" \
              "     \  |\n" \
              "      \ |___(\--/)    MEOW!\n" \
              "    __/    (  . . )\n" \
              "   \"'._.    '-.O.'\n" \
              "         '-. \\ \"|\ \n" \
              "           '.,,/'.,,mrf\n\n"


class Dog(Animal):
    def walk(self):
        """
        Dogs love walks, increases happiness and hunger
        """
        self.happiness += 10
        self.hunger += 2
        print 'Walking {0}, {0} really enjoys walking!\n'.format(self.name)
        self.dot_time_passes(30)
        return "Pet has been walked."

    def ascii_art(self):
        """
        Cute little ascii art of a dog
        """
        # Art from http://www.ascii-art.de/ascii/def/dogs.txt
        print "              _=,_\n" \
              "    WOOF! o_/6 /#\\ \n" \
              "           \__ |##/\n" \
              "            ='|--\\ \n" \
              "              /   #'-.\n" \
              "              \#|_   _'-. /\n" \
              "               |/ \_( # |\" \n " \
              "       snd   C/ ,--___/\n\n"


class UI(object):

    def __init__(self):
        """
        Let's get this party started!
        """
        self.menu()

    def menu(self):
        """
        main menu. Make a pet, or quit.
        """
        # TODO load a pet, make a new pet, save a pet, interact with pet
        print "Welcome to the crazy pet house!\n"
        choice = int(raw_input("What would you like to do today?\n"
                               "1. Pick a new pet!\n"
                               "2. Load a pet!\n"
                               "9. Quit\n"
                               ">> "))
        if choice == 1:
            self.pick_a_pet()
        elif choice ==2:
            loader = Animal()
            loader.load_a_pet()
            loader.show_checks()
            self.interact_with_pet(loader)
            #TODO figure out a way to check sub class before importing
        elif choice == 9:
            print "Goodbye! Thanks for playing!"
            exit()

    def get_name(self):
        """
        Sets the name of the pet.
        """
        name = raw_input("What are you going to name your new pet?\n>> ")
        if len(name) > 50:
            raise NameTooLong('{} is to long for a pet name!'.format(name))
        return name

    def pick_a_pet(self):
        """
        And you get a pet, and YOU get a pet, and YOU GET A PET!
        """
        print "Welcome to the pet picker!\n" \
              "Today we have in some cats and some dogs.\n"
        choice = int(raw_input("Enter 1 for cat, 2 for dog. >> "))
        if choice == 1:
            cat = Cat()
            cat.set_name(self.get_name())
            cat.ascii_art()
            print "Awww, what a good name! I'm sure %s will love it!" % cat.name
            self.interact_with_pet(cat)
        elif choice == 2:
            dog = Dog()
            dog.set_name(self.get_name())
            dog.ascii_art()
            print "Awww, what a good name! I'm sure %s will love it!" % dog.name
            self.interact_with_pet(dog)
        else:
            print "Sorry, I didn't get that."
            self.pick_a_pet()

    def interact_with_pet(self, pet):
        """
        Time to play! Walk, bath, feed.
        """
        # walk, bath , feed, show_checks
        print "Let's have some fun with your pet!"
        time.sleep(2)
        pet.ascii_art()
        choice = int(raw_input("What shall we do today?\n"
                               "1. Go for a walk.\n"
                               "2. Take a bath.\n"
                               "3. Eat something!\n"
                               "4. Pet the PET!\n"
                               "5. Save your pet!\n"
                               "9. Quit\n"
                               ">> "))
                                # TODO add save and quit option
        if choice == 1:
            pet.walk()
            time.sleep(5)
            self.interact_with_pet(pet)
        elif choice == 2:
            pet.bath()
            time.sleep(5)
            self.interact_with_pet(pet)
        elif choice == 3:
            pet.feed()
            time.sleep(5)
            self.interact_with_pet(pet)
        elif choice == 4:
            pet.pet_the_pet()
            time.sleep(5)
            self.interact_with_pet(pet)
        elif choice == 5:
            pet.save_a_pet()
        elif choice == 9:
            print "Goodbye! Thanks for playing!"
            exit()


class NameTooLong(Exception):
    """
    An exception where the name is longer than 50 characters.
    """


ui = UI()


