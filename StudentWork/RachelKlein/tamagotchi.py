from time import sleep
import random
import sys

class Animal(object):

	def __init__(self, name):
		self.name = name
		self.fullness = 4
		self.health = 5
		self.days_old = 0
		self.happiness = 5
		self.print_stats()

	def print_stats(self):
		print "Good morning. Today, {} is {} days old.".format(self.name, self.days_old)
		print "{}'s fullness level is {}".format(self.name, self.fullness)
		print "{}'s health level is {}".format(self.name, self.health)
		print "{}'s happiness level is {}".format(self.name, self.happiness)

	def change_stats(self):
		self.days_old += 1
		self.fullness -= 1
		self.health -= random.randint(0, 2)
		self.happiness -= 1

		if self.fullness < 1:
			print "{} is getting very hungry! Time for food!".format(self.name)

		if self.health < 3:
			print "It looks like {} doesn't feel well. Time for a vet visit.".format(self.name)

		if self.happiness < 2:
			print "{} is lonely and needs some playtime!".format(self.name)

	def feed_me(self):
		if self.fullness >= 4:
			print "{} isn't hungry right now.".format(self.name)
		else:
			print "Yay! {} loved their food!".format(self.name)
			self.fullness += 1

	def pet_me(self):
		self.happiness += 1
		print "Hooray! {} loves spending time with you!".format(self.name)

	def vet_visit(self):
		self.happiness -= 1
		self.health += 5
		print "{} did not enjoy going to the vet, but it was good for them.".format(self.name)

	def bedtime(self):
		print "Sleep tight, little {}. Tomorrow's another big day.".format(self.name)
		for x in xrange(3):
			print "z"
			sleep(1)
		self.change_stats()
		self.animal_rescue()
		self.print_stats()

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

class Dog(Animal):

	def walk(self):
		if self.health < 2:
			print "{} doesn't feel well enough for a walk today. :(".format(self.name)
		else:
			print "{} loves getting outside for a walk! You are the BEST!".format(self.name)
			self.happiness += 5
			self.health += 1

	def play_fetch(self):
		if self.health < 2:
			print "{} doesn't feel well enough to play fetch today. :(".format(self.name)
		else:
			print "{} could play fetch for hours!".format(self.name)
			self.happiness += 5
			self.health += 1

	def give_bath(self):
		print "Aww, {} doesn't like baths!".format(self.name)
		self.happiness -= 1

	# TODO: Separate into general Animal UI and species-specific UI to make code more dry.

	def dog_ui(self):
		""" You can do up to 3 things with your pet per day. """
		user_actions = 0
		while user_actions < 3:
			user_actions += 1
			user_choice = int(raw_input(
				"What would you like to do with your dog today? (1) Feed (2) Pet (3) Vet visit (4) Other stuff >> "))
			if user_choice == 1:
				self.feed_me()
			elif user_choice == 2:
				self.pet_me()
			elif user_choice == 3:
				self.vet_visit()
			elif user_choice == 4:
				user_choice_2 = int(raw_input(
					"How about (1) Go for walk (2) Play fetch (3) Give bath >> "))
				if user_choice_2 == 1:
					self.walk()
				elif user_choice_2 == 2:
					self.play_fetch()
				elif user_choice_2 == 3:
					self.give_bath()
		self.bedtime()
		self.dog_ui()

class Cat(Animal):

	def dangle_string(self):
		roll_the_die = random.int(1, 6)
		if roll_the_die > 1:
			print "Yay, playtime!"
			self.happiness += 1
		else:
			print "Meh, not interested."

	def lap_time(self):
		print "{} sits on your lap and purrs. Better stay here awhile.".format(self.name)
		self.happiness += 1
		self.health += 1

	def pet_tummy(self):
		roll_the_die = random.int(1, 6)
		if roll_the_die <= 3:
			print "Yay, {} loves getting tummy pets!".format(self.name)
			self.happiness += 1
		else: 
			print "Hiss, scratch! Don't touch the tummy (for now)."
			self.happiness -= 1

	def cat_ui(self):
		user_actions = 0
		while user_actions < 3:
			user_actions += 1
			user_choice = int(raw_input(
				"What would you like to do with your cat today? (1) Feed (2) Pet (3) Vet visit (4) Other stuff >> "))
			if user_choice == 1:
				self.feed_me()
			elif user_choice == 2:
				self.pet_me()
			elif user_choice == 3:
				self.vet_visit()
			elif user_choice == 4:
				user_choice_2 = int(raw_input(
					"How about (1) Dangle string (2) Lap time (3) Pet tummy >> "))
				if user_choice_2 == 1:
					self.dangle_string()
				elif user_choice_2 == 2:
					self.lap_time()
				elif user_choice_2 == 3:
					self.pet_tummy()
		self.bedtime()
		self.cat_ui()

class Rat(Animal):

	def feed_cheese(self):
		print "Cool, a special treat! {} loves it.".format(self.name)
		self.happiness += 1

	def explore(self):
		print "Rats love exploring new places! {} thinks you're a cool human.".format(self.name)
		self.happiness += 2

	def sit_on_shoulder(self):
		print "Now you've got a little buddy."
		self.happiness += 1

	def rat_ui(self):
		user_actions = 0
		while user_actions < 3:
			user_actions += 1
			user_choice = int(raw_input(
				"What would you like to do with your rat today? (1) Feed (2) Pet (3) Vet visit (4) Other stuff >> "))
			if user_choice == 1:
				self.feed_me()
			elif user_choice == 2:
				self.pet_me()
			elif user_choice == 3:
				self.vet_visit()
			elif user_choice == 4:
				user_choice_2 = int(raw_input(
					"How about (1) Feed cheese (2) Help them explore (3) Have them sit on your shoulder >> "))
				if user_choice_2 == 1:
					self.feed_cheese()
				elif user_choice_2 == 2:
					self.explore()
				elif user_choice_2 == 3:
					self.sit_on_shoulder()
		self.bedtime()
		self.rat_ui()

foo = Cat("Foo")
foo.cat_ui()