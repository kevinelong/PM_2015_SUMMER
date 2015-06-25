# write a function that given a list will return True if all the integers in the list are in a numeric
# range with no missing numbers. If not, raise a custom exception
# Given [1, 2, 3, 4] returns True
# Given [2, 3, 4] returns True
# Given [4, 6, 5, 2, 3] returns True
# Given [1, 4, 7] raises and Exception
# bonus empty list
# write unit tests, neatly handle case when something that is not a list is passed to your function,
# if the list passed contains something other than an integer raise a custom exception

def range_check(my_list):

    counter = 1
    # while counter < len(my_list):
    result_list = []
    for i in my_list:
        if counter == len(my_list):
            break
        if i + 1 == my_list[counter]:
            result_list.append(1)
        else:
            result_list.append(-1)
        if counter < len(my_list):
            counter += 1
        else:
            break

    for i in result_list:
        result = 0
        result += i
    if result > 0:
        print "Sequence detected!"
    elif result < 0:
        print "No sequence detected"


list_a = [1, 2, 3, 4]
list_b = [2, 3, 4]
list_c = [4, 6, 5, 2, 3]
list_d = [1, 4, 7]

range_check(list_a)
range_check(list_b)
range_check(list_c)
range_check(list_d)

# UNIT TEST
def test_exceptions():
    my_list = [1, 2, 3, 4]
    assert(my_list == [1, 2, 3, 4])  # assert is backwards to what i think, it only raises asserts on FALSE
    my_list = [2, 3, 4]
    assert(my_list == [2, 3, 4])
    my_list = [4, 6, 5, 2, 3]
    assert (my_list == [4, 6, 5, 2, 3])
    my_list = [1, 4, 7]
    assert (my_list == [2, 3, 4])

# test_exceptions()


# failed attempts:
    # test_list = []
    # results_list = []
    # for i in my_list:
    #     test_list.append(my_list[i] + 1)
    # for i in my_list:
    #     if my_list[i] + 1 == test_list[i]:
    #         print 'True'



    # for i in my_list:
    #     a = i
    #     a += 1
    #     b = len(my_list)
    #     while a <= len(my_list):
    #         test_a = my_list[i] + 1
    #         test_b = my_list[a]
    #         if (test_a == test_b ) or (my_list[i] - 1 == my_list[a]):
    #             print "sequence detected!"
    #         # elif my_list[i] - 1 == my_list[a]:
    #         #     print "sequence detected!"
    #         elif a > len(my_list):
    #             break
    #         a += 1




