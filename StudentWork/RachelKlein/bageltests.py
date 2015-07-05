__author__ = 'rachel'
import bagels

# Tests that the initial list of possible digit combinations includes everything it should
# and nothing it should not.

def possibilities_list_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648

# Tests that the "bagels" method reduces the number of possibilities to the appropriate number.
# If 0 is one of the digits in the guess it will rule out fewer possibilities since 0 cannot
# be the leading digit.

def bagels_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648
    test_computer_player.computer_guess()
    test_computer_player.computer_guess(["bagels"])
    if 0 in test_computer_player.last_guess:
        assert len(test_computer_player.possible_digit_combinations) == 210
    else:
        assert len(test_computer_player.possible_digit_combinations) == 180

# Tests that the "all_pico" method reduces the number of possibilities to the appropriate number.

def all_pico_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert len(test_computer_player.possible_digit_combinations) == 648
    test_computer_player.computer_guess()
    test_computer_player.computer_guess(["pico", "pico", "pico"])
    if 0 in test_computer_player.last_guess:
        assert len(test_computer_player.possible_digit_combinations) == 4
    else:
        assert len(test_computer_player.possible_digit_combinations) == 6

# Tests that the function that decides whether the player won is still working.

def did_player_win_test():
    assert bagels.did_player_win(["fermi", "fermi", "fermi"], 3) is True

possibilities_list_test()
bagels_test()
all_pico_test()
did_player_win_test()