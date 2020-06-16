word = raw_input("Please enter one word to translate into pig latin:  ")

def translate(word):
    x = 0
    while word[x] not in ("a", "e", "i", "o", "u"):
        x += 1
    if word[x] in ("a", "e", "i", "o", "u"):
        return word[x:] + word[:x] + "ay"

print translate(word)