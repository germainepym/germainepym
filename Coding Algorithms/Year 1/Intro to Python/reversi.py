#Germaine Pok 29797802

import copy

# 0 = empty
# 1 = black
# 2 = white
# player1 = black
# player2 = white

def new_board():
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    return board

def print_board(board):
    
    board1 = []                 # converting the numbers to letters.. eg: 1 to B
    for row in board:
        board2 = []
        for g in row:
            if g == 1:
                g = "B"
            elif g == 2:
                g = "W"
            elif g == 0:
                g = " "
            board2.append(g)
        board1.append(board2)
    
    index = 0
    dashes = ['-', '-', '-', '-', '-', '-', '-', '-']
    boardIndexes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    while (index < len(board)):
        index += 1
        # joining my index : 1,2,3....
        print(index , " | " , " | ".join(str(item) for item in board1[index-1]))    # item is looping within the array    
        print("-  | " , " | ".join(dashes))
    print("   | " , " | ".join(boardIndexes))

#counting my scores
def score(board):
    index = 0
    white = 0
    black = 0
    while (index < len(board)):
        black += board[index].count(1)
        white += board[index].count(2)
        index += 1
    return (black, white)

print_board(new_board())
##print(score(new_board()))

#----My own function-----

# to check if the position entered is within the range of the board
def truecoordinates(a,b,c,d):
        if a >= 0 and a <= 7 and b >= 0 and b <= 7 and c >= -1 and c <= 1 and d >= -1 and d <= 1:
            return True
        else:
            return False

#------------------------

        
def enclosing(board, player, pos, direct):

    a = pos[0]  #assigning index(0) of position to a 
    b = pos[1]

    c = direct[0] # assigning index(0) of direction to b
    d = direct[1]
    

    if player == 1 and truecoordinates(a,b,c,d) == True:
        if board[a][b] == 0:                                                    # if position of board is not occupied, if its not occupied, add direction to postion to proceed to the neighbouring tile
            if truecoordinates(a+c,b+d,c,d) == True and board[a+c][b+d] == 2:   
                while True :
                    if board[a+c][b+d] == 2:                                    # if the neighbouring tile is occupied by the opponent, add direction to position again
                        a = a+c
                        b = b+d
                        if truecoordinates(a,b,c,d) == False:                   # if the position is not within range, return false
                            return False
                    elif board[a+c][b+d] == 1:                                  # if the next neighbouring tile is occupied by player itself, return True
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False


                
    elif player == 2 and truecoordinates(a,b,c,d) == True:                  #same as player 1
        if board[a][b] == 0:
            if board[a+c][b+d] == 1:
                while True :
                    if board[a+c][b+d] == 1:
                        a = a+c
                        b = b+d
                        if truecoordinates(a,b,c,d) == False:
                            return False
                    elif board[a+c][b+d] == 2:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False                
                            
print(enclosing(new_board(), 1, (4, 5), (0, -1)))

    
def valid_moves(board, player):
    # Returns position list of [a,b] that displays the valid moves for the given player on the board.
    validmoves = []
    direction = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]      #direction is needed to check each and every direction of the board
    for q in range(len(board)):
        for w in range(len(board)):
            pos = q,w
            for a in direction:
                if enclosing(board, player, pos, a) == True:
                    validmoves.append(pos)
    return validmoves
   
print(valid_moves(new_board(), 1))

def next_state(board,player,pos):
    pass
        
     
    
            
#idk why it doesnt work help 
string = str(input("Enter position : "))
def position(string):

    i = ["a", "b", "c", "d", "e", "f", "g", "h"]
    j = [ '1', '2', '3', '4', '5', '6', '7', '8' ]

    for a in i:
        if string[0] == a:
            c = i.index(a)
        else:
            return None
        
    for b in j:
        if string[1] == b:
            r = j.index(b)
        else:
            return None

    return (r,c)



        
