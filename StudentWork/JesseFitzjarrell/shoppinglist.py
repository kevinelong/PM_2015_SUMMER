__author__ = 'lenny'
"""
Shopping list example from Python Treehouse track
Jesse Fitajarrell
7-8-15

"""

shopping_list = list()

print ("What should we pick up at the store?")
print ("Enter 'Done' to stop adding items")

while True:
    new_item = input(">")

    if new_item == "DONE":
        break


    shopping_list.append(new_item)
    print ("Added: list has {} items".format(len(shopping_list)))
        continue
    print("Here's your list:")

    for item in shopping_list:
