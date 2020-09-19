def longest_oscillation(L):
    """
    A function that finds the longest oscillation given a list
    Arguments: L = a list of integers

    Time complexity: Best case: O(n) where n is the size of list L

                     Worse case: O(n) where n is the size of list L

    Space complexity: O(n+m) where n is list L and m is memo
    Aux space complexity: O(n) where n is memo and solution ( they are both dependant on the size of list L )

    Return: the number of oscillations and the position index of the oscillation in list L
    """
    if L is None:
        return 0, []

    memo = [-1] * (len(L) + 1)
    memo[0] = 0
    solution = []
    for i in range(len(L)):
        # when we reach the last element
        if i == len(L) - 1:
            if len(L) -1 == 0: # if there is only one element in the list L
                memo[i + 1] = memo[i] + 1

            elif L[i] < L[i-1]: # last element is a min/max point if the 2nd last element is bigger than the last
                memo[i + 1] = memo[i] + 1

            elif L[i] == L[i-1]: # if there it is a few constant at the back of the list
                if L[i] == L[i-2]: #if the the 3rd last element is the same as the last element
                    memo[i + 1] = memo[i]
                else:
                    memo[i+1] = memo[i] +1

            else:
                memo[i+1] = memo[i] +1
            break

        # the first value would be a minimum point
        if i == 0:
            memo[i+1] = memo[i] + 1

        else:
            # if the adjacent element is the same
            if L[i-1] == L[i]:
                # if oscillation is going upwards (/), memo is the same as the previous memo
                if L[i + 1] > L[i - 1] >= L[i - 2]: # L[i-1] < L[i+1](/) ,  L[i-1] >= L[i-2](/)
                    memo[i+1] = memo[i]

                # if oscillation changes, and goes downwards(\), then add one
                elif L[i-1] < L[i+1] and L[i-1] <= L[i-2]: # \
                    memo[i + 1] = memo[i] + 1

                #if L[i] == L[i+2], means that there is an oscillation but it wasn't stored in the memo
                elif L[i-2] < L[i-1]:
                    if L[i] >= L[i + 1]:
                        memo[i] = memo[i] + 1
                        memo[i + 1] = memo[i]

                # if L[i] == L[i + 1], means that there is an oscillation but it wasn't stored in the memo
                elif L[i - 2] > L[i-1]:
                    if L[i] <= L[i + 1]:
                        memo[i] = memo[i] + 1
                        memo[i + 1] = memo[i]

                #if it is constant, no changes
                else:
                    memo[i + 1] = memo[i]

            #  if the next element is bigger than the current element,
            elif L[i-1] < L[i]:

                # if the next element is bigger than the next next element, add one
                if L[i] > L[i+1]:
                    memo[i+1] = memo[i] +1

                # if not means that there is no oscillation
                else:
                    memo[i+1] = memo[i]

            # if the current element is bigger than the next element
            elif L[i-1] > L[i]:

                # if the next next element is bigger than the next element, add one
                if L[i] < L[i + 1]:
                    memo[i+1] = memo[i] +1

                # if not means that there is no oscillation
                else:
                    memo[i+1] = memo[i]

    for i in range(len(L)):
        if memo[i] == memo[i+1]: #if they are the same, means that the number of max/min point didn't increase,
            pass                 # hence its not a max/min point
        else:
           solution.append(i)


    return memo[-1],solution




def longest_walk(M):
    """
       A function that finds the longest walk given a matrix
       Arguments: M = a matrix of integers

       Time complexity: Best case: O(nm) where n is the row and m is the column

                        Worse case: O(nm) where n is the row and m is the column

       Space complexity: O(nm^2) where n is row of memo and m column of memo

       Aux space complexity: O(nm^2) where n is row of memo and m column of memo

       Return: the longest walk in the matrix and the path taken
       """

    if M is None:
        return 0,[]
    elif not M:
        return 0, []
    elif M == [[]]:
        return 0, []

    memo = [[0] * len(M[0]) for _ in range(len(M))]
    final = None
    save = None
    length = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            # if the memo is already filled means that a path has already been constructed
            if memo[i][j] == 0:
                final = navigate_path(i,j,M,memo)
                #ensure it is the longest path saved
                if length < len(final):
                    length = len(final)
                    save = final

    if length > len(final):
        final = save

    return len(final),final


def navigate_path(i, j, M, memo):
    """
           A function that navigates through the matrix to find the longest path
           Arguments: i = row of matrix
                      j = column of matrix
                      M = a matrix of integer
                      memo = 2D memoization

           Time complexity: Best case: O(n) where n is constant time of 8

                            Worse case: O(n) where n is constant time of 8

           Space complexity: O(nm^2) where n is row of memo and m column of memo

           Aux space complexity: O(nm^2) where n is row of memo and m column of memo

           Return: the longest path the current position of the selected number on the matrix can take
    """
    longest_path = None
    # right, left, up, down, diagonal
    for k in range(8):
        x = [0, +1, +1, +1, 0, -1, -1, -1]
        y = [+1, +1, 0, -1, -1, -1, 0, +1]

        direction_i = x[k]
        direction_j = y[k]
        # if the path have been visited before
        if memo[i][j] != 0:

            return memo[i][j]

       # if not visited yet,check if the direction is valid
        elif 0 <= i + direction_i < len(M) and 0 <= j + direction_j < len(M[i]):

            #check if the next step taken is the smallest one (+1)
            if M[i][j] > M[i+direction_i][j+direction_j]:

                # if its valid, enter recursion and continue on to that direction until the longest walk is found
                walk = navigate_path(i + direction_i, j + direction_j,M,memo)

                # after exiting the recursion, check if the current path is the longest path or not if it is, then
                #set it as the longest path
                if longest_path is None:
                    longest_path = walk
                elif len(walk) >= len(longest_path):
                    longest_path = walk

    if longest_path is None:
        final_path = [(i,j)]
        #store path in memo
        memo[i][j] = [(i,j)]
    else:
        final_path = longest_path + [(i, j)]
        #store path in memo
        memo[i][j] = longest_path + [(i, j)]


    return final_path
