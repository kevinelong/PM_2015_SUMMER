data = {
    'long': {'name': 'kevin long'},
    'longfellow': {'name': 'kay longfellow'},
    'bob': {'name': 'billie bob'}
}

data_list = [
    {'name': 'kevin long'},
    {'name': 'kay longfellow'},
    {'name': 'lonnie buckets'},
    {'name': 'billie bob'}
]


def starts_with(searched, sought):
    return sought == searched[:len(sought)]


def find_starts_with_in_dict(sought):
    matches = []
    for key, item in data.items():
        # print(key, item)
        # if sought == key[:len(sought)]:
        if starts_with(key, sought):
            matches.append(item)
    return matches

def find_starts_with_in_list(sought):
    matches = []
    for item in data_list:
        full_name = item["name"]
        parts = full_name.split(" ")
        print(parts)
        first_name = parts[0] #first part
        last_name = parts[1] #second part
        print(last_name)
        # if starts_with(last_name, sought) or starts_with(first_name, sought):
        if starts_with(last_name, sought):
            matches.append(item)
    return matches


print(find_starts_with_in_list("lo"))

