#Return the length of the longest word in the provided sentence.

#
def find_longest_word(string):
# Go through each word
    word_list = string.split()
    longest = ""
    for word in word_list:
        if len(longest) < len(word):
            longest = word
    return longest

print find_longest_word('The quick brown fox jumped over the lazy dog')

