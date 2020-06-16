# Goal
# Create a program that selects a random word and then allows the user to guess it in a game of hangman.
# Like the real game, there should be blank spots for each letter in the word, and a part of the body should
# be added each time the user guesses a letter than is not in the answer (you may choose how many wrong turns
# the user can make until the game ends).
# Subgoals
# If the user loses, print out the word at the end of the game.
# Create a "give up" option.
import random
import time

class Hangman(object):
    def __init__(self):
        self.word = ''
        self.counter = 6
        self.hidden_word_list = []
        self.word_list = []
        self.guessed_letters = []
        self.start_game()

    # adjusted for trinket to have an internal word list, instead of loading the 3k list.
    # def set_random_word(self, length=8):
    def set_random_word(self, length=8):
        """
        choose a random word from my local dictionary, defaults to 6 characters and greater than 2
        updated with a common word list with around 3k words
        """
        # adjusted for trinket to have an internal word list, instead of loading the 3k list.
        # word_file = "common_word_list.txt"
        # with open(word_file, 'r') as word_list:
        #     narrow_word_choice = [x for x in word_list if len(x) <= length and len(x) >= 3]

        word_list = ['acres\n', 'adult\n', 'advice\n', 'attempt\n', 'August\n', 'Autumn\n', 'border\n', 'breeze\n',
                              'brick\n', 'calm\n', 'canal\n', 'Casey\n', 'cast\n', 'chose\n', 'claws\n', 'coach\n', 'cookies\n',
                              'customs\n', 'damage\n', 'Danny\n', 'deeply\n', 'depth\n', 'doll\n', 'donkey\n', 'Egypt\n', 'Ellen\n',
                              'exist\n', 'facing\n', 'film\n', 'finest\n', 'folks\n', 'fort\n', 'garage\n', 'grabbed\n', 'habit\n',
                              'happily\n', 'Harry\n', 'heading\n', 'hunter\n', 'image\n', 'instant\n', 'January\n', 'kids\n', 'label\n',
                              'Lee\n', 'lungs\n', 'Martin\n', 'melted\n', 'memory\n', 'mill\n', 'mission\n', 'monkey\n', 'Mount\n',
                              'Norway\n', 'nuts\n', 'palace\n', 'plates\n', 'poetry\n', 'pride\n', 'recall\n', 'require\n', 'rhyme\n',
                              'rocky\n', 'rubbed\n', 'rush\n', 'sale\n', 'scared\n', 'shake\n', 'shaking\n', 'shallow\n', 'shout\n',
                              'silly\n', 'slight\n', 'slip\n', 'slope\n', 'soap\n', 'solar\n', 'species\n', 'spin\n', 'stiff\n', 'swung\n',
                              'tales\n', 'thumb\n', 'tobacco\n', 'toy\n', 'trap\n', 'treated\n', 'tune\n', 'vapor\n', 'vessels\n', 'wealth\n',
                              'wolf\n', 'zoo\n', 'wood\n', 'tall\n', 'yellow\n', 'Marine\n', 'inner\n', 'wished\n', 'sounds\n', 'wagon\n',
                              'Jews\n', 'rural\n', 'item\n', 'phone\n', 'attend\n', 'unable\n', 'faced\n', 'huge\n', 'risk\n', 'symbol\n',
                              'seat\n', 'Smith\n', 'walking\n']
        narrow_word_choice = [x for x in word_list if len(x) <= length and len(x) >= 3]
        self.word = random.choice(narrow_word_choice)
        self.word = self.word[:-1].lower()
        if self.word == self.word.capitalize():
            self.set_random_word()

    @property
    def welcome_message(self):
        """
        short little welcome message
        """
        welcome = "Welcome to the Hang man game!\n" \
                  "You will have 10 chances to guess the word!\n" \
                  "Each ^ is a letter to guess!\n" \
                  "Let's play!"
        return welcome

    def choice_word_length(self):
        # commented out for trinket
        # choice = raw_input("How long of a word do you want to guess?\n"
        #                    "Enter a number between 3 and 10: ")
        print "You will get a random length word."
        choice = 8
        try:
            choice = int(choice)
        except ValueError:
            print "Please enter a number only."
        if choice > 10 and choice < 3:
            print "Please enter a number between 3 and 10: "
        else:
            return choice

    def menu_countdown(self):
        """
        little count down timer that looks neat.
        """
        timer = 0.00
        a = "."
        while timer < 1.51:
            time.sleep(.25)
            print a,
            timer += .25
        print "\n"

    def set_hidden_word_list(self):
        """
        hidden word holds the actual word in a list of characters to be compared against
        when the user guesses.
        loads the self.word_list with equal amount of blanks.
        """
        self.hidden_word_list = list(self.word)
        for x in self.hidden_word_list:
            self.word_list += '^'

    def guess(self, letter):
        """
        checks if the letter is in the hidden word and if so, puts it in the visible list
        and if the letter is not found, takes one guess away and appends the letter to the
        used letter list
        """
        for i, x in enumerate(self.hidden_word_list):
            if x == letter:
                self.word_list[i] = self.hidden_word_list[i]
                pass
        if letter not in self.word_list:
            self.counter -= 1
            self.guessed_letters.append(letter)

    def start_game(self):
        """
        starts the game, loads the functions to get it going
        :return:
        """
        print self.welcome_message()
        word_length = self.choice_word_length()
        self.menu_countdown()
        self.set_random_word(word_length)
        self.set_hidden_word_list()
        self.play()

    def set_guess(self):
        """
        gets the user's letter guess including some data integrity checks.
        Also allows the user to quit, or guess the word
        :return:
        """
        letter = raw_input("Enter 'quit' to quit, enter the word guess, or guess a letter: ")
        letter = letter.lower()
        if len(letter) > 1:
            if letter == 'quit' or letter == 'q':
                print "Thank you for playing!"
                exit()
            elif letter != 'quit' and letter != self.word:
                print "Wrong guess, try again!"
                self.set_guess()
            elif letter == self.word:
                print "You win!"
                self.play_again()
            else:
                print "Please only enter one letter."
                self.set_guess()
        elif letter in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            print "You cannot enter numbers, try again!"
            self.set_guess()
        elif letter in self.word_list or letter in self.guessed_letters:
            print "You have already guessed that letter, try again!"
            self.set_guess()
        else:
            self.guess(letter)

    def show_word(self):
        print self.ascii_hangman()
        print "Your word is: "
        guesses = ''.join(self.word_list)
        print guesses
        # print "This is here for testing only!", self.word

    def play(self):
        while self.counter > 0:
            if self.hidden_word_list != self.word_list:
                self.show_word()
                self.set_guess()
                if self.counter > 1:
                    print "You have\033[0;34m %d\033[0m guesses left!" % self.counter
                elif self.counter == 1:
                    print "You have \033[0;31mONE\033[0m guess left!"
                print "Letters used: ", ' '.join(self.guessed_letters)
            else:
                print "You win!"
                self.play_again()

        if self.counter == 0:
            print "Oh no! You lost, the word was %s!" % self.word
            self.play_again()

    def play_again(self):
        replay = raw_input("\nDo you want to play again? y/n > ").lower()
        if replay == 'y':
            self.word = ''
            self.counter = 6
            self.hidden_word_list = []
            self.word_list = []
            self.guessed_letters = []
            self.start_game()
        else:
            print "Good bye!"
            exit()

    def ascii_hangman(self):
        if self.counter == 6:
            hang = "   _____\n" \
                   "   |   |\n" \
                   "       |\n" \
                   "       |\n" \
                   "       |\n" \
                   "  _____|\n"

        elif self.counter == 5:
            hang = "   _____\n" \
                   "   |   |\n" \
                   "   O   |\n" \
                   "       |\n" \
                   "       |\n" \
                   "  _____|\n"

        elif self.counter == 4:
            hang = "   _____\n" \
                   "   |   |\n" \
                   "   O   |\n" \
                   "   |   |\n" \
                   "       |\n" \
                   "  _____|\n"

        elif self.counter == 3:
            hang = "   _____\n" \
                   "   |   |\n" \
                   "   O   |\n" \
                   "  /|   |\n" \
                   "       |\n" \
                   "  _____|\n"

        elif self.counter == 2:
            hang = "   _____\n" \
                   "   |   |\n" \
                   "   O   |\n" \
                   "  /|\  |\n" \
                   "       |\n" \
                   "  _____|\n"
        elif self.counter == 1:
            hang = "   _____\n" \
                   "   |   |\n" \
                   "   O   |\n" \
                   "  /|\  |\n" \
                   "  /    |\n" \
                   "  _____|\n"

        elif self.counter == 0:
            hang = "   _____\n" \
                   "   |   |\n" \
                   "   O   |\n" \
                   "  /|\  |\n" \
                   "  / \  |\n" \
                   "  _____|\n"

        return hang

new = Hangman()




