def pig_latin(word):
    english_word = word

    # This string contains all possible initial consonant clusters in the English language.

    consonant_clusters = "plprblbrtrdrklkrglgrflfrthrshrskskrslsmsnspsplsprststrswtwdrkwskwgw"
    vowels = "aeiouAEIOU"

    # First we deal with words that start with 3-letter consonant clusters.

    if english_word[:3] in consonant_clusters:
        english_word = english_word.lower()
        word_length = len(english_word)
        first_three_letters = english_word[:3]
        other_letters = ""
        for letter in english_word[3:word_length]:
            other_letters += letter
        pig_latin_word = other_letters + "-" + first_three_letters + "ay"
        return pig_latin_word

    # Then we take care of words that start with 2-letter consonant clusters.

    elif english_word[:2] in consonant_clusters:
        english_word = english_word.lower()
        word_length = len(english_word)
        first_two_letters = english_word[:2]
        other_letters = ""
        for letter in english_word[2:word_length]:
            other_letters += letter
        pig_latin_word = other_letters + "-" + first_two_letters + "ay"
        return pig_latin_word

    # Then we catch words that start with vowels.

    elif english_word[0] in vowels:
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
assert pig_latin("three") == "ee-thray"
assert pig_latin("I") == "I-yay"
