import numpy as np

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def dp_knapsack(itemList, capacity):
    assert len(itemList) > 0, "No items"
    assert type(capacity) == int
    assert capacity > 0, "No space to store anything?"

    memo = [None] * (len(itemList) + 1)
    for j in range(len(memo)):
        memo[j] = [0] * (capacity + 1)

    i = 1
    for item in itemList:
        for j in range(1, (capacity + 1)):
            if item.weight > j:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i - 1][j], item.value + memo[i - 1][j - item.weight])
        i += 1
    print('Items associated with optimum value: ')
    print(associated_items(capacity, memo), '\n')

    print('The optimum value')
    return memo[-1][-1]


def associated_items(capacity, memo):

    i = len(itemList)
    j = capacity

    pointer = memo[-1][ -1]
    items = []

    while i >= 1:
        if memo[i - 1][ j] == pointer:
            i -= 1
        else:
            items.append(i)
            pointer = memo[i - 1][ j]
            i -= 1
            while j >= 1:
                if memo[i][j - 1] == pointer:
                    j -= 1
                else:
                    break

        if j == 0:
            break

    return items

itemList=[]
item = Item(4000, 20)
itemList.append(item)
item = Item(3500, 10)
itemList.append(item)
item = Item(1800, 9)
itemList.append(item)
item = Item(400, 4)
itemList.append(item)
item = Item(1000, 2)
itemList.append(item)
item = Item(200, 1)
itemList.append(item)

print(dp_knapsack(itemList, 20))
#associated_item(itemList)