import time
food_dict = {
        'eggs': {"eggs": "Dozen", "price": 1.99},
        'milk': {"milk": "Gallon", "price": 2.59},
        'flour': {"flour": "Pound", "price": 3.49}
}

class Shopping_cart():

    def __init__(self):
        pass

    def add_item(self):
        user_cart = []
        user_input = raw_input("What do you want to add?\n")
        if user_input == 'eggs':
                choice_01 = (food_dict["eggs"])
                user_cart.append(choice_01)
                print "You\'ve added {}".format(user_cart)
                self.menu()
        elif user_input == 'milk':
                choice_02 = (food_dict["milk"])
                user_cart.append(choice_02)
                print in_cart
                self.menu()
        elif user_input == 'flour':
                choice_03 = (food_dict["flour"])
                user_cart.append(choice_03)
                print in_cart
                self.menu()
            

    def menu(self):
        choice = raw_input("Would you like to check out or continue?: ")
        if choice == "check out":

            pass
        else:
            self.add_item()
            pass
        pass



    def remove_item(self):
        pass
    def view_cart(self):
        pass


shopping = Shopping_cart()
print "Choose your item!"
time.sleep(.5)
for key in food_dict:
    print key

shopping.add_item()