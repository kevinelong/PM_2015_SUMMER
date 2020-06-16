import time

food_dict = {
        'eggs': {"name": "eggs", "amount": "dozen", "price": 1.99},
        'milk': {"name": "milk", "amount": "gallon", "price": 2.59},
        'flour': {"name": "flour", "amount": "pound", "price": 3.49}
}

shoppers_wallet = 10.49
user_cart = []
shopping_list = []
total = []

class Shopping_cart():

    def __init__(self):
        pass

    def add_item(self):
        print "What do you want to add?\nType 'done' to exit."
        while True:
            new_item = raw_input("> ").lower()

            if new_item == "done":
                self.view_cart()
                menu()

            user_cart.append(new_item)

            if len(user_cart) == 1:
                print "There is 1 item in your cart"
            else:
                print "There are {} items in your cart".format(len(user_cart))
            menu()


    def remove_items(self):
        print ', '.join(user_cart)
        to_delete = raw_input("What item would you like to delete?\nType 'done' to exit.: ").lower()
        for item in user_cart:
            if to_delete == item:
                del item
            elif to_delete == 'done':
                menu()
            else:
                print "That item is not in your cart."



    def view_cart(self):
        if len(user_cart) == 0:
            print "Your cart is empty"
        else:
            for item in user_cart:
                print "%s: %s" % (food_dict[item]['name'], food_dict[item]['price'])
                total.append(food_dict[item]['price'])
            print "total: %s" % sum(total)
            if sum(total) > shoppers_wallet:
                print "You don't have enough funds."



# Makes a shopping list
def make_list():
    print "You have {} items in your list.".format(len(shopping_list))
    choice = raw_input("would you like to add items to your list or delete items?\n type 'list' to exit: ").lower()
    if choice == "add":
        while True:
            new_list_item = raw_input("> ").lower()

            if new_list_item == "list":
                show_shopping_list()

            shopping_list.append(new_list_item)

            if len(shopping_list) == 1:
                print "There is 1 item in your cart"
            else:
                print "There are {} items in your cart".format(len(shopping_list))
            continue
        else:
            Shopping_cart.remove_items()


# Shows shopping list
def show_shopping_list():
    print ', '.join(shopping_list)
    menu()


# Main menu
def menu():
    choice = raw_input("Would you like to shop, check out, or go to main menu?: ").lower()
    if choice == "check out":
        Shopping_cart().view_cart()
    elif choice == "shop":
        Shopping_cart().add_item()
    else:
        menu()

# initialization
welcome = raw_input("Welcome to the shopping cart.\n1. Check shopping list\n2. Go shopping\nChoose by number: ")
if welcome == "1":
    make_list()
else:
    shopping = Shopping_cart()
    print "Choose your item!"
    shopping.add_item()


def checkage(age):
    """
    usage: checkage(age)
    If age is less than 18 will return a False response
    If age is greater than or equal too, will return a True response
    """
    if age < 18:
        return False
    elif age >= 18:
        return True

