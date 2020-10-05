#TASK6

##def transpose(a):
##    L1=[]
##    for x in range (len(a[0])):
##        L2=[]
##        for y in range (len(a)):
##            value=a[y][x]
##            L2.append(value)
##        L1.append(L2)
##    return L1
##
##print(transpose([[1,2],[3,4],[5,6]]))
##
################################################################################
##
##matrix=[[34,1,77],
##       [2,14,8],
##       [3,17,11]]
##
##vector=[[6,8,1],
##        [9,27,5],
##        [2,43,31]]
##
##result=[[0,0,0],
##        [0,0,0],
##        [0,0,0]]
##
##def multiply (matrix,vector):
##    for i in range(len(matrix)):
##        for j in range(len(vector[0])):
##            for k in range(len(vector)):
##                result[i][j] += matrix[i][k] * vector[k][j]
##    return result
##print(multiply(matrix,vector))

##############################################################################

sum_nutri=[0 for x in range (7)]

cols = ["energy " , "water" , "protein" , "carbs" , "sugars" , "fat" , "fiber"] 

rows = ["apple", "orange" ,"broccoli" ,"beef" ,"lamb" ,"bread"]

nutr_vals = [[229 , 84.3 , 0.4 , 12.0 , 11.8 , 0.0 , 2.3] ,
             [186 , 84.3 , 1, 9.5 , 8.3 , 0.2 , 2.1] ,
             [124 , 89.6 , 3.2 , 2.0 , 2.0 , 0.1 , 4.1] ,
             [613 , 70, 22.8 , 0.2 , 0.0 , 6.0 , 0.0] ,
             [1057 , 60.2 , 18.6 , 0.0 , 0.0 , 20.2 , 0.0] ,
             [1446 , 37.6 , 8.4 , 43.5 , 1.5 , 2.6 , 6.9]]



for i in range (len(nutr_vals[0])):
    for x in nutr_vals:
        sum_nutri[i] += x[i]

print(sum_nutri)
