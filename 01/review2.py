# Concatenate (Join together) two strings in various ways.

print("1. Use the Plus Operator to create an expression to concatenate two string constants.")
print("A" + "B")
print("C" + "D")

print("2. Declare two variables and assign them values and then concatenate them.")
x = "A"
y = "B"
print(x + y)
v1 = "C"
v2 = "D"
print(v1 + v2)

print("3. Define a Function that takes two Parameters/Arguments",)
print("call the function twice to show code reuse.")


def concatenate(x, y):
    return x + y


print(concatenate("A", "B"))
print(concatenate("C", "D"))

print("4. Declare a class object with a concatenate method,",)
print("create two instance objects by calling the constructor method twice",)
print("assign the instances to a variables,",)
print("call the concatenate method")


class Builder(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def concatenate(self):
        return self.x + self.y


builder1 = Builder("A", "B")
builder2 = Builder("C", "D")
print(builder1.concatenate())
print(builder2.concatenate())

print("5. use join on empty delimiter string")
print("".join(["A", "B"]))
print("".join(["C", "D"]))

print("6. use chr function to convert ascii integers to character strings")
print(chr(65) + chr(66))
print(chr(67) + chr(68))

print("7. use slice notation to print(selected pieces from index to index plus 2")
both = "AB CD"
print(both[:2])
print(both[-2:])

print("8. Binary")
print(chr(0b1000001) + chr(0b1000010))
print(chr(0b1000011) + chr(0b1000100))

print("9. ASCII Integer Plus Offset")
base = ord("A")
print(chr(base) + chr(base + 1))
print(chr(base + 2) + chr(base + 3))

print("10. Loop through list of integers")
result = ""

for character in [65, 66, 13, 10, 67, 68]:
    result = result + chr(character)
print(result)

print( "11. pull ones and zeros out of a string one byte(8 bits) at a time")
result = ""
string = "010000010100001000001101000010100100001101000100"
for index in range(0, len(string), 8):
    bits = string[index: index + 8]
    n = int(bits, 2)
    result = result + chr(n)
print(result)