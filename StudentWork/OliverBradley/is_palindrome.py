def isPalindrome(string):
    """Accepts string and returns True if palindrome or False otherwise"""
    if len(string) <=1 :
        return True
    else:
        return string[0] == string[-1] and isPalindrome(string[1:-1])

tester = raw_input("Please enter a string: ")
print isPalindrome(tester)