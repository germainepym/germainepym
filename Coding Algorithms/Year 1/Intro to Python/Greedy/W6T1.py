#workshop 6 task 1

##def greedy_knapsack(values, weights, capacity):
##    n = len(values)
##    items = range(n)
##    def score(i): return values[i]
##    items = sorted(range(n), key=score, reverse=True)   #purpose of key: to optimize value
##    sel, value, weight = [], 0, 0
##    
##    for i in items:
##        if weight + weights[i] <= capacity:
##            sel += [i]
##            weight += weights[i]
##            value += values[i]
##    return sel, value, weight
##
##def process_file(filename):
##    weights = []
##    values = []
##    f1 = open(filename,'r')
##    for line in f1:
##        line_w = line.strip(' ').split('kg')
##        line_v = line.strip('\n').split('$')
##        weights.append(line_w[0])
##        values.append(line_v[1])
##        
##    for i in range(len(weights)):
##        weights[i] = int(weights[i])
##    for i in range(len(values)):
##        values[i] = int(values[i])
##    return weights, values
##
###items.txt
##
##filename = str(input('Plaese enter file name with item details: '))
##capacity = int(input('Please enter the capacity of the knapsack: '))
##weights, values = process_file(filename)
##sel, value, weight = greedy_knapsack(values, weights, capacity)
##print('items: ' , sel, '\nvalue: ', str(value) + '$')

#2
amount = int(input("What is the amount? "))
def greedy_algorithm(amount,denoms):
    n = len(denoms)
    items = sorted(range(n),reverse=True)
    result_list = [0 for i in range(len(denoms))]
    total = 0
    while total!=amount:
        for i in items:
            if total+denoms[i]<=amount:
                total+=denoms[i]
                result_list[i]+=1
    return result_list
print(greedy_algorithm(amount,[1,7,13]))
            
