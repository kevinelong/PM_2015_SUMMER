from django.db import models
import random
import sys
from time import sleep

class Pet(models.Model):
    name = models.CharField(
        max_length=255,
        null='True', blank='True',
    )

    fullness = models.IntegerField(
        default=4,
        null='True', blank='True',
    )

    health = models.IntegerField(
        default=5,
        null='True', blank='True',
    )

    days_old = models.IntegerField(
        default=2,
        null='True', blank='True',
    )

    happiness = models.IntegerField(
        default=5,
        null='True', blank='True',
    )

    # Stats change in both random and predictable ways when your pet "sleeps" at the end of each "day."

    def change_stats(self):
        self.days_old += 1
        self.fullness -= 1
        self.health -= random.randint(0, 2)
        self.happiness -= 1
        self.save()

    def print_stats(self):
        print "Good morning. Today, {} is {} days old.".format(self.name, self.days_old)
        print "{}'s fullness level is {}".format(self.name, self.fullness)
        print "{}'s health level is {}".format(self.name, self.health)
        print "{}'s happiness level is {}".format(self.name, self.happiness)

    def check_stats(self):

        if self.fullness < 3:
            print "{} is getting very hungry! Time for food!".format(self.name)

        if self.health < 3:
            print "It looks like {} doesn't feel well. Time for a vet visit.".format(self.name)

        if self.happiness < 3:
            print "{} is lonely and needs some playtime!".format(self.name)

    def feed_me(self):
        if self.fullness >= 4:
            print "{} isn't hungry right now.".format(self.name)
        else:
            print "Yay! {} loved their food!".format(self.name)
            self.fullness += 1
            self.save()

    def pet_me(self):
        print "Hooray! {} loves spending time with you!".format(self.name)
        self.happiness += 1
        self.save()

    def vet_visit(self):
        print "{} did not enjoy going to the vet, but it was good for them.".format(self.name)
        self.happiness -= 2
        self.health += 5
        self.save()

    def bedtime(self):
        sleep(1)
        print "Sleep tight, little {}. Tomorrow's another big day.".format(self.name)
        for x in xrange(3):
            print "z"
            sleep(1)
        self.change_stats()
        self.animal_rescue()
        self.print_stats()
        self.check_stats()
        self.save()

    def animal_rescue(self):
        if self.fullness == 0:
            print "You let your pet get too hungry and animal rescue took it away. Take better care of your pets!!"
            sys.exit(0)

        elif self.health == 0:
            print "You let your pet get too unhealthy and animal rescue took it away. Take better care of your pets!!"
            sys.exit(0)

        elif self.happiness == 0:
            "You let your pet get too lonely and animal rescue took it away. Take better care of your pets!!"
            sys.exit(0)

    def __unicode__(self):
        return self.name
