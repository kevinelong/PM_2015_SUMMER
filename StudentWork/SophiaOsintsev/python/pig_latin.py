__author__ = 'sophiaosintsev'
# Translate the provided string to pig latin.

def pig_latin(string):
    word_list = string.split()
    piggy_sentence = []

    for word in word_list:
        # add 'way' to word if word begins w/vowel
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            string = word + 'way'
            piggy_sentence.append(string)
            # remove first letter in word if it begins w/consonant
        elif word[0] not in ['a', 'e', 'i', 'o', 'u']:
            letter = list(word)
            first_letter = letter.pop(0)
            word = word.lstrip(first_letter)
            piggy = word + first_letter + "ay"
            piggy_sentence.append(piggy)
    print ' '.join(piggy_sentence)
#
pig_latin('i love to eat')
# comment