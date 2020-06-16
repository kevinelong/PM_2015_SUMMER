def is_palindrome(string):
    """Accepts string and returns True if palindrome or False otherwise"""
    string = string.lower().strip()
    if len(string) <=1 :
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])

def main():
    tester = raw_input("Please enter a string: ")
    print is_palindrome(tester)

if __name__ == '__main__':
    main()
