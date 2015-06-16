def user_input():
	word = raw_input("Please write a word with random capitalization: ")
	return word

def reverse_capitalization(normal_word):
	reversed_word = normal_word.swapcase()
	return reversed_word

def reverse_capitalization_test():
	assert(reverse_capitalization('Rachel') == 'rACHEL')

stuff = user_input()
reverse_capitalization(stuff)
reverse_capitalization_test()