# start with a new empty dictionary, insert items by ide as new dictionary's in the empty dictionary
# input

data_list = [

    {"id": 123, "name": "abc"},
    {"id": 234, "name": "def"}
]

# answer should look similar to this:
# can you sort the data somehow?
# data_dictionary = {
#     123: {"name": "abc"},
#     234: {"name": "def"}
# }

# define function

def transform(data_list):
    data_dictionary = {}
    #do work here

    for n in data_list:
        ele = n["id"]
        ele2 = {"name": n["name"]}
        data_dictionary[ele] = ele2

    return data_dictionary

#call function

data_dictionary = transform(data_list)
print data_dictionary
