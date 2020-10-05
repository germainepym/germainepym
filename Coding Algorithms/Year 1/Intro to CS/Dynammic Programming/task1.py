count = 0
def fib(n):
    print('Fibonacci sequence without dynamic programming:')
    for i in range(1,(n+1)):
        print(fib_aux(i,0,1), count)


def fib_aux(n, blast, last):
    global count
    count += 1
    if n == 0:
        return blast
    else:
        return fib_aux(n-1, last, last+blast)

fib(8)

count2 = 0
def dp_Fib(n,array = []):
    while len(array) < n + 1:
        array.append(0)
    # base case
    global count2
    count2 += 1
    if n <= 1:
        return n
    # recursive case
    else:
        if array[n - 1] == 0:
            array[n - 1] = dp_Fib(n - 1)

        if array[n - 2] == 0:
            array[n - 2] = dp_Fib(n - 2)

        array[n] = array[n - 2] + array[n - 1]

    return array[n]


def array(n):
    array1 = [0 for _ in range(n+1)]
    print('Fibonacci sequence with dynamic programming:')
    for i in range(1, (n + 1)):
        print(dp_Fib(i, array1), count2)

array(8)


