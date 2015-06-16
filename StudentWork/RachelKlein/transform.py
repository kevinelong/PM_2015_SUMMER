# Define the input data

data_list = [
    { "id": 123, "Name": "abc", "age": 23 },
    { "id": 234, "Name": "def", "color": "red" }
]

# Transform function

# def transform(data_list):
#     data_dictionary = {}
#     new_id = 0
#     for x in data_list:
#         new_id = x.get("id", 0)
#         output_item = {}
#         output_item["Name"] = x["Name"]
#         data_dictionary[new_id] = output_item

# Transform function with more flexibility, ability to pass in an identifier that
# becomes the new key with a value of all the other dictionaries

def transform_anything(data_list, identifier):
    data_dictionary = {}
    for x in data_list:
        all_keys = x.keys()
        output_item = {}
        for key in all_keys:
            if key != identifier:
                output_item[key] = x[key]
        data_dictionary[x[identifier]] = output_item
    return data_dictionary

# call the transform function passing in the data
data_dictionary = transform_anything(data_list, "Name")
print data_dictionary