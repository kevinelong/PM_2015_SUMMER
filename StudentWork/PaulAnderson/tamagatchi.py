import random
dog_sayings = ["Let's play!", "Ball!?", "I'm hungry", "I've gotta pee!!!", "I've need to poop!", "SQUIRREL!!!"]
cat_sayings = ["Feed me.", "Puny Human", "Leave me alone.", "You may pet me now", "I need scratches!", "I'm sleeping!"]
bird_sayings = ["tweet", "twiddle-dee-dee", "zzzzzzzz"]
spider_sayings = ["what's going on!?", "I see you.", "Where is my dinner?"]

animal_emotions = ['hungry', 'tired', 'playful', 'dead']


class Animal(object):

    def __init__(self, name):
        self.legs = 4
        self.eyes = 2
        self.ears = 2
        self.name = name
        self.hunger = 0
        self.cleanliness = 0
        self.tiredness = 0
        self.happiness = 3

    def feed(self):
        self.hunger -= 100

    def sleep(self):
        self.tiredness -= 100

    def pet(self):
        pass

    def kill_pet(self):
        pass

class Dog(Animal):
    speak = random.choice(dog_sayings)
    greeting = speak

class Cat(Animal):
    speak = random.choice(cat_sayings)
    greeting = speak

class Tarantula(Animal):
    def __init__(self):
        self.legs = 8
        self.eyes = 10
        self.happiness = 0
    speak = random.choice(spider_sayings)
    greeting = speak

class Bird(Animal):
    leg = 2
    speak = random.choice(bird_sayings)
    greeting = speak


def hungry():
    pass

def tired():
    pass

def time():
    """
    Set a time limit
    """

# Let's player choose an animal
def pick_animal():
    choice = raw_input("""Welcome to the virtual pet store.
    These are the animals we have.
    Dog
    Cat
    Bird
    Tarantula

    What animal would you like to take home?:  """).lower()

    if choice == "dog":
        new_name = raw_input("What would you like to name your dog?: ")
        pet = Dog(new_name)
        print pet.greeting
    elif choice == "cat":
        new_name = raw_input("What would you like to name your cat?: ")
        pet = Cat(new_name)
        print pet.greeting
    elif choice == "bird":
        new_name = raw_input("What would you like to name your bird?: ")
        pet = Bird(new_name)
        print pet.greeting
    elif choice == "tarantula":
        new_name = raw_input("What would you like to name your spider?: ")
        pet = Tarantula(new_name)
        print pet.greeting
    else:
        play_game()
    return pet

def play_game():
    pet = pick_animal()
    emotion = random.choice(animal_emotions)
    if emotion == 'hungry':
        print "{} is hungry, you should feed him".format(pet.name)
        hungry()
    elif emotion == 'tired':
        print "{} is tired, it's nap time".format(pet.name)
    elif emotion == 'playful':
        print "{} is playful.  Let's go!".format(pet.name)
    elif emotion == 'dead':
        print "Maybe you should get a goldfish."
    else:
        play_game()


play_game()
