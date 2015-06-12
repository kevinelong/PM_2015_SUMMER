mylist = [
    {"id": 1, "name": "Mary", "age" : "49"},
    {"id": 2, "name": "Gerret", "age" : "56"}
]

def transform(mylist):
    mylist_dictionary = {}

    for item in mylist:

        id = item["id"]

        New_object = {}

        name = item["name"]

        New_object["name"] = name

       # New_object["name"] = item["name"]

        for key in item.keys():
            if key != "id":
                value = item[key]
                New_object[key] = value
                #New_object[key] = item[key]

        mylist_dictionary[id] = New_object

    return mylist_dictionary
Result = transform(mylist)

print Result