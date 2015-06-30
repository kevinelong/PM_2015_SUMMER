__author__ = 'rachel'

from random import randrange

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
            pass

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

        # Note: Is this preserving the traditional order of Bagels keywords (Pico first, then Fermi)?
        # We need to hide from the user as much as possible which digits are correct.

        if len(codewords) == 0:
            codewords.insert(0, "Bagels")

        return codewords

    def did_user_win(self, codewords):

        if len(codewords) == self.digits and set(codewords) == set(["Fermi"]):
            return True
        else:
            return False