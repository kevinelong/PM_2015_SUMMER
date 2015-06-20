# import time
#
# my_list = [1, 2, 4, 5, 1, 6, 7, 1, 1, 1, 1, 1, 1, 2, 3, 5]
# my_set = {1, 2, 4, 5, 1, 6, 7, 1, 1, 1, 1, 1, 1, 2, 3, 5}
# # Takes a list, converts it to a set then back to a list
# def dup_remove(thing):
#     new_list = list(set(my_list))
#     return new_list
#
# # Takes a list, converts it to a set then back to a list.  Keeps order.
# def dup_remove_keep_order(list):
#     output = []
#     for item in list:
#         if item not in output:
#             output.append(item)
#     return output
#
#
# dup_remove(my_list)
# start = time.time()
# print dup_remove(my_list)
# end = time.time()
# print 'Time to execute: ', end - start
#
# dup_remove(my_set)
# start = time.time()
# print dup_remove(my_list)
# end = time.time()
# print 'Time to execute: ', end - start

# dup_remove_keep_order(my_dict)
# start = time.time()
# print dup_remove_keep_order(my_list)
# end = time.time()
# print 'Time to execute: ', end - start

# Write a function that test if a number is even

# def even_num(num):
#     if num % 2:
#         return False
#     return True
#
# print even_num(5)

# Write a function to turn a list of strings into a single word

list_to_convert = ["Reina", "Ollie", "Rachel", "Paul", "Ryan", "Anderson"]

# def new_string(convert):
#     my_string = ""
#     for item in convert:
#         if item == convert[-1] and len(convert) > 1:
#             my_string = my_string + ' and ' + item
#         elif item == convert[0]:
#             my_string = item
#         else:
#             my_string = my_string + ", " + item
#     print my_string


# pop off the last item and store it in a variable
# check to see if list has content
# join the list items in a variable seperated by commas
# return a concat of the variables seperated by 'and'
def new_string(convert):
    last_item = convert.pop()
    if len(convert) > 0:
        remainder = ", ".join(convert)
        return remainder + ' and ' + last_item
    else:
        return convert

print new_string(list_to_convert)




