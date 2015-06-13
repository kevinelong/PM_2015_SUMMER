data = {
    'long': {'name': 'kevin long'},
    'longfellow': {'name': 'kay longfellow'},
    'bob': {'name': 'billie bob'}
}


def starts_with(searched, sought):
    return sought == searched[:len(sought)]


def find_starts_with(sought):
    matches = []
    for key, item in data.items():
        # print(key, item)
        # if sought == key[:len(sought)]:
        if starts_with(key, sought):
            matches.append(item)
    return matches


print(find_starts_with("lo"))

