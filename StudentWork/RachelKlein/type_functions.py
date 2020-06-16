import time

my_list = [2, 4, 5, 6, 2, 3, 4, 6, 6, 8, 1, 2, 100, 12]


def remove_dups(list_o_stuff):
    my_set = set()
    my_set = set(list_o_stuff)
    new_list = list(my_set)
    return new_list


def remove_dups_preserve_order(list_o_stuff):
    new_list = []
    for item in list_o_stuff:
        if item not in new_list:
            new_list.append(item)
    return new_list


def remove_dups_preserve_order_faster(list_o_stuff):
    my_set = set()
    new_list = []
    for item in list_o_stuff:
        if item not in my_set:
            my_set.add(item)
            new_list.append(item)
    return new_list


start = time.time()
remove_dups(my_list)
end = time.time()
print 'Time to execute: ', end - start
print remove_dups(my_list)

start = time.time()
remove_dups_preserve_order(my_list)
end = time.time()
print 'Time to execute: ', end - start
print remove_dups_preserve_order(my_list)

start = time.time()
remove_dups_preserve_order_faster(my_list)
end = time.time()
print 'Time to execute: ', end - start
print remove_dups_preserve_order_faster(my_list)
