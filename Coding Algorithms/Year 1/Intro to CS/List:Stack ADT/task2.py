from math import *

class ListADT:

    def __init__(self, size = 50):
        """
                Creates an empty object of the class, i.e., an empty array list.

                @param          size number of items in containing array, or maxitems of list
                @pre            none
                @post           an empty list object is created
                @complexity     best case: O(n) n is the size of list
                                worse case: O(n) n is the size of list

        """
        self.length = 0
        if size < 40:
            self.the_array = [None] * 40
        else:
            self.the_array = [None] * size
        self.size = size

    def __str__(self):
        """
                 Turns every single element in a array to a string and displays it

                 @param          none
                 @pre            a array of any size
                 @post           elements in the array are 'listed' down in strings
                 @complexity     best case: O(n) n is the length of list
                                 worse case: O(n) n is the length of list
        """
        string = ""
        length = self.length
        if length != 0:
            for i in range(self.length):
                string = string + str(self.the_array[i]) + "\n"
        return string

    def __len__(self):
        """
                  returns the length of the array

                  @param          none
                  @pre            a array of any size
                  @post           number of elements in the array
                  @complexity     best case: O(1)
                                  worse case: O(1)
         """
        return self.length

    def __getitem__(self, index):
        """
                  displays the number at the position index based on the index given

                  @param          index of array
                  @pre            a array of any size with elements in it that is not empty
                  @post           an element in the array is returned
                  @complexity     best case: O(1)
                                  worse case: O(1)
         """
        try:
            if self.is_empty():
                raise Exception

            try:
                if index > (self.length - 1):
                    raise IndexError

                if index >= 0:
                    return self.the_array[index]

            except IndexError:
                print('Positive index not within range')

            try:
                if index < (-self.length):
                    raise IndexError

                if index < 0:
                    return self.the_array[self.length + index]
            except IndexError:
                print('Negative index not within range')

        except Exception:
            print('The list is empty')

    def __setitem__(self, index, item):
        """
                  set the number at the position index based on the index given

                  @param          index of list and the number to set
                  @pre            an array of any size with elements in it that is not empty
                  @post           an element in the array is changed based on the index and item given
                  @complexity     best case: O(1)
                                  worse case: O(1)
         """

        try:

            if self.is_empty():
                raise Exception

            try:

                if index > (self.length - 1):
                    raise IndexError

                if index >= 0:
                    self.the_array[index] = item

            except IndexError:
                print('Positive index out of range')

            try:
                if index < (-self.length):
                    raise IndexError

                if index < 0:
                    self.the_array[self.length + index] = item

            except IndexError:
                print('Negative index out of range')

        except Exception:
            print('This list is empty')

        return self.the_array

    def __eq__(self, other):
        """
                  checks if the current array is equivalent to another array

                  @param          an array
                  @pre            a list of any size with elements in it
                  @post           none
                  @complexity     best case: O(1)
                                  worse case: O(1)
         """
        thislist = self.the_array
        if thislist == other:
            return True
        else:
            return False

    def insert(self, index, item):
        """
                  Insert a number at the given index, shuffling the rest of the elements to the back of the array.
                  If the array is full, then the size of array is increased by 1.9(round off)

                  @param          index of the array and the item to be inserted
                  @pre            an array of any size with elements in it that is not full or empty
                  @post           a new element was inserted to the array at the index given
                  @complexity     best case: O(n) where the list is empty
                                  worse case: O(n^2) where the list is full
         """

        if self.is_full():
            templist = self.the_array
            self.the_array = [None] * (ceil(len(self) * 1.9))
            for i in range(len(templist)):
                self.the_array[i] = templist[i]

        if self.is_empty():
            if index >= 0:
                self.length += 1
                self.the_array[index] = item
                return self.the_array

            elif index < 0:
                index = index + len(self) + 1
                self.length += 1
                self.the_array[index] = item
                return self.the_array


        elif 0 <= index <= self.length:

            if index == self.length:
                self.append(item)
                return self.the_array

            if index > 0 :
                self.length += 1
                n = len(self) - 1
                while n >= index:
                    self.the_array[n] = self.the_array[n - 1]
                    n -= 1
                self.the_array[index] = item
                return self.the_array

        elif -1 >= index >= -self.length:

            if index == -1:
                self.append(item)
                return self.the_array

            if index < 0:
                index = index + len(self) + 1
                self.length += 1
                n = len(self) - 1
                while n >= index:
                    self.the_array[n] = self.the_array[n - 1]
                    n -= 1
                self.the_array[index] = item
                return self.the_array
        else:
            raise IndexError


    def delete(self, index):
        """
                  delete a number at the given index. If the number of elements in the array is smaller than 1.4 of the
                  size of the array, the size of the array is decreased into half of the size.

                  @param          index of the array
                  @pre            an array of any size with elements in it that is not empty
                  @post           an element was deleted from the array at the index given
                  @complexity     best case: O(n) where the list is 1/4 of length of self the array
                                  worse case: O(n^2) where the length of list is small
         """
        if self.is_empty():
            raise Exception

        if 0 <= index <= self.length:
                deleted = self.the_array[index]

                if index >= 0:
                    while index < len(self) - 1:
                        self.the_array[index] = self.the_array[index + 1]
                        index += 1
                    self.length -= 1
                    self.the_array[self.length] = None


        elif -1 >= index >= -self.length:
                deleted = self.the_array[self.length + index]

                if index < 0:
                    index = index + len(self)
                    while index < len(self) - 1:
                        self.the_array[index] = self.the_array[index + 1]
                        index += 1
                    self.length -= 1
                    self.the_array[self.length] = None


        else:
            raise IndexError

        if self.length < int(1 / 4 * len(self.the_array)):
                newlist = self.the_array
                lengthh = len(self.the_array) // 2
                self.the_array = [None] * lengthh
                for i in range(lengthh):
                    self.the_array[i] = newlist[i]

        return deleted


    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == len(self.the_array)

    def __contains__(self, item):
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False

    def append(self, item):
        if self.is_full():
            templist = self.the_array
            self.the_array = [None] * (ceil(len(self) * 1.9))
            for i in range(len(templist)):
                self.the_array[i] = templist[i]

        if not self.is_full():
            self.the_array[self.length] = item
            self.length += 1


    def unsafe_set_array(self, array, length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        try:
            assert self.in_test_mode
        except:
            raise Exception('Cannot run unsafe_set_array outside testing mode')

        self.the_array = array
        self.length = length



def test__str__():
    tsk1 = ListADT(42)
    tsk1.append(10)
    tsk1.append(8)
    tsk1.append(9)
    tsk1.append(7)
    assert str(tsk1) == '10\n8\n9\n7\n'


def test__len__():
    tsk1 = ListADT(42)
    assert len(tsk1) == 0
    tsk1.append(10)
    tsk1.append(8)
    tsk1.append(9)
    tsk1.append(7)
    assert len(tsk1) == 4

def test_get_item():
    tsk1 = ListADT(42)
    tsk1.append(10)
    tsk1.append(8)
    tsk1.append(9)
    tsk1.append(7)
    assert tsk1[0] == 10
    assert tsk1[1] == 8
    assert tsk1[2] == 9
    assert tsk1[3] == 7

def test_set_item():
    tsk1 = ListADT(42)
    tsk1.append(10)
    tsk1.append(8)
    tsk1.append(9)
    tsk1.append(7)
    tsk1[0] = 5
    tsk1[1] = 6
    assert tsk1.the_array[:tsk1.length]  == [5,6,9,7]
    tsk1[2] = 7
    tsk1[3] = 8
    assert tsk1.the_array[:tsk1.length] == [5,6,7,8]

def test__eq__():
    lst = ListADT(42)
    lst.append(10)
    lst.append(8)
    lst.append(9)
    lst.append(7)
    lst2 = ListADT(42)
    lst2.append(10)
    lst2.append(8)
    lst2.append(9)
    lst2.append(7)
    assert (lst == lst2) == True
    lst3 = ListADT(42)
    lst3.append(10)
    lst3.append(8)
    lst3.append(9)
    lst3.append(7)
    lst4 = ListADT(42)
    lst4.append(10)
    lst4.append(8)
    lst4.append(3)
    lst4.append(7)
    assert (lst3 == lst4) == False

def test_insert():
    tsk1 = ListADT(40)
    tsk1.append(10)
    tsk1.append(8)
    tsk1.append(9)
    tsk1.append(7)
    assert tsk1.the_array[:tsk1.length] == [10,8,9,7]
    tsk1.insert(1,6)
    assert tsk1.the_array[:tsk1.length] == [10,6,8,9,7]
    tsk1.insert(3,5)
    assert tsk1.the_array[:tsk1.length] == [10,6,8,5,9,7]
    tsk1.insert(2,4)
    assert tsk1.the_array[:tsk1.length] == [10,6,4,8,5,9,7]

    tsk2 = ListADT(42)
    tsk2.append(1)
    for i in range(42):
        tsk2.insert(-1, i)
    assert len(tsk2.the_array) == 80


def test_delete():
    tsk1 = ListADT(100)
    tsk1.append(10)
    tsk1.append(8)
    tsk1.append(9)
    tsk1.append(7)
    assert tsk1.the_array[:tsk1.length] == [10,8,9,7]
    tsk1.delete(1)
    assert tsk1.the_array[:tsk1.length] == [10,9,7]
    assert tsk1.length == 3
    tsk1.delete(1)
    assert tsk1.the_array[:tsk1.length] == [10, 7]
    assert tsk1.length == 2

    tsk2 = ListADT(100)
    tsk2.append(10)
    tsk2.append(8)
    tsk2.append(9)
    tsk2.append(1)
    tsk2.append(2)
    tsk2.append(3)
    tsk2.append(4)
    tsk2.delete(-4)
    assert tsk2.the_array[:tsk2.length] == [10,8,9,2,3,4]
    assert len(tsk2.the_array) == 50
    assert tsk2.length == 6
    tsk2.delete(0)


# hello = ListADT(50)
# hello.append(1)
# hello.append(1)
# hello.append(1)
# hello.append(1)
# print(hello.__str__())


test__str__()
test__len__()
test_get_item()
test_set_item()
test__eq__()
test_insert()
test_delete()
#print('T E S T  P A S S E D ')

