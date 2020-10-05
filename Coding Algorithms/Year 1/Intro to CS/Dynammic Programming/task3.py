import timeit
from itertools import product
import random
import numpy as np

def bitlists(n):
    return list(product([0,1],repeat = n))

def brute_force_knapsack(values,weights,capacity):
    def is_feasible(subset):
        weight = 0
        for i in range(len(subset)):
            if subset[i] == 1:
                weight += weights[i]
        return weight <= capacity

    def names(sol):
        solution = []
        for  i in range(len(sol)):
            if sol[i] == 1:
                solution.append(values[i])
        return solution

    def value(subset):
        total = 0
        for i in range(len(subset)):
            total += subset[i]
        return total

    all = bitlists(len(values))
    feasible = []
    for sol in all:
        if is_feasible(sol):
            feasible +=[names(sol)]

    opt = feasible[0]
    for sol in feasible:
        if value(sol) > value(opt):
            opt = sol

    return opt



class Item:
    def __init__(self, value = 0, weight = 0):
        assert type(weight) == int
        self.value = value
        self.weight = weight

    def __str__(self):
        return '(v = {}: w = {})'.format(self.value, self.weight)

    def __repr__(self):
        return str(self)

def knapsack_value(list_of_items, knapsack_capacity):
    assert len(list_of_items) > 0, "No items"
    assert knapsack_capacity > 0, "No space to store anything?"
    assert type(knapsack_capacity) == int

    table = np.zeros(shape=(len(list_of_items)+1, knapsack_capacity + 1))

    for i, item in enumerate(list_of_items, start=1):
        for j in range(1, knapsack_capacity+1):
            if item.weight > j:
                table[i,j] = table[i-1, j]
            else:
                table[i,j] = max(table[i-1,j], item.value + table[i-1, j - item.weight])

    return table[-1][-1]


def who_is_faster():


    random.seed()  # initialise the random generator

    random_number = random.randint(200, 1000)
    random_number2 = random.randint(1,20)
    values = []
    weights = []
    for i in range (6):
        values.append(random_number)
        weights.append(random_number2)


    start = timeit.default_timer()  # start the timer

    brute_force_knapsack(values, weights, 20)

    # i stop the timer here bcs i wanna time how long does it take to create a list of 100 list
    # (eg 2^2, list size = 4)
    taken1 = (timeit.default_timer() - start)

    itemList = []
    item = Item(random_number, random_number2)
    itemList.append(item)
    item = Item(random_number, random_number2)
    itemList.append(item)
    item = Item(random_number, random_number2)
    itemList.append(item)
    item = Item(random_number, random_number2)
    itemList.append(item)
    item = Item(random_number, random_number2)
    itemList.append(item)
    item = Item(random_number, random_number2)
    itemList.append(item)
    # i start it again to find the time taken to sort the list
    start = timeit.default_timer()

    knapsack_value(itemList, 20)

    # i stop the timer here again to get the time taken to find the sort the list
    taken2 = (timeit.default_timer() - start)

    print(taken1)
    print(taken2)


who_is_faster()