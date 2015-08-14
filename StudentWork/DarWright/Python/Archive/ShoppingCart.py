# item barcode, price, name/description
# cart num of items, add item, remove item,
# check out sum total, tender out

# cart -
class Item(object):
    def __init__(self):
        self.price = 0
        self.name = ''
        self.barcode = ''

    def __repr__(self):
        return self.name

    def set_price(self, price=0):
        self.price = price

    def set_name(self, name='a'):
        self.name = name

    def set_barcode(self, barcode='111'):
        self.barcode = barcode

    def create_item(self, price, name, barcode):
        self.set_price(price)
        self.set_name(name)
        self.set_barcode(barcode)
        # return {name + price: price, name: name, barcode: barcode}

    def show_item(self):
        return {'price': self.price, 'name': self.name, 'barcode': self.barcode}

class Cart:
    def __init__(self):
        # self.numofitems = 0
        self.itemlist = []
        self.total = 0.00

    def add_item(self, item):
        self.itemlist.append(item)
        # return self.itemlist

    def remove_item(self):
        # search through the item list
        # offer or print item choices
        # get the user to say what item to remove
        # remove the item
        # for item in self.itemlist:
        self.show_items()
        choice = raw_input("Enter the name of the item you want to remove: ")
        index = next(index for (index, d) in enumerate(self.itemlist) if d["name"] == choice)
        if choice == 'Widget':
            check_id()
        #TODO add error catching
        del self.itemlist[index]

    def clear_cart(self):
        self.itemlist = []

    def show_items(self):
        print self.itemlist
        #TODO make this look pretty


    def sum_total(self):
        for item in self.itemlist:
            a = float(item["price"])
            self.total += a

def check_id():
    age = int(raw_input('Please enter your age:\n'))
    if age >= 18:
        return True
    else:
        print("You are not old enough to purchase the Widget!")
        return False

def main_menu():
    print





            # if isinstance(iter(self.itemlist), int) == True:
            #
            #     self.total +=


item = Item()
item.create_item('2.00', 'Widget', 'acb123')
item2 = Item()
item2.create_item('1.23', 'Soda', '1234abc')
cart = Cart()
# print item.show_item()
cart.add_item(item.show_item())
cart.add_item(item2.show_item())
cart.show_items()
print cart.total
cart.sum_total()
print cart.total
cart.remove_item()
cart.show_items()
cart.clear_cart()
cart.show_items()

# class CheckOut:
#
#     def sum_total(self):
#
#
#     def tender(self):




# UNIT Test
# def test_create_item
# item = Item()
# item.create_item('soda', '0.99','000111')
# assert(item.name == 'soda')
# assert(item.price == '0.99')
# assert(item.barcode == '000111')

#
# item = Item()
# item.create_item('2.00', 'widget', 'abc123')
# print item.price, item.name, item.barcode
#
# item.set_price('5.00')
# print item.price, item.name, item.barcode
#
# item.set_name('dodad')
# print item.price, item.name, item.barcode
#
# item.set_barcode('adjjfadjfakl;j')
# print item.price, item.name, item.barcode