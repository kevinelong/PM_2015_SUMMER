def pig_latin(word):
	english_word = word

	# First we take care of words that start with consonant clusters.

	if english_word[:2] in "plprblbrtrdrklkrglgrflfrthrshrsk"
	"skrslsmsnspsplsprststrswtwdrkwskwgw":
		word_length = len(english_word)
		first_two_letters = english_word[:2]
		other_letters = ""
		for letter in english_word[2:word_length]:
			other_letters += letter
		pig_latin_word = other_letters + "-" + first_two_letters + "ay"
		return pig_latin_word

	# Then we catch words that start with vowels.

	elif english_word[0] in "aeiouAEIOU":
		pig_latin_word = english_word + "-yay"
		return pig_latin_word

	# Everything else gets treated the same (okay, so I haven't dealt with silent letters...)

	else:
		word_length = len(english_word)
		first_letter = english_word[0]
		other_letters = ""
		for letter in english_word[1:word_length]:
			other_letters += letter
		pig_latin_word = other_letters + "-" + first_letter + "ay"
		return pig_latin_word

# Unit tests

assert pig_latin("Rachel") == "achel-Ray"
assert pig_latin("Ollie") == "Ollie-yay"
assert pig_latin("snack") == "ack-snay"