import timeit
import csv
import random

def shaker_sort(a_list):

    '''
    This program is to sort the list from left to right then from right to left to produce a sorted list
    :param a_list:
    :return: a sorted list
    :precondition: the list must be a list of real numbers
    :complexity: best case: O(n) the list is already sorted
                 worse case: O(n^2) a list that is unsorted
    '''
    right = len(a_list)-1 # right = 5
    for left in range(right): # left loops through the list
        swapped = False
        for i in range(left,right): # range 0 - 5
            if a_list[i] > a_list[i+1]: # if the value in a list is bigger than the number to the right.
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i] # swap the values
                swapped = True

        right -= 1 # 1 is subtracted because the most right side of the list is already sorted
        if not swapped: #if swapped is True then it wont go to break
            break

        for a in range (right, left, -1): # the list goes backwards
            if a_list[a] < a_list[a-1]: # if the value of the left is bigger than the value to the right
                a_list[a], a_list[a - 1] = a_list[a - 1], a_list[a] # swap the values
                swapped = True

        if not swapped: #if swapped is True then it wont go to break
            break

    return a_list

print(shaker_sort([3,4,7,5,2,1]))

def table_time_shaker_sort():
    '''
    This program records the time taken to generate a list of random numbers and time taken for it to be sorted by the
    shaker sort. It also records the time taken for a sorted list and revered list to be sorted through the shaker sort.
     The results is then recorded in a csv file called output_ex3.csv
    :return: csv file
    :precondition: none
    :complexity: best case: O(n) the list is already sorted
                 worse case: O(n^2) a list that is unsorted
    '''

    with open('output_ex3.csv', 'w') as openFile: # create csv file
        writer = csv.writer(openFile)
        random.seed()  #initialise the random generator
        sorted_list = []


        for i in range(1,11): #bcs 2^10 is 1026
            a_list = []
            sorted_list = []
            start = timeit.default_timer() #start the timer

            for a in range(1 << i): #<< =2^i * 1

                random_number = random.random() # generate random numbers
                a_list.append(random_number) # append the random numbers into the list

            for u in range(1,a): #stops when a, which is the n reaches 1026
                sorted_list.append(u)  # append into sorted list

            reversed_list = sorted_list[::-1] #reverse the sorted list
            #i stop the timer here bcs i wanna time how long does it take to create a list of random numbers
            # (eg 2^2, list size = 4)
            taken1 = (timeit.default_timer() - start)

            # i start it again to find the time taken to sort the list
            start = timeit.default_timer()
            shaker_sort(a_list) # call shaker_sort
            # i stop the timer here again to get the time taken to find the sort the list
            taken2 = (timeit.default_timer() - start)

            # i start it again to find the time taken to sort the sorted list
            start = timeit.default_timer()
            shaker_sort(sorted_list)
            # i stop the timer here again to get the time taken to find the sort the sorted list
            taken3 = (timeit.default_timer() - start)

            # i start it again to find the time taken to sort the revered list
            start = timeit.default_timer()
            shaker_sort(reversed_list)
            # i stop the timer here again to get the time taken to find the sort the reversed list
            taken4 = (timeit.default_timer() - start)

            #write the data in the csv file
            writer.writerow([1 << i, taken1, taken2, taken3, taken4])

table_time_shaker_sort()

def table_avg_time_shaker_sort():
    '''
    This program records the time it takes to generate a list of 100 list and the time taken for it to be sorted thorough
    the shaker sort. The results is then recorded in a csv file called output_ex3_avg.csv
    :return: csv file
    :precondition: none
    :complexity: best case: O(n) the list is already sorted
                 worse case: O(n^2) a list that is unsorted
    '''

    with open('output_ex3_avg.csv', 'w') as openFile: # create csv file
        writer = csv.writer(openFile)
        random.seed()  #initialise the random generator

        for i in range(1,11): #bcs 2^10 is 1026

            start = timeit.default_timer() #start the timer

            for a in range(1 << i): #<< =2^i * 1
                b_list = []
                for r in range(100): # generates 100 lists, then append the 100 lists in a list
                    a_list = []
                    for k in range(random_number): # for the list of the list

                        random_number2 = random.random() # generate random numbers
                        a_list.append(random_number2) # append the random numbers into the list
                    b_list.append(a_list) # append list in list

                # i stop the timer here bcs i wanna time how long does it take to create a list of 100 list
                # (eg 2^2, list size = 4)
                taken1 = (timeit.default_timer() - start)

            # i start it again to find the time taken to sort the list
            start = timeit.default_timer()
            for j in b_list:
                shaker_sort(j) # call shaker_sort
            # i stop the timer here again to get the time taken to find the sort the list
            taken2 = (timeit.default_timer() - start)

            #write the data in the csv file
            writer.writerow([1 << i, taken1, taken2])

table_avg_time_shaker_sort()
