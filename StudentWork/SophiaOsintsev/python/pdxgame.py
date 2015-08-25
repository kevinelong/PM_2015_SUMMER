import random

# Basic class for user-created player.

class Player():
    def __init__(self, name):
        self.hp = 90
        self.name = name
    def increase_hp(self, hp):
        self.hp += hp
    def decrease_hp(self, hp):
        self.hp -= hp

# Different types of players user can choose.

class Hipster(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.hp += random.randint(20, 50)

class Panhandler(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.hp += random.randint(5, 15)

class Vegan(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.hp += random.randint(15, 30)

class BeardedTechie(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.hp += random.randint(5, 50)

# Tiles for the player's location.

class Tile():
    def __init__(self, exits):
        self.exits = exits

# Method to move to different tiles in the game.

def tile_change(tile):
    tiles = ''
    for x in tile.exits.keys():
        tiles += x + ' '
    try:
        tile_choice = raw_input("Where do you want to go? %s > " % tiles)
        move(tile.exits[tile_choice], player)
    except KeyError:
        print "I do not understand that."
        tile_change(tile)

# Creates random outcomes for the player in a new tile.

def randomizer(player):

    response = [ "Rain", "a Canvasser", "the Naked Bike Ride", "Bike Messengers", "Rush Hour",
                 "a Free Box", "Freak Sunshine", "Coffee and Donuts", "a Thrift Store Find",
                 "Free Hugs" ]
    response_num = random.randint(0,9)
    if response_num > 4:
        player.increase_hp(10)
    else:
        player.decrease_hp(10)
    print "You have %s hipster points." % player.hp
    return response[response_num]

def choose_player():
    player_type = raw_input(""" What type of Portlander are you? Choose:
                                0 for hipster
                                1 for vegan
                                2 for panhandler
                                3 for bearded techie """)
    player_name = raw_input("And what do you like to be called? ")
    return player_type, player_name

def move(tile, player):
    check_hp()
    obstacle = randomizer(player)
    print "Guess what? You ran into " + obstacle + ". How Portland!"
    tile_change(tile)

def check_hp():
    if hp >= 150:
        print "You are the ultimate Portlander and YOU WIN!"
        quit()
    elif hp <= 100:
        print "Sorry, you lose. Go back to California."
        quit()

player_type, player_name = choose_player()

if player_type == "0":
    player = Hipster(player_name)
    chosen_type = "Hipster"

elif player_type == "1":
    player = Vegan(player_name)
    chosen_type = "Vegan"

elif player_type == "2":
    player = Panhandler(player_name)
    chosen_type = "Panhandler"

elif player_type == "3":
    player = BeardedTechie(player_name)
    chosen_type = "Bearded Techie"

else:
    print "Sorry, there are no other options."

print "Hi, %s. Isn't it great to be a %s?" % (player_name, chosen_type) + " You are starting with " + str(player.hp) + " hipster points."

hp = player.hp
tile1 = Tile( {} )
tile2 = Tile( {} )
tile3 = Tile( {} )
tile4 = Tile( {} )
tile5 = Tile( {} )
tile1.exits = {"NE": tile5}
tile2.exits = {"N": tile1}
tile3.exits = {"SE": tile2}
tile4.exits = {"SW": tile3}
tile5.exits = {"NW": tile4}
move(tile1, player)