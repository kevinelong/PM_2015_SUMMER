#Write a function that splits an array (first argument) into groups the length of size
# (second argument) and returns them as a multidimensional array.
def list_in_list(list, num):
    output = []
    while len(list) >= num:
        slice = list[:num]
        list = list[num:]
        output.append(slice)
    if len(list) > 0:
        output.append(list)
    return output

print list_in_list(['a', 'b', 'c', 'd', 'e'], 2)