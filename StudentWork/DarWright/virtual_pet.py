# Make a Tamogatchi app
# choose what kind of pet (dog, cat, fish etc)
# Things to do: feed, take for walk, give bath, etc
# get feedback on how pet is doing: Happiness, health, hunger, etc
# one custom exception class
# Bonus: write unit test for your animals in a separate file. Be able to "save" game.
# Bonus: Make fun ascii art of add sounds.
#
import datetime
import time

class Animal(object):
    def __init__(self):
        self.type = ''
        self.health = 5
        self.how_healthy = ''
        self.happiness = 30
        self.how_happy = ''
        self.hunger = 0
        self.how_hungry = ''
        self.age = datetime.datetime.now()

    def feed(self):
        self.health += 5
        self.happiness += 5
        print 'Feeding pet.',
        self.dot_time_passes(10)
        self.hunger -= 2
        return 'Pet has been feed'

    def walk(self):
        self.happiness += 5
        self.hunger += 2
        print 'Walking pet.',
        self.dot_time_passes(30)
        return "Pet has been walked."

    def bath(self):
        self.hunger += 1
        print "Bathing pet.",
        self.dot_time_passes(20)
        return "Pet has been bathed."

    def time_passed(self):
        if (datetime.datetime.now() - self.age) > datetime.timedelta(seconds=19):
            self.health -= 2
            self.hunger += 2
        elif (datetime.datetime.now() - self.age) > datetime.timedelta(seconds=9):
            self.health -= 1
            self.hunger += 1

    def check_happy(self):
        happy_list = ['\033[1;32msuper HAPPY', '\033[0;36mHAPPY', '\033[0;31mUNHAPPY']
        if self.happiness >= 50:
            self.how_happy = happy_list[0]
        elif self.happiness < 50 and self.happiness > 10:
            self.how_happy = happy_list[1]
        else:
            self.how_happy = happy_list[2]

    def check_health(self):
        health_list = ['\033[1;32mexcellent HEALTH', '\033[0;36mfair HEALTH', '\033[0;31mpoor HEALTH']
        if self.health >= 25:
            self.how_healthy = health_list[0]
        elif self.health < 25 and self.health > 10:
            self.how_healthy = health_list[1]
        else:
            self.how_healthy = health_list[2]

    def check_hunger(self):
        hunger_list = ['\033[1;32mreally HUNGRY', '\033[0;36mHUNGRY', '\033[0;31mnot HUNGRY']
        if self.hunger >= 10:
            self.how_hungry = hunger_list[0]
        elif self.hunger < 9 and self.health > 0:
            self.how_hungry = hunger_list[1]
        else:
            self.how_hungry = hunger_list[2]

    def show_checks(self):
        self.check_happy()
        self.check_health()
        self.check_hunger()
        print "\nYour pet is %s\033[0m, in %s\033[0m, and %s\033[0m" % (self.how_hungry, self.how_healthy, self.how_happy)

    def show_stats(self):
        print "\nHealth: %d\n" \
              "Happiness: %d\n" \
              "Hunger: %d\n" % (self.health, self.happiness, self.hunger)

    def dot_time_passes(self, num):
        art = '.'
        for x in range(0, num):
            time.sleep(.5)
            print art,
        self.time_passed()
        self.show_checks()

class Cat(Animal):

    def walk(self):
        self.happiness -= 5
        self.hunger = 0
        print 'Walking pet, pet dislikes walking.\n'
        self.dot_time_passes(1)
        return "Pet has been walked."

class Dog(Animal):
    def walk(self):
        self.happiness += 10
        self.hunger += 2
        print 'Walking pet, pet really enjoys walking!\n'
        self.dot_time_passes(30)
        return "Pet has been walked."


# animal = Animal()
# animal.show_stats()
# animal.bath()
# animal.show_stats()
# animal.feed()
# animal.show_stats()
# animal.walk()
# animal.show_stats()

cat = Cat()
cat.show_stats()
# cat.bath()
cat.show_stats()
cat.walk()
# cat.show_stats()
# cat.walk()
# cat.show_stats()

# dog = Dog()
# dog.show_stats()
# # dog.walk()
# # dog.show_stats()
# dog.show_checks()