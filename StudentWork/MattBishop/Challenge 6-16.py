# removing duplicates in a list by converting to a set then back to a list
mylist = [1, 2, 3, 4, 5, 1, 3]
mylist = list(set(mylist))

# same exercise, but one that retains order of list
def remove_dups(list):
    output = []
    for item in list:
        if item not in output:
            output.append(item)
    return output

print remove_dups([1, 2, 3, 4, 5, 6, 7, 2, 5, 99, 2, 87, 55, 1])
