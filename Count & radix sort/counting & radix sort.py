# import libraries
import random
import timeit
import math
import matplotlib.pyplot as plt
import numpy as np

def radix_sort(num_list, base):
    """
    Function that sorts a list of numbers according to the base
    Precondition: n numbers in the list range 1..k where k is the biggest value in the list
    Arguments:          num_list = list of numbers to be sorted
                        base = list is sorted according to the base

    Time complexity:    Best case : O((n+b)m) where n is the size of the list, b is the base and m is the number
                                    of digit in the largest number of the input list


                        Worst case : O((n+b)m) where n is the size of the list, b is the base and m is the number
                                    of digit in the largest number of the input list

    Space complexity: O(kn) where k is the base and n is the number of digit in the largest number of the num_list
    Aux space complexity: O(n) where n is the number of elements in num_list

    Return: num_list (where the list will be sorted in ascending order)
    """
    # find the longest digit based on the base
    if len(num_list) == 0:
        return num_list
    else:
        biggest = num_list[0]
        for item in num_list:
            if item > biggest:
                biggest = item

    if biggest%10 == 0: #if multiple of 10 round up
        maximum = int(math.ceil(math.log(biggest, base) + 1))
    else: #round down
        maximum = int(math.floor(math.log(biggest, base) + 1))


    # perform radix sort column by column
    for col in range(maximum):
        if col == 0:
            num_list = counting_sort_stable(num_list, base, col)
        else:
            num_list = counting_sort_stable(num_list, base, col)

    return num_list

def counting_sort_stable(input_list,base,col):
    """
    Function that sorts according to their columns
    Precondition: n numbers in the list range 1..k where k is the biggest value in the list
    Arguments:          input_list = list of numbers to be sorted
                        base = list is sorted according to the base
                        col = which column of digit is being sorted

    Time complexity:    Best case : O(n+m) where n is the input list and m is the count array
                        Worst case :  O(n+m) where n is the input list and m is the count array

    Space complexity: O(n+m+k) where n is the input_list, m is the count array and k is the sorted_list array
    Aux space complexity: O(n+m) where n is the count array and m is the sorted_list array

    Return: sorted_list (which is a list sorted in ascending order according to the column)
    """
    sorted_list = []
    # find maximum
    for i in range(len(input_list)):
        sorted_list.append(get_digit(input_list[i],base,col))

    max_item = sorted_list[0]
    for item in sorted_list:
        if item > max_item:
            max_item = item

    # initialise count array
    count = [None] * (max_item+1)
    for i in range(len(count)):
        count[i] = []
    for i in input_list:
        count[get_digit(i,base,col)].append(i)

    # update input array
    sorted_list = [None] * len(input_list)
    index = 0
    for i in range(len(count)):
        if len(count[i]) == 0:
            pass
        elif len(count[i]) >= 2:
            for j in range(len(count[i])):
                sorted_list[index] = count[i][j]
                index += 1
        else:
            sorted_list[index] = count[i][0]
            index +=1

    return sorted_list

def get_digit(number,base,col):
    """
   Function that 'converts' a number according to it's base
   Arguments :         number = This number is to be divided by base**col to obtain the 'column'
                       base = base of the radix sort
                       col = which column should be obtained

   Time complexity:    Best case : O(1)
                       Worst case : O(1)

   Space complexity: O(1)
   Aux space complexity: O(1)

   Return: digit
   """
    digit = ( number // (base ** col)) % base
    return digit

def time_radix_sort():
    """
    Function that time radix sort
    Time complexity:    Best case : O(kn(m+b)) where k is the number of digit in the largest number of the input list,
                                    n is the size of base_list, m size of the num_list and b is the base
                        Worst case : O(kn(m+b)) where k is the number of digit in the largest number of the input list,
                                     n is the size of base_list, m size of the num_list and b is the base

    Space complexity: O(n+m+k) where n is timing, m is time and k is num_list
    Aux space complexity: O(n+m+k) where n is timing, m is time and k is num_list

    Return: A list stating the time it took to sort random numbers according to the base
    """
    num_list = [random.randint(1,(2**64)-1) for _ in range(100000)]
    base_list = [2,10,4096,131072,262144,1000000,4194304,8388608,67108864]
    
    #store tuple of base and time
    base_time = []
    #store time each base takes to run radix sort
    time = []
    for base in base_list:
        # time the function only for the sorting itself
        # start timer
        start = timeit.default_timer()
        radix_sort(num_list, base)

        # end timer
        end = (timeit.default_timer() - start)
        base_time.append((base, end))
        time.append(end)

    #plotting the graph
    plt.scatter(base_list, time, color='k', s=25, alpha=0.5)
    plt.plot(base_list,time, '--')
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.xlabel('Base')
    plt.ylabel('Time(seconds)')
    plt.title('Time taken to sort a list by base')
    plt.show()

    return base_time

def radix_sort_strings(input_list):
    """
        Function that sorts a list of strings in a lexicographical order using radix sort
        Precondition: n number of strings in the list
        Arguments:          input_list = list of strings to be sorted

        Time complexity:    Best case : O(nm) where n is the size of the list and m is the number of characters
                                              in the longest string of the input list
                            Worst case : O(nm) where n is the size of the list and m is the number of characters
                                              in the longest string of the input list

        Space complexity: O(kn) where k is the base and m is the number of character in the largest word of the input_list
        Aux space complexity: O(n) where n is the number of elements in input_list

        Return: new_list (where the list of words will be sorted in lexicographical order)
        """
    #check the which string is the longest character
    if len(input_list) == 0:
        return input_list
    else:
        biggest = max(input_list, key=len)

    maximum = len(biggest)

    #perform counting sort
    for col in range(maximum):
        if col == 0:
            input_list = counting_sort_strings(input_list, col)
        else:
            input_list = counting_sort_strings(input_list, col)

    return input_list

def counting_sort_strings(input_list,col):
    """
      Function that sorts a list of strings according to columns
      Precondition: n numbers of strings in the list
      Arguments:          input_list = list of strings to be sorted
                          col = which column of character is being sorted

      Time complexity:    Best case : O(n+m) where n is the input list and m is the count array
                          Worst case :  O(n+m) where n is the input list and m is the count array

      Space complexity: O(n+m+k+l) where n is the input_list, m is the count array and k is the new_list array where
                        l is col_alpha list
      Aux space complexity: O(m+n+k) where m is the count array, n is the new_list array and k is col_alpha list

      Return: new_list (which is a list sorted in lexicographic order according to the column)
      """

    #sort the strings from the right, if the length of the word is shorter than the column, use the first word
    #appending characters of the words according to the column
    col_alpha = []
    for i in input_list:
        if len(i) > col:
            col_alpha.append(i[(len(i)-col)-1])
        else:
            col_alpha.append(i[0])

    #convert strings to integers
    new_list = []
    for i in range(len(col_alpha)):
        new_list.append(get_alpha(col_alpha[i]))

    #find maximum
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item

    # initialise count array
    count = [None] * (max_item + 1)
    for i in range(len(count)):
        count[i] = []

    counter = 0
    for i in input_list:
        count[get_alpha(col_alpha[counter])].append(i)
        counter += 1

    #update input array
    new_list = [None] * len(col_alpha)
    index = 0
    for i in range(len(count)):
        if len(count[i]) == 0:
            pass
        elif len(count[i]) >= 2:
            for j in range(len(count[i])):
                new_list[index] = count[i][j]
                index += 1
        else:
            new_list[index] = count[i][0]
            index += 1

    return new_list


def get_alpha(word):
    """
      Function that converts strings to numbers referring to ASCII
      Arguments :         word = This word is to be converted to a number

      Time complexity:    Best case : O(1)
                          Worst case : O(1)

      Space complexity: O(1)
      Aux space complexity: O(1)

      Return: number (the converted number of the alphabet)
      """
    number = ord(word)-97

    return number

def find_rotations(string_list, p):
    """
    Function that rotates a string given a p-rotation
    Arguments:          string_list = a list of strings
                        p = determine what kind of rotation to be carried out
    Time complexity:    Best case: O(nm): where n is the number of strings in the input list and m is the maximum number
                                          of letters in a word, among all words in the input list
                        Worst case: O(nm) where n is the number of strings in the input list and m is the maximum number
                                          of letters in a word, among all words in the input list

    Space complexity: O(n+m+k) where n is the string_list, m is new_list and k is rotated
    Aux space complexity: O(m+k) where m is new_list and k is rotated

    Return: rotated ( a list where the p-rotation of string_lists is also in string_list itself)
    """


    if len(string_list) == 0:
        return string_list

    # do the p rotations
    new_list = []

    #using circular queue to obtain the rotations
    for i in range(len(string_list)):
        if p == 0:
            new_list.append(string_list[i])
        else:
            a = p % len(string_list[i])
            first = string_list[i][0:a]
            second = string_list[i][a:]
            new_list.append(second + first)

    #checking which rotated string is present in the string_list
    new_list = string_list + new_list
    rotated = []
    new_list = radix_sort_strings(new_list)
    j = 0
    for i in range(len(new_list)):
        if i == (len(new_list)-1):
            pass
        elif new_list[i+1] == new_list[j]:
            if new_list[i + 1] in rotated:
                pass
            else:
                rotated.append(new_list[i + 1])
        else:
            new_list[i+1], new_list[j+1] = new_list[j+1], new_list[i+1] # swap
            j += 1

    #rotate back
    for i in range(len(rotated)):
        if p == 0:
            pass
        else:
            a = p % len(rotated[i])
            r_first = rotated[i][0:-a]
            r_second = rotated[i][-a:]
            rotated[i] = r_second + r_first

    return rotated

