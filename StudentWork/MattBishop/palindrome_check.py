def palindrome():
    a = [raw_input("Enter a word to see if its a palindrome:  ").split()]
    b = a[::-1]
    if a == b:
        print True
    else:
        print False

def play_again():
    choice = raw_input ("Play again?  [y]/[n]  ")
    if choice == 'y':
        palindrome()
        play_again()
    else:
        print("Goodbye!")


palindrome()
play_again()
