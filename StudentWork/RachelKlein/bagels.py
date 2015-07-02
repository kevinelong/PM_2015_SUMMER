__author__ = 'rachel'

from random import randrange, choice

def did_player_win(codewords, digits):
    """
    This method is shared by the Game and ComputerPlayer classes because it can check whether a human
    or a computer player has won the game.
    """

    if len(codewords) == digits and set(codewords) == set(["Fermi"]):
        return True
    else:
        return False

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
                raise Exception("Infinite loop detected!")
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

        # Sorting the list so it's harder for the human to tell which digits the computer
        # is talking about with the keywords.

        return sorted(codewords)

class ComputerPlayer(object):

    def __init__(self, digits):
        """
        The computer player can store information about its guesses in a variety of different ways.
        """
        self.digits = digits
        self.first_digit_possibilities = range(1, 10)
        self.other_digit_possibilities = range(0, 10)
        self.not_possibilities = []
        self.previous_guesses = []
        self.last_guess = []
        self.next_guess = []
        self.best_guess = []

    def computer_guess(self, codewords=None):
        """
        This method allows the computer to guess the number chosen by a human player.
        """
        current_guess = []

        # if "Fermi" in codewords:
        #     if len(self.not_possibilities) >=  2:

        # TODO: Figure out if there is a way to do this part without so much nested looping.

        if codewords == ["Bagels"]:
            for x in self.last_guess:
                if x in self.first_digit_possibilities:
                    self.first_digit_possibilities.remove(x)
                if x in self.other_digit_possibilities:
                    self.other_digit_possibilities.remove(x)
                self.not_possibilities.append(x)
                # Instead of a list of things that are NOT possibilities, maybe make a list
                # of digits that definitely ARE in the number? And other method(s) to test that
                # through deduction?

        first_digit = choice(self.first_digit_possibilities)
        current_guess.append(first_digit)

        infinite_loop_prevention = 0

        while len(current_guess) < self.digits:
            infinite_loop_prevention += 1
            if infinite_loop_prevention > 10:
                raise Exception("Infinite loop detected!")
            new_digit = choice(self.other_digit_possibilities)
            if new_digit not in current_guess:
                current_guess.append(new_digit)

        # This makes sure the computer doesn't guess the same number multiple times.

        if current_guess not in self.previous_guesses:
            self.previous_guesses.append(current_guess)
            self.last_guess = current_guess
        else:
            computer_guess()

        return self.last_guess

class SmarterComputerPlayer(ComputerPlayer):
    """
    A computer player with a somewhat smarter playing algorithm.
    """
