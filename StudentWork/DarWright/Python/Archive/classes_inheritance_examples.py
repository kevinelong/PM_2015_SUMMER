class LivesOnEarth(object):

    def something(self):
        pass


class Animal(object):

    def take_for_walk(self):
        put_on_harness()
        pass

    def feed(self):
        pass

    # def put_on_harness(self):
    #     pass

class Dog(Animal):

    def take_for_walk(self):  # this over writes the parent method
        super(Dog, self).take_for_walk()  # this line say execute code in parent class then the next line(s)
        grab_poop_bags()


    # def grab_poop_bags(self):
    #     pass

    def give_bath(self):
        pass

class Cat(Animal):

    def take_for_walk(self):
        pass


