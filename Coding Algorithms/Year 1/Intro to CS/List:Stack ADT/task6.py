from task2 import ListADT
from task3 import read_text_file

class Nodes:
    def __init__(self, item = None, next= None):
        self.item = item
        self.next = next

class StackADT:
    def __init__(self, capacity):
        """Builds a stack with given capacity > 0."""
        if capacity <= 0:
            raise Exception("The capacity must be positive")
        self.the_array = [None] * capacity
        self.top = -1  # the index of the top element

    def size(self):
        """Returns the size, i.e. the number
        of elements in the container."""
        return self.top + 1

    def is_empty(self):
        """Returns True if and only if the container is empty."""
        return self.size() == 0

    def is_full(self):
        """Returns True if and only if the container is full."""
        return self.size() >= len(self.the_array)

    def push(self, item):
        """Places the given item at the top of the stack
        if there is capacity, or raises an Exception."""
        if self.is_full():
            raise Exception("Stack is full.")
        self.top += 1
        self.the_array[self.top] = item
        ## ALT: If we had started with top=-1, we could instead use:
        ## self.the_array[self.top+1] = item
        ## self.top += 1

    def pop(self):
        """Removes and returns the top element of the stack,
        or raises an Exception if there is none."""
        if self.is_empty():
            raise Exception("Tried to pop from an empty stack.")
        element = self.the_array[self.top]
        self.top -= 1
        return element

    def peek(self):
        """Returns the value on the top of the stack. Raises an
        IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("Attempted to peek an empty stack.")
        return self.the_array[self.top]

    def reset(self):
        """Removes all elements from the container."""
        self.top = -1




class Editor:
    def __init__(self):
        self.text_lines = ListADT()
        self.insert = StackADT(50)
        self.delete = StackADT(50)
        self.Sback = StackADT(50)
        self.Lback = ListADT()
        self.lines = StackADT(50)

    def print_menu(self):

        print('=================')
        print('\nMenu:')
        print('=================')
        print('1. read file')
        print('2. print num')
        print('3. delete num')
        print('4. insert num')
        print('5. search string')
        print('6. undo')
        print('7. quit')
        print('=================')

        quit = False


        while not quit:
            try:
                command = input('Please enter a command:').split()

                if command[0] == 'read':
                    if len(command) == 1:
                        raise Exception('?')
                    if len(command) == 2:
                        self.text_lines = (self.read_filename(command[1]))

                    self.print_menu()

                elif command[0] == 'print':
                    if len(command) == 1:
                        print(self.print_num(''))
                        StackADT.push(self.new, 'print' )
                    elif len(command) == 2:
                        print(self.print_num(command[1]))
                        StackADT.push(self.new, 'print' + command[1])


                    self.print_menu()

                elif command[0] == 'delete':

                    if len(command) == 1:
                        self.Sback.push(command[0])
                        self.Lback.append(command[0])
                        print(self.delete_num(''))
                    elif len(command ) == 2:
                        self.Sback.push(command[0])
                        self.Lback.append(command[0])
                        self.insert.push(command[1])
                        print(self.delete_num(command[1]))


                    self.print_menu()

                elif command[0] == 'insert':
                    storage = ListADT()
                    if len(command) == 1:
                        raise Exception
                    line = ''
                    if len(command) == 2:
                        while line != '.':
                            line = str(input())
                            if line != '.':
                                storage.append(line)
                        new_storage = ListADT()
                        for i in range(len(storage)):
                            new_storage.append(storage[-i - 1])


                        self.Sback.push(command[0])
                        self.Lback.append(command[0])
                        self.delete.push(command[1])
                        print(self.insert_num_strings(command[1], new_storage))
                        save = self.insert_num_strings\
                            (command[1], new_storage)
                        self.lines.push(save)

                    self.print_menu()
                elif command[0] == "search":
                    if len(command) == 1:
                        raise Exception("?")
                    elif len(command) == 2:
                        print(self.search_string(command[1]))
                        self.print_menu()
                    elif len(command) >= 3:
                        for i in range(2,len(command)):
                            command[1] += ' '
                            command[1] += command[i]
                        print(self.search_string(command[1]))

                        self.print_menu()

                elif command[0] == "undo":
                    print(self.undo())
                    #self.text_lines = self.Sback.pop()
                    #print(self.text_lines)

                elif command[0] == 'quit':
                    break

            except Exception:
                print('?')
                self.print_menu()


    def read_filename(self, file_name):
        self.text_lines = read_text_file(file_name)
        return self.text_lines


    def print_num(self, line_num):
        if line_num == 0:
            raise Exception('?')
        elif line_num == '':
            return self.text_lines
        line_num = int(line_num)
        if -1 < (line_num-1) <= len(self.text_lines):
            return self.text_lines[line_num-1]
        elif 0 > line_num >= -(len(self.text_lines)):
            return  self.text_lines[line_num]

    def delete_num(self, line_num):
        # self.text_lines = (self.read_filename('TestFile.txt'))
        if line_num == 0:
            raise Exception('?')
        elif line_num == '':
            self.text_lines = ListADT()
            return self.text_lines

        line_num = int(line_num)
        if -1 < (line_num-1) <= len(self.text_lines)-1:
            self.text_lines.delete(line_num-1)
            return self.text_lines
        elif 0 > line_num>= -(len(self.text_lines)):
            ListADT.delete(self.text_lines, line_num)
            return self.text_lines
        else:
            raise IndexError

    def insert_num_strings(self, line_num, lines):
        if line_num == 0:
            raise Exception('?')
        line_num = int(line_num)
        if -1 < (line_num-1) <= len(self.text_lines):
            for i in range(len(lines)):
                ListADT.insert(self.text_lines, (line_num-1), lines[i])
            return self.text_lines
        else:
            for i in range(len(lines)):
                ListADT.insert(self.text_lines, line_num, lines[i])
            return self.text_lines

    def search_string(self, query):
        new_list = ListADT()
        for i in range(len(self.text_lines)):
            exist = False
            for j in range(len(self.text_lines[i])):
                counter = 0
                if exist:
                    break
                if query[0] == (self.text_lines[i])[j]: #if the first letter == to letter
                    for k in range(len(query)):
                        maximum = j+k
                        if maximum >= len(self.text_lines[i]) or query[k] != (self.text_lines[i])[maximum]:
                            break
                        else:
                            counter += 1
                    if counter == len(query):
                        new_list.append(i+1)
                        exist == True
                        break

        return new_list

    def undo(self):

        for i in range(len(self.text_lines)):
            if self.Lback[i] == 'insert':
                return self.delete_num(self.insert.pop())
            elif self.Lback[i] == 'delete':
                return self.insert_num(self.delete.pop(), self.lines.pop())


hello = Editor()
hello.print_menu()