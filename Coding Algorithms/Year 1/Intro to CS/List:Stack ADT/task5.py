from task2 import ListADT
from task3 import read_text_file

class Editor:
    def __init__(self):
        """
                                Creates an empty object of the class, i.e., an empty array list.

                                @param          none
                                @pre            none
                                @post           an empty list object is created
                                @complexity     best case: O(1)
                                                worse case: O(1)

        """
        self.text_lines = ListADT()


    def print_menu(self):
        """
                        Opens up a menu with choices for the users to choose and execute

                        @param          none
                        @pre            none
                        @post           a menu is shown to user
                        @complexity     best case: dependant on user's choice
                                        worse case: dependant on user's choice

        """

        print('=================')
        print('\nMenu:')
        print('=================')
        print('1. read file')
        print('2. print num')
        print('3. delete num')
        print('4. insert num')
        print('5. search string')
        print('6. quit')
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
                    elif len(command) == 2:
                        print(self.print_num(command[1]))

                    self.print_menu()

                elif command[0] == 'delete':
                    if len(command) == 1:
                        print(self.delete_num(''))
                    elif len(command ) == 2:
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
                            new_storage.append(storage[-i-1])

                        print(self.insert_num(command[1], new_storage))


                elif command[0] == "search":
                    if len(command) == 1:
                        raise Exception("?")
                    elif len(command) == 2:
                        print(self.search_string(command[1]))
                    elif len(command) >= 3:
                        for i in range(2,len(command)):
                            command[1] += ' '
                            command[1] += command[i]
                        print(self.search_string(command[1]))
                        self.print_menu()

                elif command[0] == 'quit':
                    break

            except Exception:
                print('?')
                self.print_menu()


    def read_filename(self, file_name):
        """
                        Reads the file of the the name given

                        @param          file_name
                        @pre            user must enter file name
                        @post           the file is read
                        @complexity     best case: O(n) where n is the number of lines printed
                                        worse case: O(n) where n is the number of lines printed

        """
        self.text_lines = read_text_file(file_name)
        return self.text_lines


    def print_num(self, line_num):
        """
                        Prints either a certain line from the text file or the whole text dependant on the user's
                        choice

                        @param          line_num
                        @pre            a file must be read
                        @post           a line of text or the whole text is printed out
                        @complexity     best case: O(1)
                                        worse case: O(n): for n is the number of lines printed

        """
        if line_num == 0:
            raise Exception('?')
        elif line_num == '':
            return self.text_lines
        line_num = int(line_num)
        if -1 < (line_num-1) <= len(self.text_lines):
            return self.text_lines[line_num-1]
        elif 0 > line_num >= -(len(self.text_lines)):
            return  self.text_lines[line_num]
        else:
            raise IndexError

    def delete_num(self, line_num):
        """
                        Either delete a line from the text file or the whole text dependant on the user's choice

                        @param          line_num
                        @pre            a file must be read
                        @post           either a single line or whole text is deleted
                        @complexity     best case: O(1)
                                        worse case: O(n) where n is the number of lines printed

        """
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

    def insert_num(self, line_num, lines):
        """
                    Dependant on how many lines the user inputs, it is inserted into the array

                    @param          line_num and lines
                    @pre            a file must be read
                    @post           strings inputted into the array
                    @complexity     best case: O(1)
                                    worse case: O(n) where n is the number of lines printed

        """
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
        """
                    prints out the line if it contains the keywords the user wants

                    @param          query
                    @pre            a file must be read
                    @post           lines of code that contains the keywords is printed
                    @complexity     best case: O(1) if the length of self.text_lines is empty
                                    worse case: O(i*j*k) i is the number of lines, j is the number of letters
                                                         in each line and k is the number of letters for string.

        """
        new_list = ListADT()
        for i in range(len(self.text_lines)):
            exist = False
            for j in range(len(self.text_lines[i])):
                counter = 0
                if exist:
                    break
                if query[0] == (self.text_lines[i])[j]:  # if the first letter == to letter
                    for k in range(len(query)):
                        maximum = j + k
                        if maximum >= len(self.text_lines[i]) or query[k] != (self.text_lines[i])[maximum]:
                            break
                        else:
                            counter += 1
                    if counter == len(query):
                        new_list.append(i + 1)
                        exist == True
                        break

        return new_list

hello = Editor()
hello.print_menu()
# print(hello.search_string('is a'))

