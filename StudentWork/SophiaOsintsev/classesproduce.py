class Produce:
    def __init__(self, name, cost, count):
        self.name = name
        self.cost = cost
        self.count = count
        self.profit = 0

    def sell(self):
        if self.count <= 0:
            print 'There are no items left to sell'
        else:
            self.profit += self.cost
            self.count -= 1
            print self.cost

apple = Produce("apple", .59, 50)
apple.sell()
print apple.profit
print apple.count
