def remove_dups_using_dictionaries(my_list):
    seen = dict()  # seen is a dict
    new_list = []  # new_list is a list
    for item in my_list:  # my_list is a list
        if item not in seen:  # seen is a dict
            new_list.append(item)
            seen[item] = True
    return new_list


def remove_dups_using_sets(my_list):
    seen = set()  # seen is a set
    new_list = []  # new_list is a list
    for item in my_list:  # my_list is a list
        if item not in seen:  # seen is a set
            new_list.append(item)
            seen.add(item)
    return new_list
