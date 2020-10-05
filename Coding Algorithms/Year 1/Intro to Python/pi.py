#Germaine Pok 29797802

#BASEL
from math import pi
from math import sqrt

print("Please enter precision value : ")        #user entering percision value
precision = float(input())
        
#function to calculate basel
def basel(precision):
    b_result = 0        
    b_n = 0     #terms for basel/counter
    b_x = 0     # first approximation for basel
    b_list = []
    while (abs(pi-b_x) > precision):  #to make the positive bcs negative cannot be bigger than positive
                                        #some values precision can be negative (diff x and pi) want positive difference so can compare
        b_n += 1
        b_result = (1/(b_n**2))
        b_list.append(b_result)
        b_x = sqrt((sum(b_list)) * 6)
    return(b_x, b_n)
    

print(basel(precision))


#WALLIS

#function to calculate wallis
def wallis(precision):
    w_result = 1
    w_x = 0     #terms for wallis/counter
    w_n = 0     # first approximation for wallis
    w_y = pi - precision
    if (precision <= 0): 
        return (w_x, w_n)
    while (abs(pi-w_x) > precision):
        w_n += 1
        w_result = w_result*((2 * w_n) * (2 * w_n)) / ((2 * w_n - 1) * (2 * w_n + 1))
        w_x = w_result * 2
    return (w_x, w_n)
print(wallis(precision))


#TAYLOR

#function to calculate taylor
def taylor(precision):
    t_results = 1
    t_x = 0     #terms for taylor/counter
    t_n = 0     # first approximation for taylor
    t_denominator = 1
    isPositive = True
    if (precision <= 0):
        return (t_x, t_n)
    while (abs(pi-t_x) > precision):
        t_n += 1
        if (t_n > 1):
            t_denominator += 2
            if (isPositive):
                t_results += (1/t_denominator)
            else:
                t_results -= (1/t_denominator)
        t_x = 4 * t_results
        isPositive = not isPositive
    return (t_x, t_n)

print(taylor(precision))

#SPIGOT

#function to calculate spigot
def spigot(precision):
    s_results = 1
    s_x = 0     #terms for spigot/counter
    s_n = 0     # first approximation for spigot
    previousValue = 1
    s_denominator = 3
    if (precision <= 0):
        return (s_x, s_n)
    while (abs(pi - s_x) > precision):
        if (s_n >= 1):
            previousValue *= ((s_n)/s_denominator)
            s_results += previousValue
            s_denominator += 2
        s_n += 1
        s_x = 2 *s_results
    return (s_x, s_n)

print(spigot(precision))


algorithms = []

#entering algorithm eg. basel, spigot
print("Please enter algorithm : " )
algorithm = str(input())
algorithms = algorithm.split()
print(algorithms)

#function for race
def race(precision, algorithms):

    return_value = [ ]
    b = [ ]
    newReturn = [ ]

    for h in range(len(algorithms)):        
        if algorithms[h] == 'basel':
            return_value.append(basel(precision))
            
        elif algorithms[h] ==  'wallis':
            return_value.append(wallis(precision))
            
        elif algorithms[h] == 'taylor':
            return_value.append(taylor(precision))
            
        elif algorithms[h] == 'spigot':
            return_value.append(spigot(precision))

        
    for j in range(len(return_value)):      #to append the algorithms into a list
        newReturn.append(return_value[j])   #j = index of return_value and then append to newReturn
        alist = list(newReturn[j])          #tuple to list
        alist[0] = j + 1                    #converting the index(0) of alist to integer eg. 1
        b.append(alist)
    

    def min_index(b):   #finding minimum index of b list
    
        k=0
        for i in range(1, len(b)):
            if b[i][1] < b[k][1]:
                k=i
        return k

    def selection_sort(b):  #selection sort my b list
    
        for i in range(len(b)):
            j = min_index(b[i:]) + i
            b[i], b[j] = b[j], b[i]

    selection_sort(b)
    return b

print(race(precision, algorithms))
            
def print_results(race):
    for x in range(len(race)):
        print("Algorithm" , race[x][0], "finished in", race[x][1], "steps")

print_results(race(precision, algorithms))

    
