__author__ = 'rachel'
import bagels
import sys
from time import sleep

def guess():
    """
    This method prompts the user to guess a new number. It then converts the guess from
    a string to a list of digits that can be compared to the computer's chosen number.
    """
    current_guess = int(raw_input("Okay, I'm thinking of my number! What do you think it is??? "))
    list_of_digits = map(int, str(current_guess))
    if len(list_of_digits) != new_game.digits:
        print "Hey, you're not guessing the right number of digits. " \
              "Your guess should be {} digits long.".format(new_game.digits)
    else:
        current_codewords = new_game.compare_guess(list_of_digits)
        results_of_guess(current_codewords, new_game)

def results_of_guess(codewords, game):
    """
    This method will show the human player keywords based on how the computer player has evaluated
    their guess. It will also show how many guesses the human player has used so far.
    """

    # If the list codewords is as long as the number of digits in the chosen number and
    # all the slots contain "Fermi", the human user wins!
    if new_game.did_user_win(codewords):
        you_win()
        sys.exit()
    else:
        print ", ".join(codewords)

        if new_game.number_of_guesses == 1:
            print "So far, you've made 1 guess."
        else:
            print "So far, you've made {} guesses.".format(new_game.number_of_guesses)

def you_win():
    """
    Does something cool and possibly bagel-related when the human player wins (either by guessing
    the computer's number in a certain number of guesses or by "stumping" the computer, which will
    also have a limited number of guesses.
    """
    # TODO: Insert cooler reward here!
    print "You win! That was awesome! It took you {} guesses.".format(new_game.number_of_guesses)

def save_user_info():
    """
    Saves information on how many guesses a certain user takes on average to guess a number
    as well as any other relevant information.
    """
    pass

def print_directions():
    """
    The user can choose to get the rules of the game when they start.
    """
    print "Oh good! I love explaining things!"
    sleep(2)
    raw_input("One player chooses a random number and the other one has to guess it. >> ")
    raw_input("You can guess first. I'll think of a number (and the first digit won't be 0). >> ")
    raw_input("If no digits are right, I'll say \'Bagels.\' >> ")
    raw_input("If you guess one digit right but it's in the wrong place, I'll say \'Pico\'. >> ")
    raw_input("If that happens twice, I'll say it twice. But I won't tell you which ones I mean. >> ")
    raw_input("If you get any digit right AND it's in the right place, I'll say \'Fermi\'. >> ")
    raw_input("Then you use my wacky code to keep guessing until you get it right! >>" )

# A new game is created when this file is run from the console.

if __name__ == '__main__':
    raw_input(
        "Hi! It's your computer! Care for some Bagels? And by \'Bagels\' I of course mean the fun logic game. >> ")
    need_to_learn = raw_input ("Oh good! Do you need to learn the rules? y/n??? >> ")
    if need_to_learn.lower() == "y" or need_to_learn.lower() == "yes":
        print_directions()
    raw_input("Okay then, press enter if you're ready! I am so ready!!! >> ")
    possible_digit_choices = range(3, 10)
    number_of_digits = int(raw_input("""Do you want to guess a 3 digit number? 4? 5?
                                The more digits you pick, the harder it is to guess.
                                Less than 3 isn't fun. And you can't pick more than 9 digits.
                                You just can't, okay? >> """))
    new_game = bagels.Game("human", number_of_digits)
    while True:
        guess()