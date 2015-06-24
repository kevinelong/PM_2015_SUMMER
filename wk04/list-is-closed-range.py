def is_a_range(my_list):
    if not isinstance(my_list, list):
        raise IWantedAListException('{} is not a list!'.format(my_list))
    elif not is_only_integers(my_list):
        # make sure all elements in my_list are integers
        raise IWantedOnlyIntegersException(
            'There are things other than integers in the '
            'list {}'.format(my_list))
    elif not len(my_list):
        # this is an empty list
        return True

    minimum = min(my_list)
    maximum = max(my_list)

    my_set = set(my_list)  # increases speed when searching
    for num in xrange(minimum + 1, maximum):
        if num not in my_set:
            raise ItsNotThereException(
                'The number {} is not in the list {}'.format(
                    num, my_list))

    return True


def is_only_integers(my_list):
    for element in my_list:
        if not isinstance(element, int):
            return False
    return True


class ItsNotThereException(Exception):
    """
    Custom exception for when something should be there but is not
    """


class IWantedAListException(Exception):
    """
    An excpetion when a list was expected but not gotten
    """


class IWantedOnlyIntegersException(Exception):
    """
    An excpetion where something in something is not an integer
    """


def test_is_a_range():
    assert(is_a_range([1, 2, 3]))
    assert(is_a_range([2, 3, 4]))
    assert(is_a_range([4, 3, 2]))
    assert(is_a_range([1, 3, 2]))
    assert(is_a_range([]))     # len 0
    assert(is_a_range([100]))  # len 1
    assert(is_a_range([-1, 0, 1]))

    try:
        assert(is_a_range([1, 2, 4]))
        assert(is_a_range([4, 3, 1]))
    except ItsNotThereException:
        # this is what we'd expect to happen
        pass
    else:
        raise AssertionError(
            '{} should have raised exception {}'.format(
                expression, exception_class))

    try:
        is_a_range('Reina')
        is_a_range(set([1, 2, 3]))
        is_a_range({})
    except IWantedAListException:
        # this is what we'd expect to happen
        pass
    else:
        raise AssertionError(
            'An exception should have been raised but was not')

    try:
        is_a_range(['a', 1, 2, 3])
        is_a_range([1, 5, 'a'])
    except IWantedOnlyIntegersException:
        # this is what we'd expect to happen
        pass
    else:
        raise AssertionError(
            'An exception should have been raised but was not')


if __name__ == '__main__':
    test_is_a_range()
