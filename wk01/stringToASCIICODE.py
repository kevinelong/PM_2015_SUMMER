def string_to_ascii(s):
    output = []
    for c in s:
        v = ord(c)
        # opposite of chr
        output.append(v)
        print(bin(v))
    return output

print(string_to_ascii("ABC"))
print(string_to_ascii("KEL"))

