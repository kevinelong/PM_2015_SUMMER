data_list = [
    {"id": 123, "name": "abc"},
    {"id": 234, "name": "Aef"}
]


def transform(data_list):
    data_dictionary = {}
    for item in data_list:
        data_dictionary[item.id] = item
    print d.keys()
    # return data_dictionary

transform(data_list)