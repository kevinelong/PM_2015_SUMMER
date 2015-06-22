# define the input data
data_list = [
    {"id": 123, "name": "abc", "phone": "555-1111"},
    {"id": 456, "name": "def", "phone": "555-2222"}
]

# define the function that we will call later
def transform(data_list_input):
    data_dictionary_output = {}

    # DO YOUR WORK HERE
    # LOOP THROUGH ALL ITEMS IN data_list
    for item in data_list_input:

        # EXTRACT id from each extracted item
        id = item["id"]

        # CREATE an output item that is a new Dictionary/Object
        output_item = {}

        # COPY all properties except id from the original item into the new one

        # name = item["name"]
        # output_item["name"] = name

        # Previous two lines same as this
        # output_item["name"] = item["name"]

        #this loop does the same as the literal steps above but instead of just "name"
        # it does it for all keys in the object. e.g. "name", and "phone" and anything else added.
        for key in item.keys():
            if key != "id":
                output_item[key] = item[key]

        # ADD the new item to data_dictionary using the id as the key.
        data_dictionary_output[id] = output_item
        #this is the same as the line above without using the local
        # temporary variable named 'id'
        data_dictionary_output[item["id"]] = output_item

    # INCORRECT NAIVE ATTEMPT WITHOUT LOOPS OR VARIABLES
    # data_dictionary_output[data_list_input[0]["id"]] = {"name": data_list_input[0]["name"]}
    # data_dictionary_output[data_list_input[1]["id"]] = {"name": data_list_input[1]["name"]}

    return data_dictionary_output

# call the transform function passing in the data
data_dictionary_result = transform(data_list)

print(data_dictionary_result)