__author__ = 'rachel'

from random import randrange, choice

class Game(object):

    def __init__(self, guesser="human", digits=3):
        """
        Each game stores the number of guesses as an attribute. You will be able to choose
        whether the human player or the computer player will be the guesser and it will
        change how the game is played.
        """
        self.digits = digits
        self.number_of_guesses = 0
        if guesser == "human":
            self.chosen_number = self.create_num(digits)
        # TODO: Figure out what happens when the computer guesses!
        else:
            self.first_digit_possibilities = range(1, 10)
            self.other_digit_possibilities = range(0, 10)
            self.not_possibilities = []
            self.last_guess = []
            if guesser == "computer":
                pass
                # while True:
                #     self.last_guess = self.computer_guess()
            elif guesser == "smarter_computer":
                pass
                # while True:
                #     self.last_guess = self.computer_guess_smarter()

    def create_num(self, digits):
        """
        This method generates a random number of a specified number of digits (3 to start).
        No digits can repeat, and the number cannot start with 0. The digits are stored as
        a list so it's easier to iterate through them and compare them to human guesses.
        """

        final_number = []

        first_digit = randrange(1, 10)
        final_number.append(first_digit)

        infinite_loop_prevention = 0

        while len(final_number) < digits:
            infinite_loop_prevention += 1
            if infinite_loop_prevention > 10:
                raise Exception("This is to make sure if I make a bug it doesn't loop forever.")
            new_digit = randrange(0, 10)
            if new_digit not in final_number:
                final_number.append(new_digit)

        return final_number

    def compare_guess(self, human_guess):

        """
        This method takes the human player's guess and compares the digits and indices
        to those in the random number the computer chose. It returns the code words "Bagel,"
        "Pico," and/or "Fermi" based on whether any digits are right or in the right place.
        """

        self.number_of_guesses += 1
        codewords = []
        digits_place = 0

        while digits_place < self.digits:
            if human_guess[digits_place] == self.chosen_number[digits_place]:
                codewords.insert(0, "Fermi")
            elif human_guess[digits_place] in self.chosen_number:
                codewords.insert(0, "Pico")
            digits_place += 1

        if len(codewords) == 0:
            codewords.insert(0, "Bagels")

        return codewords

    def computer_guess(self, codewords=None):
        """
        This method allows the computer to guess the number chosen by a human player.
        """

        # TODO: Make a computer player class so we can, at a minimum, save past guesses.
        # However, that would mean making a seperate win condition check. :(
        # Maybe just make past_guesses an attribute of the class?

        current_guess = []

        if codewords == ["Bagels"]:
            for x in self.last_guess:
                self.first_digit_possibilities.remove(x)
                self.other_digit_possibilities.remove(x)
                self.not_possibilities.append(x)

        first_digit = choice(self.first_digit_possibilities)
        current_guess.append(first_digit)

        infinite_loop_prevention = 0

        while len(current_guess) < self.digits:
            infinite_loop_prevention += 1
            if infinite_loop_prevention > 10:
                raise Exception("This is to make sure if I make a bug it doesn't loop forever.")
            new_digit = choice(self.other_digit_possibilities)
            if new_digit not in current_guess:
                current_guess.append(new_digit)

        self.number_of_guesses += 1
        self.last_guess = current_guess

    def computer_guess_smarter(self):
        """
        This method is my attempt to create a "smarter" guessing method for the
        computer player.
        """
        pass

    def did_player_win(self, codewords):

        if len(codewords) == self.digits and set(codewords) == set(["Fermi"]):
            return True
        else:
            return False