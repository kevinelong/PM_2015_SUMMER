# Define the input data

data_list = [
    { "id": 123, "Name": "abc" },
    { "id": 234, "Name": "def" }
]

# Transform function

def transform(data_list):
    data_dictionary = {}
    new_id = 0
    for x in data_list:
        new_id = x.get("id", 0)
        output_item = {}
        output_item["Name"] = x["Name"]
        data_dictionary[new_id] = output_item
    print data_dictionary

# call the transform function passing in the data
data_dictionary = transform(data_list)