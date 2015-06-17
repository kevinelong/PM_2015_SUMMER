#remove duplicates from a list

#remove_dups([1, 2, 2, 3] returns [1, 2, 3]

def remove_dups(list):
    for x in list:
        for x in list:
            if list.count(x) > 1:
                list.remove(x)
            elif list.count(x) == 1:
                continue

    return list

l = [1, 1, 2, 1, 2, 3, 2, 2, 3, 2, 3, 1, 2, 4, 5, 4, 3, 2, 1]
print l
remove_dups(l)
print l
