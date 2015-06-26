__author__ = 'lenny'


"""
Jesse Fitzjarrell
Freecodecamp in class example
palindrome
"""

print "Enter a word,\ let's see if it'\s a palindrome?"
potentialpalindrome = raw_input()

# s[0] == s[-1]
# s[1] == s[-2]
# s[2] == s[-3]
# center = s[len(s)/2]
def palindromeChecker(s):


    i=0

    while True:
        if s[i] != s[-(i+1)]:
            return False
        i +=1
        if i == len(s)/2:
            return True
print palindromeChecker(potentialpalindrome)


