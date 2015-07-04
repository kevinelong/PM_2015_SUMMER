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
        self.digits = digits
        self.number_of_guesses = 0
        self.possible_numbers = []
        self.possible_digit_combinations = []
        self.last_guess = []
        self.previous_guesses = []

        # This part makes a list of all the numbers the computer can possibly guess based on
        # the number of digits there are in the number.

        minimum = [1]
        maximum = [1]

        for x in range(digits - 1):
            minimum.append(0)
        minimum = ''.join(map(str, minimum))
        minimum = int(minimum)

        for x in range(digits):
            maximum.append(0)
        maximum = ''.join(map(str, maximum))
        maximum = int(maximum)

        self.possible_numbers = range(minimum, maximum)

        # The possible numbers are then made into lists of digits so it's easier to loop through
        # them and find the digits you have just guessed.

        for x in self.possible_numbers:
            x = (map(int, str(x)))
            self.possible_digit_combinations.append(x)

        # Now we need to eliminate any numbers (lists of digits at this point) that duplicate any
        # digits.

        temporary_list = []

        for list_of_digits in self.possible_digit_combinations:
            if len(set(list_of_digits)) == self.digits:
                temporary_list.append(list_of_digits)

        self.possible_digit_combinations = temporary_list

    def computer_guess(self, codewords=None):
        """
        This method allows the computer to guess the number chosen by a human player.
        """

        if did_player_win(codewords or [], self.digits) is True:
            return

        # If the human player says "Bagels," all numbers containing any of those digits are
        # removed from the list of possible numbers.

        if codewords == ["Bagels"]:
            self.bagels()

        # If one of the codewords is "Pico," all numbers NOT containing any of those digits
        # are removed from the list of possible numbers.

        elif codewords is not None:
            if len(codewords) == self.digits and set(codewords) == set(["Pico"]):
                self.all_pico()

            elif "Pico" in codewords:
                self.pico()

        current_guess = choice(self.possible_digit_combinations)

        if len(self.possible_digit_combinations) > self.digits:
            while current_guess in self.previous_guesses:
                current_guess = choice(self.possible_digit_combinations)

        self.previous_guesses.append(current_guess)
        self.last_guess = current_guess

    def bagels(self):
        new_possibilities = []
        for number in self.possible_digit_combinations:
            for digit in self.last_guess:
                if digit in number:
                    break
            else:
                if number not in new_possibilities:
                    new_possibilities.append(number)
        self.possible_digit_combinations = new_possibilities

    def pico(self):
        new_possibilities = []
        for number in self.possible_digit_combinations:
            for digit in self.last_guess:
                if digit in number:
                    if number not in new_possibilities:
                        new_possibilities.append(number)
        self.possible_digit_combinations = new_possibilities

    def all_pico(self):
        new_possibilities = []
        for number in self.possible_digit_combinations:
            for digit in self.last_guess:
                if digit not in number:
                    break
            else:
                if number not in new_possibilities:
                    new_possibilities.append(number)
        self.possible_digit_combinations = new_possibilities

    def fermi(self):
        new_possibilities = []
        for number in self.possible_digit_combinations:
            for x in range(0, self.digits):
                if self.last_guess[x] == self.possible_digit_combinations[x]:
                    if number not in new_possibilities:
                        new_possibilities.append(number)
                else:
                    break
        self.possible_digit_combinations = new_possibilities
