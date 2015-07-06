__author__ = 'rachel'

from random import randrange, choice


def did_player_win(codewords, digits):
    """
    This method is shared by the Game and ComputerPlayer classes because it can check whether a human
    or a computer player has won the game.
    """

    if len(codewords) == digits and set(codewords) == set(["fermi"]):
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

        return codewords

class ComputerPlayer(object):
    def __init__(self, digits):
        self.digits = digits
        self.number_of_guesses = 0
        self.possible_numbers = []
        self.possible_digit_combinations = []
        self.last_guess = []

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
        This method allows the computer to guess the number chosen by a human player. Right now the
        algorithm is not as sophisticated as it could be but it is definitely a big improvement over
        random guessing.
        """

        if did_player_win(codewords or [], self.digits) is True:
            return

        if codewords == ["bagels"]:
            self.bagels()

        elif codewords is not None:

            number_of_picos = codewords.count("pico")
            number_of_fermis = codewords.count("fermi")

            if len(codewords) == self.digits and set(codewords) == set(["pico"]):
                self.all_pico()

            elif len(codewords) == self.digits:
                self.all_pico()
                self.fermi()

            elif number_of_fermis > 1:
                self.multiple_fermis(number_of_fermis)

            elif number_of_picos > 1:
                self.multiple_picos(number_of_picos)

            elif "fermi" in codewords:
                self.fermi()

            elif "pico" in codewords:
                self.pico()

        current_guess = choice(self.possible_digit_combinations)

        self.possible_digit_combinations.remove(current_guess)
        self.last_guess = current_guess

    def bagels(self):
        """
        If the human player responds "Bagels" to the computer player's guess, the computer player will
        rule out any numbers that contain any of the digits in that guess.
        """

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
        """
        If the human player's response contains the word "Pico," the computer player will rule out any
        numbers that don't have at least one digit in common with their last guess.
        """

        new_possibilities = []
        for number in self.possible_digit_combinations:
            for digit in self.last_guess:
                if digit in number:
                    if number not in new_possibilities:
                        new_possibilities.append(number)
        self.possible_digit_combinations = new_possibilities

    def all_pico(self):
        """
        If the human player's response is to type "Pico" as many times as there are digits in the number
        being guessed, the computer player will rule out anything that doesn't have all three of those
        digits.
        """

        new_possibilities = []
        for number in self.possible_digit_combinations:
            for digit in self.last_guess:
                if digit not in number:
                    break
            else:
                if number not in new_possibilities:
                    new_possibilities.append(number)
        self.possible_digit_combinations = new_possibilities

    def multiple_picos(self, number_of_picos):
        """
        If the human player types in "Pico" multiple times but not as many times as there are digits,
        the computer player will rule out any number that doesn't have that number of digits in common.
        """

        new_possibilities = []
        for number in self.possible_digit_combinations:
            digits_in_common = 0
            for digit in self.last_guess:
                if digit in number:
                    digits_in_common += 1
            if digits_in_common == number_of_picos:
                if number not in new_possibilities:
                    new_possibilities.append(number)
        self.possible_digit_combinations = new_possibilities

    def fermi(self):
        """
        If the human player's response contains the word "Fermi," the computer player will rule out any
        numbers that don't have at least one digit in common and in the same place as in their last guess.
        """

        new_possibilities = []
        for number in self.possible_digit_combinations:
            for x in range(0, self.digits):
                if self.last_guess[x] == number[x]:
                    if number not in new_possibilities:
                        new_possibilities.append(number)
        self.possible_digit_combinations = new_possibilities

    def multiple_fermis(self, number_of_fermis):
    """
    If the human player's response contains the word "Fermi" multiple times, the computer player will rule out
    any numbers that don't have at least that number of digits in common and in the same place as in their
    last guess.
    """

        new_possibilities = []
        for number in self.possible_digit_combinations:
            for x in range(0, self.digits):
                if self.last_guess[x] == number[x]:
                    if number not in new_possibilities:
                        new_possibilities.append(number)
        self.possible_digit_combinations = new_possibilities
