pet_list = ("""

            ******************************
            * 1.Dog                      *
            *                            *
            * 2.Cat                      *
            *                            *
            * 3.Parrot                   *
            *                            *
            * 4.Tiger                    *
            *                            *
            ******************************
""")
    def death_by_hunger(self):
        if self.hunger <= 0:
            print "\nYour pet as passed away from starvation!"
        elif self.hunger == xrange(1, 5):
            print "\nI'm so so so hungry!"

    def sadness_effect(self):
        if self.happiness <= 8:
            print "\nI'm feeling sad..."
            self.life -= 2

    def hunger_occurs(self):
        if self.hunger <= 12:
            print "\nI'm feel hungry"
            self.life -= 1

    def feed_pet(self):
        if self.hunger >= 15:
            print "Thanks but I'm not hungry."
        else:
            print "Wow, that tasted great! Thanks!"
            self.hunger += 2

    def clean_pet(self):
        if self.hygiene >= 15:
            print "Thanks but I'm not hungry."
        else:
            print "Wow, that tasted great! Thanks!"
            self.hygiene += 3

    def pet_pet(self):
        if self.happiness >= 15:
            print "I'm already very happy! Thanks though!"
        else:
            print "Wow! That feels great! Thank you so much for the loves!!!"
            self.happiness += 2

def game_play():
    print pet_list
    choice = raw_input("What pet would you like to adopt?")