from unsorted_list import List


class Tour:

    board_rows = 8
    board_cols = 8
    board_size = board_rows * board_cols
    
    def __init__(self):
        """
               this function creates the board and sets a starting position for the knight

               @param          none
               @return         none
               @pre            none
               @post           a list is created with (1,1) as the initial position of the knight
               @complexity     best case: O(1)
                               worse case: O(1)
        """
        # You may wish to add additional attributes to the object.
        self.moves = List(Tour.board_size)
        self.saved = 0
        self.moves.add_last( (1, 1) ) # Set a starting position

    def move_knight(self, row, col):
        """
                this function moves the knight to the entered position

               @param          row
               @param          col
               @return         none
               @pre            the total moves of the knight must be less than board size
               @post           the position of the knight is moved
               @complexity     best case: O(1)
                               worse case: O(1)
        """
        assert self.moves.length() < Tour.board_size
        self.moves.add_last( (row, col) )

    def show_tour(self):
        """
                this functions prints out the board and shows the player where the knight is and the knight's
                previous positions.

               @param          none
               @return         none
               @pre            none
               @post           a board that shows the knights current and previous positions.
               @complexity     best case: O(1)
                               worse case: O(1)
                """
        for r in range(1, Tour.board_rows+1):
            for c in range(1, Tour.board_cols+1):
                pos = self.moves.index( (r, c) )
                cell_char = '|_'
                if pos is not None:
                    if pos == self.moves.length()-1:
                        cell_char = '|K'
                    else:
                        cell_char = '|*'

                print(cell_char, end='')
            print('')

    def next_moves(self,pos):
        """
                this function returns a list of the next moves the player could make

                @param          pos
                @return         list of next possible moves
                @pre            position is checked if it is within the board
                @post           list of next possible moves is created
                @complexity     best case: O(n)     : the list is empty
                                worse case: O(n^2)  : the list is not empty
        """
        row, col = pos
        size = List(8)

        if row - 2 >= 1 and col - 1 >= 1:
            size.add_last((row - 2, col - 1 ))
        if row - 1 >= 1 and col - 2 >= 1:
            size.add_last((row - 1, col - 2))
        if row + 1 <= self.board_rows and col - 2 >= 1:
            size.add_last((row + 1 , col - 2))
        if row + 2 <= self.board_rows and col - 1 >= 1:
            size.add_last((row + 2, col - 1))
        if row + 2 <= self.board_rows and col + 1 <= self.board_cols:
            size.add_last((row + 2, col + 1))
        if row + 1 <= self.board_rows and col + 2 <= self.board_cols:
            size.add_last((row + 1, col + 2))
        if row - 1 >= 1 and col + 2 <= self.board_cols:
            size.add_last((row - 1, col + 2))
        if row - 2 >= 1 and col + 1 <= self.board_cols:
            size.add_last((row - 2, col + 1))

        for i in range(self.moves.length()):
            if self.moves.get_item(i) is not None:
                for h in range(self.moves.length()):
                    if size.get_item(h) == self.moves.get_item(i):
                        size.delete_item(size.index(size.get_item(h)))

        return size

    def valid_moves(self,pos):
        """
                This function ensures if the moved entered by the player is valid or not

                      @param          pos
                      @return         true or false values
                      @pre            row and column of the desired position
                      @post           True if move is valid
                      @post           False if the move is not valid
                      @complexity     best case: O(n) : n is the number of possible moves
                                      worse case: O(n): n is the number of possible moves
        """
        position = self.moves.get_item(self.moves.length()-1)
        valid_pos = self.next_moves(position)
        valid = False

        for i in range(valid_pos.length()):
            if pos == valid_pos.get_item(i):
                row, col = pos
                self.move_knight(row, col)
                valid = True

        return valid

    def undo(self):
        """
                This function undo the latest move of the player to its previous position
                      @param          none
                      @return         none
                      @pre            the knight must be move at least one time
                      @post           the latest move of the knight is removed from the list
                      @complexity     best case: O(1)
                                      worse case: O(1)
        """

        if self.moves.length()  > 1:                   # if the length is more than 1
            self.moves.delete_item(self.moves.get_item(self.moves.length() -1))  #delete the latest 'move' in the list
            position = self.moves.get_item(self.moves.length() -1)               #index of the latest element in the list
            self.moves.delete_item(position)                     #delete the latest 'move' in the list
            row, col = position                                  #row, col = position(eg. (3,2))
            self.move_knight(row, col)                           #move the knight using move_knight
        elif self.moves.length()  <= 1:                # if the length less less or equals to 1
            print('The knight never moved')                      #tell the user that the knight never move, cannot undo

    def copy(self):
        """
                This function copies the current board

                      @param          none
                      @return         none
                      @pre            none
                      @post           an identical board is copied
                      @complexity     best case: O(n) : n is the length of the list
                                      worse case: O(n): n is the length of the list
        """
        self.saved = List(Tour.board_size)                  # saved is a list

        for i in range(self.moves.length()):
            self.saved.add_last(self.moves.get_item(i))     # append each value in moves into saved


    def set(self):
        """
                This function replaces the current board with a board that was copied previously
                      @param          none
                      @return         none
                      @pre            a copied board
                      @post           identical board that was copied previously
                      @complexity     best case: O(n) : n is the length of the list
                                      worse case: O(n): n is the length of the list
        """
        self.moves.reset()                                  #reset moves

        for i in range(self.saved.length()):
            self.moves.add_last(self.saved.get_item(i))     # add back each values in saved into moves




def test_move_knight():
    chess1 = Tour()
    chess1.move_knight(3, 2)
    assert chess1.moves.the_array[:chess1.moves.length()] == [(1, 1), (3, 2)]
    chess1.move_knight(5, 3)
    assert chess1.moves.the_array[:chess1.moves.length()] == [(1, 1), (3, 2), (5, 3)]
    chess1.move_knight(3, 4)
    assert chess1.moves.the_array[:chess1.moves.length()] == [(1, 1), (3, 2), (5, 3), (3, 4)]

def test_valid_moves():
    chess2 = Tour()
    assert chess2.valid_moves((3, 2)) is True
    chess2.move_knight(3, 2)
    assert chess2.valid_moves((2, 1)) is False
    assert chess2.valid_moves((3, 1)) is False
    assert chess2.valid_moves((5, 3)) is True


def test_undo():
    chess3 = Tour()
    chess3.move_knight(3, 2)
    chess3.move_knight(5, 3)
    chess3.move_knight(3, 4)
    assert chess3.moves.the_array[:chess3.moves.length()] == [(1, 1), (3, 2), (5, 3), (3, 4)]
    chess3.undo()
    assert chess3.moves.the_array[:chess3.moves.length()] == [(1, 1), (3, 2), (5, 3)]


def test_copy():
    chess4 = Tour()
    chess4.move_knight(3, 2)
    chess4.move_knight(5, 3)
    chess4.copy()
    assert chess4.saved.the_array[:chess4.saved.length()] == [(1, 1), (3, 2), (5, 3)]
    chess4.move_knight(3, 4)
    chess4.move_knight(5, 5)
    assert chess4.saved.the_array[:chess4.saved.length()] == [(1, 1), (3, 2), (5, 3)]


def test_set():
    chess5 = Tour()
    chess5.move_knight(3, 2)
    chess5.move_knight(5, 3)
    chess5.copy()
    assert chess5.moves.the_array[:chess5.moves.length()] == [(1, 1), (3, 2), (5, 3)]
    chess5.move_knight(3, 4)
    chess5.move_knight(5, 5)
    chess5.set()
    assert chess5.moves.the_array[:chess5.moves.length()] == [(1, 1), (3, 2), (5, 3)]

if __name__ == '__main__':
    # the_tour = Tour()
    #
    # the_tour.move_knight(2, 3)
    # the_tour.move_knight(4, 2)
    # the_tour.show_tour()

    test_move_knight()
    test_valid_moves()
    test_undo()
    test_copy()
    test_set()

    print('All test pass')
