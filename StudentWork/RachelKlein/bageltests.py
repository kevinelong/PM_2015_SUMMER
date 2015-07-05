__author__ = 'rachel'
import bagels

# Tests that the initial list of possible digit combinations includes everything it should
# and nothing it should not.

def possibilities_list_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648

# Tests that the "bagels" method reduces the number of possibilities to the appropriate number.
# If 0 is one of the digits in the guess it will rule out fewer possibilities since 0 cannot
# be the leading digit, but the list should always be 210 or fewer.

def bagels_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648
    test_computer_player.computer_guess()
    test_computer_player.computer_guess(["bagels"])
    assert len(test_computer_player.possible_digit_combinations) <= 210

# Tests that the "all_pico" method reduces the number of possibilities to the appropriate number.

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

# Tests that the function that decides whether the player won is still working.

def did_player_win_test():
    assert bagels.did_player_win(["fermi", "fermi", "fermi"], 3) is True

def removing_duplicates_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648
    test_computer_player.computer_guess()
    assert len(test_computer_player.possible_digit_combinations) == 647

possibilities_list_test()
bagels_test()
all_pico_test()
did_player_win_test()