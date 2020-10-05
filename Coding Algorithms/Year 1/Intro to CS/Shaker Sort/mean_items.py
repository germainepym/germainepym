def mean_items(a_list):

    '''
    This program is to find the mean of the given list. If the list is empty, a message will pop up to inform the user
    :param a_list: input integers
    :return: mean of the summed values of the list
    :precondition: the list must be a list of real numbers
    :complexity: best case: O(1), where the list is empty
                 worse case: O(n), where n is the length of the list
    '''

    if a_list == []:
        raise ZeroDivisionError("The list is empty")

    eq = sum(a_list)/len(a_list)
    return eq

def test_mean_items():

    '''
    This program is test whether the function mean_items is working
    :precondition: none
    :return: none
    '''

    # testing the function mean_items
    assert mean_items([1,2,3,4,5]) == 3, "TEST FAILED"
    assert mean_items([3,5,8,3,6]) == 5, "TEST FAILED"
    print("TEST PASSED")

    # testing if the list is empty, if empty then pass
    try:
        mean_items([])
        print("TEST FAILED")
    except ZeroDivisionError:
        print("TEST PASSED")

test_mean_items()