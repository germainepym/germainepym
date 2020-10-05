def text_justification(text, width):
    memo = [None] * len(text)
    for i in range(len(memo)):
        memo[i] = [None] * len(text) # creating an empty list (i and j)


    for j in range(len(text)):
        if len(text[j]) <= width:
            total = (width - len(text[j]) )**3
            memo[j][j] = total # finding the cost of the empty spaces

        if j < 4:
            join = text[j] + ' ' + text[j+1] # concatenating the text together

            if len(join) <= width:
                total = (width - len(join))**3
                memo[j][j + 1] = total # find the cost of empty spaces next to the founded one

    cost = [None] * len(text)
    arrange = [None] * len(text)

    i = len(text)-1
    j = len(text)-1

    for a in range(len(text)):
        if memo[i][j] is not None:
            cost[i] = memo[i][j] # if the value in the table is not None, the last index in cost is the value from the table
            arrange[i] = j + 1
            i -= 1
        else:
            while memo[i][j-1] is None:
                j -= 1
            opt = memo[i][j-1] + cost[j]
            smallest = j

            while j > i+1: # checks if the supposed minimum value is minimum or not if not replace
                j -= 1
                if (memo[i][j-1] + cost[j]) < opt:
                    opt = memo[i][j-1] + cost[j]
                    smallest = j
            cost[i] = opt # it is replaced here
            arrange[i] = smallest
            i -= 1
            j = len(text) - 1

    i = 0
    j = arrange[0]
    newlist = []
    while True:
        line = ''
        for characters in text[i:j]:
            line += (characters + ' ')
        newlist.append(line) # appending the characters into a new list according to arrange list

        if j == len(text):
            break

        i = j
        j = arrange[i]

    for i in range(len(newlist)): # printing the characters
        print(newlist[i])

    print(cost[0])


text_justification(['Tushar', 'Roy', 'Likes', 'to', 'Code'], 10)

