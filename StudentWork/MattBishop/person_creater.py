class Person(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

def main():
    person = Person('Matt', 33, "5'10", 200)
    print "My name is {} and I am {} years old. I am {} and weigh {} pounds.".format(person.name, person.age,
    person.height, person.weight)

if __name__ == '__main__':
    main()
