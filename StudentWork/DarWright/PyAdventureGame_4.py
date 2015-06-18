# imports
import random

# global variables
ISMONSTER = False
MONSTERNAME = ''
DOORCHOICE = ''
HERO = ''
MONSTER = ''

# classes


class Room:
    def __init__(self):
        global MONSTERNAME
        global ISMONSTER
        global MONSTER
        findmonster()
        self.desc = ''
        self.n_door = self.dooropen()
        self.s_door = self.dooropen()
        self.e_door = self.dooropen()
        self.w_door = self.dooropen()
        if self.n_door is False and self.s_door is False and self.e_door is False and self.w_door is False:
            self.n_door = True
            self.doorstatement()
        else:
            self.doorstatement()
        if ISMONSTER is True:
            MONSTERNAME = namemonster()
            MONSTER = Things(MONSTERNAME)

    # list with the four directions
    direction = ['North', 'South', 'East', 'West']

    # list of different room descriptions
    description = ['The %s wall is covered in moss.',
                   'The %s wall is covered in slime.',
                   'The %s wall is made of brick.',
                   'The %s wall is solid stone.',
                   'The %s wall has crumbled.',
                   'The %s wall is normal looking.',
                   'The %s wall, its just a forrest.',
                   'The %s wall looks like it is dense fog.',
                   'The %s wall is made of old hard cheese.',
                   'The %s wall is a decaying dragon, and no you cant loot him.'
                   ]

    # load the 4 directions
    def north(self):
        rnd = rnd09()
        self.desc = self.description[rnd] % self.direction[0]
        return self.desc

    def south(self):
        rnd = rnd09()
        self.desc = self.description[rnd] % self.direction[1]
        return self.desc

    def east(self):
        rnd = rnd09()
        self.desc = self.description[rnd] % self.direction[2]
        return self.desc

    def west(self):
        rnd = rnd09()
        self.desc = self.description[rnd] % self.direction[3]
        return self.desc

    # generate the door open messages
    def doorstatement(self):
        global DOORCHOICE
        if self.n_door is True and self.s_door is True and self.e_door is True and self.w_door is True:
            ds = "There are open doors to the North, South, East and West."
            DOORCHOICE = "You can go North, South, East or West: "
        elif self.n_door is False and self.s_door is True and self.e_door is True and self.w_door is True:
            ds = "There are open doors to the South, East and West."
            DOORCHOICE = "You can go South, East or West: "
        elif self.n_door is False and self.s_door is False and self.e_door is True and self.w_door is True:
            ds = "There are open doors to the East and West."
            DOORCHOICE = "You can go East or West: "
        elif self.n_door is False and self.s_door is False and self.e_door is False and self.w_door is True:
            ds = "There is an open door to the West."
            DOORCHOICE = "You can go West: "
        elif self.n_door is True and self.s_door is False and self.e_door is False and self.w_door is True:
            ds = "There are open doors to the North and West."
            DOORCHOICE = "You can go North or West: "
        elif self.n_door is True and self.s_door is True and self.e_door is False and self.w_door is True:
            ds = "There are open doors to the North, South and West."
            DOORCHOICE = "You can go North, South or West: "
        elif self.n_door is True and self.s_door is True and self.e_door is True and self.w_door is False:
            ds = "There are open doors to the North, South, and East."
            DOORCHOICE = "You can go North, South or East: "
        elif self.n_door is True and self.s_door is True and self.e_door is False and self.w_door is False:
            ds = "There are open doors to the North and South."
            DOORCHOICE = "You can go North or South: "
        elif self.n_door is False and self.s_door is False and self.e_door is True and self.w_door is False:
            ds = "There is an open door to the East."
            DOORCHOICE = "You can go East: "
        elif self.n_door is False and self.s_door is True and self.e_door is False and self.w_door is False:
            ds = "There is an open door to the South."
            DOORCHOICE = "You can go South: "
        elif self.n_door is True and self.s_door is False and self.e_door is False and self.w_door is False:
            ds = "There is an open door to the North."
            DOORCHOICE = "You can go North: "
        elif self.n_door is True and self.s_door is True and self.e_door is False and self.w_door is True:
            ds = "There are open doors to the North, South and West."
            DOORCHOICE = "You can go North, South or West: "
        elif self.n_door is False and self.s_door is True and self.e_door is False and self.w_door is True:
            ds = "There are open doors to the South and West."
            DOORCHOICE = "You can go South or West: "
        elif self.n_door is True and self.s_door is False and self.e_door is True and self.w_door is True:
            ds = "There are open doors to the North, East and West."
            DOORCHOICE = "You can go North, East or West: "
        elif self.n_door is False and self.s_door is True and self.e_door is True and self.w_door is False:
            ds = "There are open doors to the South and East."
            DOORCHOICE = "You can go South or East: "
        elif self.n_door is True and self.s_door is False and self.e_door is True and self.w_door is False:
            ds = "There are open doors to the North and West."
            DOORCHOICE = "You can go North or West: "
        return ds

    # function to see if the door is open or not for each wall
    def dooropen(self):
        if random.randint(1, 101) < 50:
            do = True
        else:
            do = False
        return do

    # moving through a door statements
    def doormove(self, dchoice):
        if dchoice == "north" or dchoice == "n":
            direction = "North"
        elif dchoice == "south" or dchoice == "s":
            direction = "South"
        elif dchoice == "east" or dchoice == "e":
            direction = "East"
        elif dchoice == "west" or dchoice == "w":
            direction = "West"
        path = "   You walk through the door in the %s wall.\n\n" % direction
        return path


class Things():
    def __init__(self, name):
        self.hp = 50 + random.randint(5, 50)
        self.name = name
        self.ap = 5 + random.randint(3, 10)
        self.w = 0
        self.a = 0


# functions


def greeting():
    print "Welcome to the tiny adventure game!\n"


def getname():
    global HERO
    name = raw_input("Please enter the name of your hero: ")
    HERO = Things(name)


def stats(hero):
    print "Your stats:\n  Hit points   : %s\n  Attack Power : %s\n  Weapon Bonus : %s\n  Armor Bonus  : %s" \
        % (hero.hp, hero.ap, hero. w, hero.a)


# generate some random numbers between 0 and 9
def rnd09():
    rnd = random.randint(0, 9)
    return rnd


# is there a monster in this room?
def findmonster():
    global ISMONSTER
    if random.randint(1, 101) < 50:
        ISMONSTER = True
    else:
        ISMONSTER = False
    return ISMONSTER


# name the monster
def namemonster():
    global MONSTERNAME
    names = [
        'Magneto',
        'Doctor Doom',
        'Venom',
        'Juggernaut',
        'Thanos'
    ]
    rnd = random.randint(0, 4)
    name = names[rnd]
    return name


def playagain(room):
        choice = raw_input("Do you want to continue?\nPlease Enter Yes or No: ")
        choice = str.lower(choice)
        if choice == "yes" or choice == "y":
            print room.doorstatement()
            print DOORCHOICE
            dchoice = str.lower(raw_input("Which way do you want to go?"))
            print room.doormove(dchoice)
            playmore = True
            return playmore
        elif choice == "no" or choice == "n":
            print "Thank you for playing!"
            playmore = False
            return playmore
        else:
            print "Please enter a valid choice."
            playagain(room)


# fight function --stephen
def fight(p, m):
    while m.hp >= 0 or p.hp >= 0:

        choice1 = raw_input("Enter 1 to attack the monster.\n Enter 2 to run away. \n> ")

        if choice1 == "1":
            m.hp -= (p.ap + random.randint(-2, 3))
            p.hp -= (m.ap + random.randint(-2, 3))
            print "Your hp is %s." % p.hp
            print "The monster hp is %s." % m.hp
        elif choice1 == "2":
            break
        if m.hp <= 0 and p.hp <= 0:
            print "You have killed each other!"
            break
        elif m.hp <= 0:
            print "You have killed the monster!"
            lt = loot(p)
            print "The monster has left some loot, you pick up the %s!" % lt
            break        
        elif p.hp <= 0:
            print "You have died."
            break


# Loot function --Stephen
def loot(p):
        ran = random.randint(0, 100)
        if ran < 50:
            p.a += 1
            lot = "armor"
        else:
            p.w += 1
            lot = "weapon"
        return lot


# user interface
def userinterface():
    global MONSTERNAME
    global ISMONSTER
    global DOORCHOICE
    global HERO
    global MONSTER
    greeting()
    playmore = True
    getname()
    while playmore is True:
        new = Room()

        print "You have entered a new room.\n  %s\n  %s\n  %s\n  %s\n" \
              % (new.north(), new.south(), new.east(), new.west())

        if ISMONSTER is True:
            print "Look out! You see %s in the room!" % MONSTERNAME
            stats(HERO)
            fight(HERO, MONSTER)
            if HERO.hp < 0 and MONSTER.hp < 0:
                print "Thank you for playing!"
                break
            elif HERO.hp <= 0:
                print "Thank you for playing!"
                break
        else:
            print "You do not see any monsters!"

        # Continue playing options:
        playmore = playagain(new)


userinterface()