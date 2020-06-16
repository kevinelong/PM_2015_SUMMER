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


def starts_with(haystack, needle):
    return needle == haystack[:len(needle)]

def contains(haystack, needle):
    return needle in haystack


def find_starts_with_in_dict(sought):
    matches = []
    for key_last_name, item in data.items():
        if starts_with(key_last_name, sought):
            matches.append(item)
    return matches

def find_contains_with_in_dict(sought):
    matches = []
    for key_last_name, item in data.items():
        if contains(key_last_name, sought):
            matches.append(item)
    return matches

def find_starts_with_any_in_list(sought):
    matches = []
    for item in data_list:
        full_name = item["name"]
        parts = full_name.split(" ")
        # print(parts)
        first_name = parts[0] #first part
        last_name = parts[1] #second part
        # print(last_name)
        if starts_with(last_name, sought) or starts_with(first_name, sought):
        # if starts_with(last_name, sought):
            matches.append(item)
    return matches


print(find_starts_with_in_dict("lo"))
print(find_contains_with_in_dict("o"))
print(find_starts_with_any_in_list("lo"))

