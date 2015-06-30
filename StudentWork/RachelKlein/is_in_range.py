# This method tests whether a list you feed it is a complete range with no missing values.

def is_in_range(int_list):
    this_list = sorted(int_list)
    if this_list == []:
        raise EmptyListException("That list is empty!")
    list_length = len(this_list)
    last_num = this_list[0]
    current_num = 0
    for num in this_list[1:list_length]:
        current_num = num
        if current_num == last_num + 1:
            last_num = num
        else:
            raise RangeException("Some values are missing from the range of this list.")
    return True


class EmptyListException(Exception):
    """ In case the user gives us an empty list """


class RangeException(Exception):
    """ When all the numbers in the list are not in range """


list1 = [2, 3, 4]
list2 = [11, 9, 10]


def is_in_range_test():
    assert is_in_range(list1) is True
    assert is_in_range(list2) is True


is_in_range_test()
