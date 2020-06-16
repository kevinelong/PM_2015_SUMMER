def ascii(letters):
    output = []
    for c in letters:
        output.append(ord(c))
    return output


def characters(numbers):
    output = ""
    for n in numbers:
        output += chr(n)
    return output


def characters_two(numbers):
    output = []
    for n in numbers:
        output.append(chr(n))
    return ", ".join(output)

s = "Kevin Ernest Long (503) 888-6879 \t\talmost\nthe\nend"
numbers = ascii(s)

original = characters(numbers)  # USE chr
with_commas = characters_two(numbers)  # USE chr

print(numbers)
print(original)
print(with_commas)

