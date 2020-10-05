import timeit
import csv
import random

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

def table_time_mean_items():

    '''
    This program is to record the time taken for to generate a list with random numbers and the time taken to find the
    mean of the list and then record the results in a csv file called output_ex2.csb
    :return: csv file
    :precondition: none
    :complexity: best case: O(1), where the list is empty
                 worse case: O(n), where n is the length of the list
    '''

    with open('output_ex2.csv', 'w') as openFile:
        writer = csv.writer(openFile)
        random.seed()
        a_list = []

        for i in range(1,13): #bcs 2^12 is 4096

            start = timeit.default_timer()

            for a in range(1 << i): #<< =2^i * 1

                random_number = random.random()
                a_list.append(random_number)

            #i stop the timer here bcs i wanna time how long does it take to create a list of random numbers (eg 2^2, list size = 4)
            taken1 = (timeit.default_timer() - start)

            # i start it again to find the time taken to find the mean
            start = timeit.default_timer()
            mean_items(a_list)
            # i stop the timer here again to get the time taken to find the mean of the list
            taken2 = (timeit.default_timer() - start)

            writer.writerow([1 << i, taken1, taken2])

table_time_mean_items()