__author__ = 'stephen'

#Store_shopping_cart

#two classes: Cart, item
#each class has at least 2 items attributes(are they mutable or immutable?)
#Ability to add items to the cart, view the current cost of the cart, and check out

# The Shopping cart

class Item(object):
    def __init__(self):
        self.price = 0.00
        self.name = ''
        self.barcode = ''

    __
    def set_price(self,price =0 ):
        self.price =

class Cart:
    def __init__(self):
        self.numberOfItems = 0
        self.itemlist = []

    def add_item(self, item):
        self.itemlist.append(item)
        return self.itemslist
    def remove_item(self):
        pass

    def show_items(self):
        print self.itemlist
