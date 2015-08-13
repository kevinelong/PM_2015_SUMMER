my_list = ["Abbie", "John", "Mollie"]

def list_names(my_list):
    if len(my_list) == 1:
        return my_list[0]
    elif len(my_list) == 2:
        my_string = " and ".join(my_list)
        return my_string
    else:
        len(my_list) == ""
    # elif
    #     my_string = ", ".join(my_list)
    # output = my_string


print list_names(my_list)







# def list_to_string():
#     output = ""
#     for x in output:
#         if x in output:
#             output.append(add(','))
#             return output
# print list_to_string(my_list)