from tour import Tour
from unsorted_list import List

def print_menu():
    print('\nMenu:')
    print('1. position')
    print('2. restart')
    print('3. undo')
    print('4. save')
    print('5. restore')
    print('6. quit')

chess = Tour()
quit = False



while not quit:
    try:
        print_menu()
        command = int(input('Please enter your command: '))

        if command < 1 or command > 6:
            raise ValueError

        if command == 1:
            try:
                row = int(input('Insert row :'))
                col = int(input('Insert column :'))

                position = (row, col)

                if (row < 1 or row > 8) or (col < 1 or col > 8):
                    raise ValueError

                while not chess.valid_moves(position):
                    print('The move is not valid, please enter a new position')
                    row = int(input('Insert row :'))
                    col = int(input('Insert column :'))

                    position = (row, col)
                chess.show_tour()

            except ValueError:
                print('Position out of bound, please only enter numbers from 1 - 8')


        elif command == 2:
            try:
                chess.moves.reset()
                row = int(input("Please insert row: "))
                col = int(input("Please insert column: "))

                if (row < 1 or row > 8) or (col < 1 or col > 8):
                    raise ValueError

                position = (row, col)
                chess.moves.add_last(position)
                chess.show_tour()

                next_moves = chess.next_moves(position)

                for i in range(next_moves.length()):
                    print(next_moves.get_item(i))

            except ValueError:
                print('Position out of bound, please only enter numbers from 1 - 8')

        elif command == 3:
            chess.undo()
            chess.show_tour()

        elif command == 4:
            chess.copy()

        elif command == 5:
            chess.set()
            chess.show_tour()

        elif command == 6:
            quit = True

    except ValueError:
        print('Command is not available')

