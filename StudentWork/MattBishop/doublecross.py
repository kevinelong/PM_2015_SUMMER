from sys import exit
import random
import time

# class Character:
#     def __init__(self, name):
#         self.name = name
#         self.hp = 100
#         self.strength = 10
#         self.agility = 10
#         self.perception = 10
#         self.intuition = 10
#         self.luck = 10
#
#
# class NPC(Character):
#     def __init__(self, name, hp, strength, agility):
#         Character.__init__(self, name)
#         self.hp = hp
#         self.strength = strength
#         self.agility = agility

print """
____________________________________________________________________________________________________________________________________________________________________________________________
8 888888888o.          ,o888888o.     8 8888      88 8 888888888o   8 8888         8 8888888888                 ,o888888o.    8 888888888o.      ,o888888o.       d888888o.      d888888o.
8 8888    `^888.    . 8888     `88.   8 8888      88 8 8888    `88. 8 8888         8 8888                      8888     `88.  8 8888    `88.  . 8888     `88.   .`8888:' `88.  .`8888:' `88.
8 8888        `88. ,8 8888       `8b  8 8888      88 8 8888     `88 8 8888         8 8888                   ,8 8888       `8. 8 8888     `88 ,8 8888       `8b  8.`8888.   Y8  8.`8888.   Y8
8 8888         `88 88 8888        `8b 8 8888      88 8 8888     ,88 8 8888         8 8888                   88 8888           8 8888     ,88 88 8888        `8b `8.`8888.      `8.`8888.
8 8888          88 88 8888         88 8 8888      88 8 8888.   ,88' 8 8888         8 888888888888           88 8888           8 8888.   ,88' 88 8888         88  `8.`8888.      `8.`8888.
8 8888          88 88 8888         88 8 8888      88 8 8888888888   8 8888         8 8888                   88 8888           8 888888888P'  88 8888         88   `8.`8888.      `8.`8888.
8 8888         ,88 88 8888        ,8P 8 8888      88 8 8888    `88. 8 8888         8 8888                   88 8888           8 8888`8b      88 8888        ,8P    `8.`8888.      `8.`8888.
8 8888        ,88' `8 8888       ,8P  ` 8888     ,8P 8 8888      88 8 8888         8 8888                   `8 8888       .8' 8 8888 `8b.    `8 8888       ,8P 8b   `8.`8888. 8b   `8.`8888.
8 8888    ,o88P'    ` 8888     ,88'     8888   ,d8P  8 8888    ,88' 8 8888         8 8888                      8888     ,88'  8 8888   `8b.   ` 8888     ,88'  `8b.  ;8.`8888 `8b.  ;8.`8888
8 888888888P'          `8888888P'        `Y88888P'   8 888888888P   8 888888888888 8 888888888888               `8888888P'    8 8888     `88.    `8888888P'     `Y8888P ,88P'  `Y8888P ,88P'
_____________________________________________________________________________________________________________________________________________________________________________________________

  ,---.        ,--.                    ,--.         ,--.                          ,--.               ,--.                          ,--.
 /  O  \     ,-'  '-. ,---.,--.  ,--.,-'  '-.,-----.|  |-. ,--,--. ,---. ,---.  ,-|  |     ,--,--. ,-|  |,--.  ,--.,---. ,--,--, ,-'  '-.,--.,--.,--.--. ,---.      ,---.  ,--,--.,--,--,--.,---.
|  .-.  |    '-.  .-'| .-. :\  `'  / '-.  .-''-----'| .-. ' ,-.  |(  .-'| .-. :' .-. |    ' ,-.  |' .-. | \  `'  /| .-. :|      \'-.  .-'|  ||  ||  .--'| .-. :    | .-. |' ,-.  ||        | .-. :
|  | |  |      |  |  \   --./  /.  \   |  |         | `-' \ '-'  |.-'  `)   --.\ `-' |    \ '-'  |\ `-' |  \    / \   --.|  ||  |  |  |  '  ''  '|  |   \   --.    ' '-' '\ '-'  ||  |  |  \   --.
`--' `--'      `--'   `----'--'  '--'  `--'          `---' `--`--'`----' `----' `---'      `--`--' `---'    `--'   `----'`--''--'  `--'   `----' `--'    `----'    .`-  /  `--`--'`--`--`--'`----'
                                                                                                                                                                   `---'
"""
time.sleep(3)
print """
Welcome to Double Cross, a text based detective story. Let's begin by creating a character.
"""


def add_character_points():
    attribute = raw_input("\nWhich attribute? Strength, Agility, Perception, Intuition, or Luck?\n").lower()

    if attribute in my_character.keys():
        amount = int(raw_input("By how much?  "))

        if (amount > my_character['points']) or (amount <= 0):
            print "Not enough points!"
        else:
            my_character[attribute] += amount
            my_character['points'] -= amount
    else:
        print "\nThat attribute doesn't exist!\n"


def print_character():
    for attribute in my_character.keys():
        print attribute, " : ", my_character[attribute]


my_character = {'name': '', 'strength': 10, 'agility': 10, 'perception': 10, 'intuition': 10, 'luck': 10, 'health': 100,
                'points': 30}

running = True

my_character['name'] = raw_input("What is your character's name? ")

print """
Let's assign points to your character. Each attribute will affect game play in different ways, such as
displaying special options during scenes, which will aid you in solving mysteries, identifying clues and
character interaction.
"""
time.sleep(5)

print """
Below is a description of each attribute:

Strength = How strong you are. This attribute primarily governs the 'Hit' action.
Agility = How quick you are. This attribute primarily governs the 'Use' action.
Perception = How easily you see what others don't. This attribute is most useful during investigations.
Intuition = How empathetic you are. This attribute is most useful during investigations.
Luck = Pure, dumb luck. A high luck gives you advantages other characters wouldn't normally have!
"""

while running:
    print "\nYou have", my_character['points'], "points left.\n"
    print "1. Add points\n2. See current attributes\n3. Go to game when finished assigning points.\n"

    choice = raw_input("Choice:  ")

    if choice == "1":
        add_character_points()
    elif choice == "2":
        print_character()
    elif choice == "3":
        running = False
    else:
        pass


class Action(object):
    def __init__(self):
        self.speak = "With whom do you wish to speak?  "
        self.hit = "Who do you wish to hit?  "
        self.take = "What do you wish to take?  "
        self.use = "What would you like to use?  "
        self.open = "What would you like to open?  "
        self.help = "Here is the list of valid commands: "


class Scene(object):
    def __init__(self):
        self.scene_actions = ['speak', 'hit', 'take', 'use', 'open', 'help']
        # use Inventory items in each Scene


class Death(Scene):
    def enter(self):
        print ("*game over message*")
        exit(1)


class Office(Scene):
    def enter(self):
        return 'office_building'

    print """
The year is 1944 and you live in the greatest city on Earth - Chicago. You've managed to avoid the draft (for now) and
have been scrapping by for years as a private investigator. The pre-war years were a goldmine, filled with jilted
lovers, insurance and corporate fraud, all manner of scams and schemes and the occasional police contract. And even
though business has steadily declined since the world went to hell, you've always managed to get by. This time, though,
is different. You're on your last dime and haven't had a real case in two months. The water was shut off yesterday, the
lights are about to go out and the landlord will be coming down on you any day now. You've always heard stories about
the Cook County Almshouse - it looks like you'll be getting a firsthand tour real soon.
"""
    raw_input("Press Enter to continue...  ").lower()

    print """
That's why the knock on the door is surprising but welcome, like Christmas come early. You open the door and are greeted
with a confident and cool woman, maybe in her late forties. She is smartly dressed in a freshly pressed dress and a
button up, waist-cinching jacket.  Her dark hair is pulled up in a tight bun nested beneath a glamorous pillbox hat. She
looks you up and down, regards your disheveled state and says dryly, "Are you going to let me in or should I make an
appointment - seeing as how you are obviously a very busy individual." Normally you would not be inclined to entertain
such behavior, but a customer is a customer and your confidence is as threadbare as your cheap suit. You mumble a
greeting and open the door wide; the woman breezes right past you and looks intently around your office.
"""


def dialogue_tree():
    tree_input = raw_input("""

What's your next move, ace?

A.) "Say there - you wanna drink?"
B.) "What can I do for you, Miss uh..."
C.) "Why don't you have a seat and tell me what brings you to my office today."
""").lower()

    if tree_input == 'a':
        print """
"I suppose. What do you have?

You open the drawer to your woefully stocked liquor cabinet and produce a second-rate bottle of scotch whiskey.

"And I suppose that will have to do," she says with a sigh. She eyes the bottle warily but accepts the glass readily,
seemingly grateful.
"""
        if my_character['intuition'] >= 30:
            print """
As she takes a pull from the glass, you notice that her hands shake. You stare for another half second - despite her
outwards appearance she doesn't seem as well-collected as you previously believed.

"Look, I deal with all sorts of cases and have seen just about everything under the sun. There's no need to be
nervous."

"I am certainly not nervous. I am here because I have need of your services. Will you assist me or not?"

"Of course. Of course I will." Your slow nod seems to reassure her a bit but you already get the suspicion
that your new client is already up to no good. She turns to you and says:
"""
        return tree_input == 'c'

    elif tree_input == 'b':
        print """
My name is Martha Sternwood.
"""
    elif tree_input == 'c':
        print """
My name is Martha Sternwood.
"""
    else:
        print "Please enter the letter that corresponds with the dialogue you wish to choose."
        dialogue_tree()


dialogue_tree()


class OfficeBuilding(Scene):
    def enter(self):
        print ("*more text*")
        return 'city_street'


class CityStreet(Scene):  # random encounter
    def enter(self):
        print ("*more text*")
        return 'bus_station'


class BusStation(Scene):
    def enter(self):
        print ("*more text*")
        return 'city_bus'


class CityBus(Scene):
    def enter(self):
        print ("*more text*")
        return 'crime_scene'


class CrimeScene(Scene):
    def enter(self):
        print ("*more text*")
        return 'police_station'


class PoliceStation(Scene):
    def enter(self):
        print ("*more text*")
        return 'hospital'


class Hospital(Scene):
    def enter(self):
        print ("*more text*")
        return 'skylark_lounge'


class SkylarkLounge(Scene):
    def enter(self):
        print ("*more text*")
        return 'bar_stool'


class BarStool(Scene):  # random encounter
    def enter(self):
        print ("*more text*")
        return 'hotel_albatross'


class HotelAlbatross(Scene):
    def enter(self):
        print ("*more_text*")
        return 'hotel_room'


class HotelRoom(Scene):
    def enter(self):
        print ("*more text*")
        return 'tenement_building'


class TenementBuilding(Scene):
    def enter(self):
        print ("*more text*")
        return 'tenement_hallway'


class TenementHallway(Scene):  # random encounter
    def enter(self):
        print ("*more text*")
        return 'apartment_403'


class Apartment403(Scene):
    def enter(self):
        print ("*more text*")
        return 'train_station'


class TrainStation(Scene):
    def enter(self):
        print ("*more text*")
        return 'lawyer_office_building'


class LawyerOfficeBuilding(Scene):  # random encounter
    def enter(self):
        print ("*more text*")
        return 'secretary_office'


class SecretaryOffice(Scene):
    def enter(self):
        print ("*more text*")
        return 'lawyer_office'


class LawyerOffice(Scene):
    def enter(self):
        print ("*more text*")
        return 'entrance_casino'


class EntranceCasino(Scene):  # random encounter
    def enter(self):
        print ("*more text*")
        return 'casino_floor'


class CasinoFloor(Scene):
    def enter(self):
        print ("*more text*")
        return 'blackjack_table'


class BlackjackTable(Scene):
    def enter(self):
        print ("*more text*")
        return 'penthouse_suite'


class PenthouseSuite(Scene):
    def enter(self):
        print ("*more text*")
        return 'ending'


class Ending(Scene):
    def enter(self):
        print ("*end text*")
        exit(1)


class Map(object):
    scenes = {
        'death': Death(),
        'office': Office(),
        'office_building': OfficeBuilding(),
        'city_street': CityStreet(),
        'bus_station': BusStation(),
        'city_bus': CityBus(),
        'crime_scene': CrimeScene(),
        'police_station': PoliceStation(),
        'hospital': Hospital(),
        'skylark_lounge': SkylarkLounge(),
        'bar_stool': BarStool(),
        'hotel_albatross': HotelAlbatross(),
        'hotel_room': HotelRoom(),
        'tenement_building': TenementBuilding(),
        'tenement_hallway': TenementHallway(),
        'apartment_403': Apartment403(),
        'train_station': TrainStation(),
        'lawyer_office_building': LawyerOfficeBuilding(),
        'secretary_office': SecretaryOffice(),
        'lawyer_office': LawyerOffice(),
        'entrance_casino': EntranceCasino(),
        'casino_floor': CasinoFloor(),
        'blackjack_table': BlackjackTable(),
        'penthouse_suite': PenthouseSuite(),
        'ending': Ending()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


def play(game_map):
    current_scene = game_map.opening_scene()

    while True:
        next_scene_name = current_scene.enter()
        current_scene = game_map.next_scene(next_scene_name)


inventory = ['cigarette lighter', '$20 bill', '.45 caliber Colt']


def add_to_inventory(item):
    inventory.append(item)


game_map = Map('office')
play(game_map)
