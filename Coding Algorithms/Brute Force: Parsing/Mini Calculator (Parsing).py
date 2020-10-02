#Germaine Pok Yi Min
# ID: 29792802
#Task 2 :Calculator

from math import pow

def tokenization(expr):


    lst = []
    a = [i for i in expr]
    opr = ["+", "-", "*", "/", "^", "(", ")"]
    isItANumber = []
    numbers = ''
    n = 0
    for i in range(len(a)):
        if a[i] in opr:                     # if the element is in opr
            if numbers != '':               #if numbers is not null
                lst.append(numbers)                 
                isItANumber.append(True)    # used as a reference to convert the string to float
                numbers = ''                # then empty the number
            lst.append(a[i])                # if number is null, append the opr to the list
            isItANumber.append(False)       # used as a reference to convert the string to float
        else:
            if a[i] != ' ':                 # if element is not in opr
                numbers += a[i]             # concatenate the string to number
                if i == len(a)-1 and numbers != '':  #checking if it is the last index
                    lst.append(a[i])        
                    isItANumber.append(True)
    for i in range(len(lst)):               # according to isItANumber , if its true, it will covert the number in the lst to a float
        if isItANumber[i]:
            lst[i] = float(lst[i])

    return lst

#print(tokenization(" 3.14 + 6 * 2 ^ 2 * 2 - 1"))



def has_precedence(op1, op2):  #higher precedence =true
    
    low_precedence = ["+", "-"] 
    precedence = ["*", "/" ]
    high_precedence = ["^"]

    

    if op1 in precedence and op2 in low_precedence:
        return True
    elif op1 in high_precedence and op2 in low_precedence:
        return True
    elif op1 in high_precedence and op2 in precedence:
        return True
    elif op1 in low_precedence and op2 in precedence:
        return False
    elif op1 in low_precedence and op2 in high_precedence:
        return False
    elif op1 in precedence and op2 in high_precedence:
        return False
    elif op1 in low_precedence and op2 in low_precedence:
        return False
    elif op1 in precedence and op2 in precedence:
        return False
    elif op1 in high_precedence and op2 in high_precedence:
        return False
    

##print(has_precedence("*", "*"))

def simple_evaluation(token):
    
    opr = ["+", "-", "*", "/", "^" ]

    def evaluating(no1, no2, opr):
        if opr == "^":
            return float(no1**no2)
        elif opr == "-":
            return float(no1-no2)
        elif opr == "+":
            return float(no1+no2)
        elif opr == "/":
            return float(no1/no2)
        else:                                  
            return float(no1*no2)
    
    while len(token) != 1:
        operator = []
        for i in range(len(token)):
            if token[i] in opr:
                operator.append(token[i])                    
        

        current_operator = operator[0]
        
        for i in range(1,len(operator)):    
            if has_precedence(current_operator,operator[i]) == False:               # if my current operator(the first element of the index) is a higher precedence, it stays as the current operator
                if has_precedence(operator[i], current_operator) == True:           # if its false(not higher precedence), check if its in the same precedence category, if it is current operator stays the same
                    current_operator = operator[i]                                  # if condition is met replace current operator with the higher precedence
                    
        
        for r in range(len(token)):
            if token[r] == current_operator:                                        # find the current operator in the token's list
                value = evaluating(token[r-1], token[r+1], current_operator)        # calculate it
                token.pop(r-1)                                                      # pop out the elements that has been calculated at then 
                token.pop(r-1)
                token.pop(r-1)
                token.insert(r-1, value)                                            # insert the value calculated into the token list
                break

    return token[0]                     


#print(simple_evaluation(tokenization("2*8^2- 2 +6")))


def complex_evaluation(tokens):

    open1 = "("

    while open1 in tokens:

        for i in range(len(tokens)):
            for j in range(len(tokens)):
                if tokens[j] == open1:
                    opens_index = j
                elif tokens[j] == ")":
                    close_index = j
                    break


        a = tokens[opens_index+1: close_index]
        b = a[:]
        values = simple_evaluation(a)               # calculate the equation within the bracket using simple evaluation
        for j in range(len(b)+2):
            tokens.pop(opens_index)                       # pop out the equation in the token
        tokens.insert(opens_index,values)                 # insert the value calculated


    simple_evaluation(tokens)        
    return tokens[0]
    
#print(complex_evaluation(["(", 2, "-","(", 3, "+" ,7  , ")", ")", "*", 4, "^", "(", 2, "+", 1, ")"]))


def evaluation(expr):
    
    
    a = complex_evaluation(tokenization(expr))
    return a


#print(evaluation('(((2*(1+1))+2)^2)'))




