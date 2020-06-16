# These variables show what is in the store and what is in the cart, respectively.

STORE_INVENTORY = dict()
CART_VIEW = dict()

def user_is_eighteen():
    age = int(raw_input("What is your age?"))
    if age < 18:
        print "You can not purchase this item!"
    elif age:
        KeyError
        print "I don't recognize this input, please try again."
    else:
        cart.menu()

class Cart(object):
    def __init__(self):
        self.qty = 0
        self.total_price = 0.0
        self.items = []

    def add_item(self, item_id, item_qty):
        # TODO: Test this.
        item_qty = int(item_qty)
        self.qty += (item_qty)
        CART_VIEW[(item_id)] = item_qty
        self.total_price += STORE_INVENTORY[item_id][1] * item_qty
        STORE_INVENTORY[item_id][2] -= item_qty

    def remove_item(self, item_id):
        if CART_VIEW[item_id]:
            self.total_price -= STORE_INVENTORY[item_id][1] * CART_VIEW[item_id]
            STORE_INVENTORY[item_id][2] += CART_VIEW[item_id]
            del CART_VIEW[item_id]
        else:
            print "Item not in cart."

    def user_is_eighteen(self):
        age = int(raw_input("What is your age?: "))
        if age < 18:
            print "No soup for you!"
            return
        else:
            cart.menu()

    def checkout(self):
        self.user_is_eighteen()

    # The view gives the user more choices if they branch out from the basic menu.

    def view(self):
        print CART_VIEW.items()
        yes_or_no = raw_input("Would you like to update your order before proceeding to checkout? y/n ")
        if yes_or_no.lower() == "y" or yes_or_no.lower() == "yes":
            customer_choice = raw_input("Press 1 to add an item or press 2 to remove an item.")
            if customer_choice == "1":
                self.menu()
            elif customer_choice == "2":
                item_to_delete = raw_input("Please enter the ID of the item you want to remove: ")
                self.remove_item(item_to_delete)
            else:
                print "WTF!"
        elif yes_or_no.lower() == "n" or yes_or_no.lower() == "no":
            self.checkout()

    # The main menu that allows the customer to start their purchase.

    def menu(self):
        if STORE_INVENTORY == {}:
            print "Sorry, the store is closed. We are out of stuff."
        else:
            item_list = ''
            print "Here is what we have:"
            print "Id\tName\tPrice\tQuantity"
            for item in STORE_INVENTORY:
                item_list = item_list + str(item)
                for x in STORE_INVENTORY[item]:
                    item_list = item_list + "\t" + str(x)
                item_list += "\n"
            print item_list
            customer_choice = raw_input("Please enter the item number of the item you want to buy: ")
            customer_count = raw_input("Please enter how many you want to buy: ")
            self.add_item(customer_choice, customer_count)
            yes_or_no = raw_input("Will there be anything else today? y/n ")
            if yes_or_no.lower() == "y" or yes_or_no.lower() == "yes":
                self.menu()
            elif yes_or_no.lower() == "n" or yes_or_no.lower() == "no":
                self.view()


# The store creates items the customer can add to the cart. Each one has a name, price, and inventory.

class Item(object):
    def __init__(self, id_number, name, price, inventory):
        self.id_number = id_number
        self.name = name
        self.price = price
        self.inventory = inventory
        STORE_INVENTORY[self.id_number] = [self.name, self.price, self.inventory]

    # TODO: Make all these methods. :)

    def check_inventory(self):
        return self.inventory

    def update_inventory(self):
        pass

    def change_price(self):
        pass

# Items we created and running the program

item = Item("01", "beer", 9.99, 200)
item2 = Item("02", "20 tacos", 19.99, 100)
cart = Cart()
user_is_eighteen()
cart.menu()
