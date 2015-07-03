__author__ = 'rachel'
import bagels

# Tests that the initial list of possibile digit combinations includes everything it should
# and nothing it should not.

def possibilities_list_test():
    test_computer_player = bagels.ComputerPlayer(3)
    assert test_computer_player.possible_digit_combinations == 648

# Tests that the "bagels" method reduces the number of possibilities to the appropriate number.

def bagels_test():
    test_computer_player = bagels.ComputerPlayer(3)
    test_computer_player.computer_guess(["Bagels"])
    assert test_computer_player.possible_digit_combinations == 180

# Tests that the "all_pico" method reduces the number of possibilities to the appropriate number.

def all_pico_test():
    test_computer_player = bagels.ComputerPlayer(3)
    test_computer_player.computer_guess(["Bagels"])
    assert test_computer_player.possible_digit_combinations == 6

possibilities_list_test()
bagels_test()
all_pico_test()
