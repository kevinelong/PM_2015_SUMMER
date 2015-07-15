__author__ = 'rachel'
import bagels
import sys
from time import sleep

def guess(new_game):
    """
    This method prompts the user to guess a new number. It then converts the guess from
    a string to a list of digits that can be compared to the computer's chosen number.
    """
    try:
        current_guess = int(raw_input("Okay, I'm thinking of my number! What do you think it is??? "))
        list_of_digits = map(int, str(current_guess))
        if len(list_of_digits) != new_game.digits:
            print "Hey, you're not guessing the right number of digits. " \
                  "Your guess should be {} digits long.".format(new_game.digits)
        elif len(set(list_of_digits)) < len(list_of_digits):
            print "Remember, there are no repeating digits in this number!"
        else:
            current_codewords = new_game.compare_guess(list_of_digits)
            results_of_guess(current_codewords, new_game)
    except ValueError:
        print "That's not a real guess, silly!"


def results_of_guess(codewords, game, new_game):
    """
    This method shows the human player keywords based on how the computer player has evaluated
    their guess. It also shows how many guesses the human player has used so far.
    """

    # Before giving feedback on the latest guess, the computer checks to see if the human won.

    lowercase_codewords = []
    for word in codewords:
        lowercase_codewords.append(word.lower())

    if bagels.did_player_win(lowercase_codewords, new_game.digits):
        you_win()
        sys.exit()
    else:

        # Rather than display codewords in the order they're originally added to the list,
        # we want to list any "Pico" responses first and then any "Fermi" responses. This is
        # the traditional Bagels order and it makes it harder for the human player to guess.

        codewords.sort(reverse=True)
        print " ".join(codewords)

        if new_game.number_of_guesses == 1:
            print "So far, you've made 1 guess."
        else:
            print "So far, you've made {} guesses.".format(new_game.number_of_guesses)


def you_win(game):
    """
    Provides feedback to user when they win the game.
    """
    print "You win! That was awesome! It took you {} guesses.".format(new_game.number_of_guesses)


def print_directions():
    """
    The user can choose to get the rules of the game when they start.
    """
    print "Oh good! I love explaining things!"
    sleep(2)
    raw_input("One player chooses a random number and the other one has to guess it. >> ")
    raw_input \
        ("Let's say I'm the one choosing a number. No digits can repeat, and the first digit won't be 0. >> ")
    raw_input("If no digits are right, I'll say \'Bagels.\' >> ")
    raw_input("If you guess one digit right but it's in the wrong place, I'll say \'Pico\'. >> ")
    raw_input("If that happens twice, I'll say it twice. But I won't tell you which ones I mean. >> ")
    raw_input("If you get any digit right AND it's in the right place, I'll say \'Fermi\' "
              "(could also happen twice). >> ")
    raw_input("Then you use my wacky code to keep guessing until you get it right! >> ")


def compare_computer_guess(computer_player):
    """
    Prompts the user for input on how well the computer did on its last guess.
    """
    computer_guess = ''.join(map(str, computer_player.last_guess))
    print computer_guess
    guess_response = raw_input \
        ("Okay, how did I do? Remember, type \'Bagels\' if none of the digits are right,\n"
         "\'Pico\' every time I got a digit right but it's in the wrong place,\n"
         "and \'Fermi\' every time a digit is right AND in the right place. >> ").lower()
    guess_response = guess_response.split()
    return guess_response


def computer_guessing_game():
    """
    The whole process of a computer player guessing a number is contained in this method.
    """
    try:
        number_of_digits = int(raw_input("""Do you want me to guess a 3 digit number? 4? 5?
                Less than 3 isn't fun. And you can't pick more than 9 digits. You just can't, okay? >> """))
        new_game = bagels.Game("computer", number_of_digits)
        computer_player = bagels.ComputerPlayer(number_of_digits)
    except ValueError:
        print "Okay, whatever, 3 digits is good."
        new_game = bagels.Game("computer", 3)
        computer_player = bagels.ComputerPlayer(3)
    computer_player.computer_guess()
    codewords = []

    while bagels.did_player_win(codewords, new_game.digits) is False:
        computer_player.number_of_guesses += 1
        codewords = compare_computer_guess(computer_player)

        # Making sure the computer can read user codewords if they use commas.

        codewords_sans_commas = []
        for word in codewords:
            if "," in word:
                word = word.replace(',', '')
                codewords_sans_commas.append(word)
            else:
                codewords_sans_commas.append(word)
        codewords = codewords_sans_commas
        try:
            computer_player.computer_guess(codewords)
        except IndexError:
            raw_input("Hey, you either forgot your number or you're cheating. That's impossible! >> ")
            print "Come back when you're ready to play for real."
            sys.exit()
    print "Yay! I won! And it only took me {} guesses.".format(computer_player.number_of_guesses)

# A new game is created when this file is run from the console.


def regular_game():
    try:
        number_of_digits = int(raw_input(
            "Do you want to guess a 3 digit number? 4? 5? "
            "The more digits you pick, the harder it is to guess. Less than "
            "3 isn't fun. And you can't pick more than 9 digits. You just "
            "can't, okay? >> "))
        new_game = bagels.Game("human", number_of_digits)
    except ValueError:
        print "Okay, whatever, 3 digits is good."
        new_game = bagels.Game("human", 3)
    while True:
        guess(new_game)


if __name__ == '__main__':
    raw_input(
        "Hi! It's your computer! Care for some Bagels? And by 'Bagels' "
        "I of course mean the fun logic game. >> ")
    need_to_learn = raw_input(
        "Actually I don't care whether you do or not. :D Do you need to "
        "learn the rules? y/n??? >> ")
    if need_to_learn.lower() == "y" or need_to_learn.lower() == "yes":
        print_directions()
    raw_input("Okay then, press enter if you're ready! I am so ready!!! >> ")
    game_type = raw_input(
        "Please type 1 if you want me to pick the number for you to guess "
        "and 2 if you want to pick one for me. >> ")
    if game_type == "1":
        regular_game(new_game)
    elif game_type == "2":
        computer_guessing_game()
    else:
        raw_input("Okay, so you're bad at decisions. I knew that. You can guess this time. >> ")
        try:
            number_of_digits = int(raw_input(
                "Do you want to guess a 3 digit number? 4? 5? The more digits "
                "you pick, the harder it is to guess. Less than 3 isn't fun. "
                "And you can't pick more than 9 digits. You just can't, okay? "
                ">> "))
            new_game = bagels.Game("human", number_of_digits)
        except ValueError:
            print "Okay, whatever, 3 digits is good."
            new_game = bagels.Game("human", 3)
        while True:
            guess(new_game)
