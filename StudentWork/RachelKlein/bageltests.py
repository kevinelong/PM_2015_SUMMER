__author__ = 'rachel'
import bagels

# Tests that the initial list of possible digit combinations includes everything it should
# and nothing it should not.

def possibilities_list_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648

# Tests that all codeword-based methods reduce the number of possibilities to the appropriate number.
# If 0 is one of the digits in the guess it will rule out a different number of possibilities since 0 cannot
# be the leading digit. Since the guesses are random and may or may not contain 0, we are testing for a range
# rather than an exact number.

def bagels_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648
    test_computer_player.computer_guess()
    test_computer_player.computer_guess(["bagels"])
    assert len(test_computer_player.possible_digit_combinations) <= 210

def all_pico_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648
    test_computer_player.computer_guess()
    test_computer_player.computer_guess(["pico", "pico", "pico"])
    assert len(test_computer_player.possible_digit_combinations) <= 6

def fermi_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648
    test_computer_player.computer_guess()
    test_computer_player.computer_guess(["fermi"])
    assert len(test_computer_player.possible_digit_combinations) <= 185

def multiple_pico_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648
    test_computer_player.computer_guess()
    test_computer_player.computer_guess(["pico", "pico"])
    assert len(test_computer_player.possible_digit_combinations) <= 120

def multiple_fermi_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648
    test_computer_player.computer_guess()
    test_computer_player.computer_guess(["fermi", "fermi"])
    assert len(test_computer_player.possible_digit_combinations) <= 21

# Tests that the function that decides whether the player won is still working.

def did_player_win_test():
    assert bagels.did_player_win(["fermi", "fermi", "fermi"], 3) is True

# Tests that the last computer player's guess is removed from the list of possible future
# guesses.

def removing_duplicates_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648
    test_computer_player.computer_guess()
    assert len(test_computer_player.possible_digit_combinations) == 647

possibilities_list_test()
bagels_test()
all_pico_test()
did_player_win_test()
multiple_pico_test()
multiple_fermi_test()