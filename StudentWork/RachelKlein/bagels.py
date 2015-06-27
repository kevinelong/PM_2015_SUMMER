__author__ = 'rachel'

from random import randrange

class Game(object):

    def __init__(self, guesser="human"):
        """
        Each game stores the number of guesses as an attribute. You will be able to choose
        whether the human player or the computer player will be the guesser and it will
        change how the game is played.
        """
        self.number_of_guesses = 0
        # Note: should self.previous_guess_results be a list of dictionaries? Key = guess, value = keywords?
        self.previous_guess_results = []
        if guesser == "human":
            self.chosen_number = self.create_num()
            pass
        else:
            pass

    def create_num(self, digits=3):
        """
        This method generates a random number of a specified number of digits (3 to start).
        No digits can repeat, and the number cannot start with 0. The digits are stored as
        a list so it's easier to iterate through them and compare them to human guesses.
        """

        # Note: number of digits cannot be more than 10 or it will be an infinite loop!

        final_number = []

        first_digit = randrange(1, 10)
        final_number.append(first_digit)

        while len(final_number) < digits:
            new_digit = randrange(0, 10)
            if new_digit not in final_number:
                final_number.append(new_digit)

        return final_number

    def compare_guess(self, human_guess):

        """
        This method will take the human player's guess and compare the digits and indices
        to those in the random number the computer chose. It will return the code words "Bagel,"
        "Pico," and "Fermi" based on whether any digits are right or in the right place and the UI
        will relay this back to the human player.
        """

        pass