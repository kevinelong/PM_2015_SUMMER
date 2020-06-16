# data_list = [
#     {"id": 123, "name": "abc"},
#     {"id": 234, "name": "Aef"}
# ]
#
#
# def transform(data_input):
#     data_output = {}
#
#     for item in data_input:
#         # store item id in variable id
#         id = item["id"]
#         # create variable output that stores an empty list
#         output = {}
#         # for loop using key method, using item keys
#         for key in item.keys():
#             # if key doesn't equal id start go back to beginning of for loop
#             if key != "id":
#                 # create variable called value that stores item[key]
#                 value = item[key]
#                 # create variable output[key] that stores above variable
#                 output[key] = value
#         # create variable data_output[id] to store output variable
#         data_output[id] = output
#
#     return data_output
#
# print(transform(data_list))










data_list = [
    {"id": 123, "name": "abc"},
    {"id": 234, "name": "Aef"}
]


def transform(data_input):
    data_output = {}

    for item in data_input:
        id = item["id"]
        output = {}
        for key in item.keys():


    return data_output

print(transform(data_list))