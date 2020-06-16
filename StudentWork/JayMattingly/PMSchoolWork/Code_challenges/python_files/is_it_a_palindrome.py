def palindrome():
    string = [raw_input("Check to see if your word is a palindrome!").split()]
    string_2 = string[::-1]
    if string == string_2:
        print "Yay it's a pali!!!!"
    else:
        print "It's not a pali!!!!Too bad!!!!"


def play_game():
    choice = raw_input("Would you like to check another PALI???? [y/n]")
    if choice == 'y':
        palindrome()
        play_game()
    else:
        print "Game Over! Thanks for playing!"
        return
palindrome()
play_game()
