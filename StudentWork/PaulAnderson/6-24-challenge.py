nums = [1,2,3,4,5,6,7,8,9,10]
num_list = []

def exception_test(passed_list):
    for item in passed_list:
        num_list.append(int(item))
        while item in nums:
            print num_list
    print num_list
    # try:
    #     if item in nums:
    #         print num_list
    # except:
    #     raise



user_nums = raw_input('Enter a series of numbers between 1 and 10 >> ')
exception_test(user_nums)


def exceptions():
    assert([1, 2, 3, 4])
    assert([1, 2, 3])
    assert([1, 3, 4])
    assert([4, 5, 7, 2])