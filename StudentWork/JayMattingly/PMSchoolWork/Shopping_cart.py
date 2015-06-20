food_dict = {
        'poultry': {"eggs": "Dozen", "price": 1.99},
        'dairy': {"milk": "Gallon", "price": 2.59},
        'dry': {"flour": "Pound", "price": 3.49}
}

class Shopping_cart():

    def __init__(self):
        pass

    def add_item(self):
        user_input = []
        user_input = raw_input("What do you want to add?\n")
        if user_input == 'eggs':
            choice_01 = (food_dict["poultry"])
        elif user_input == 'dairy':
            choice_02 = (food_dict["dairy"])
        elif user_input == 'dry':
            choice_03 = (food_dict["dry"])

        elif user_input == '3':
            pass
            




    def remove_item(self):
        pass
    def view_cart(self):
        pass

shopping = Shopping_cart()

shopping.add_item()