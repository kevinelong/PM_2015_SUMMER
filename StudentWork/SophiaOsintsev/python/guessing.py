from random import randint

def game(tries):
    # global count
    # global tries
    target_num = randint(1, 100)
    guess = int(raw_input("Guess a number between 1 and 100: "))
    count = 1

    while guess != target_num:
        if guess > target_num:
            print "Too high. Try again!"
            tries -= 1
            print "You have %s guesses left" % tries
        else:
            print "Too low. Try again!"
            tries -= 1
            print "You have %s guesses left" % tries
        if count >= 7:
            print "You are out of guesses! " + "The right number was " + str(target_num)
            break
        else:
            guess = int(raw_input("Enter a new guess: "))
            count += 1
    if guess == target_num:
        print "You got it! It took you " + str(count) + " tries."

game(7)

