import task2
import csv
import timeit
import bst

class HashTable:

    def __init__(self, table_capacity = 100, hash_base = 31):

        self.table_size = table_capacity
        self.table = [None] * table_capacity
        self.base = hash_base
        self.count = 0

        self.collision = 0
        self.probe_total = 0
        self.count_rehash = 0
        self.probe_max = 0


    def __getitem__(self, key):
        """
                  finds the value of they given key in the hash table

                  @param          key
                  @pre            the key must be a string
                  @post           the value of the key is returned
                  @complexity     best case: O(1) when the key is found immediately
                                  worse case: O(N) when the key is not in the hash the hash table
        """
        pos = self.hash(key)
        tree = self.table[pos]
        if tree is None:
            raise KeyError("key not found")

        else:
            if key in tree:
                item = tree[key]
                return item
            else:
                raise KeyError

    def __setitem__(self, key, value):
        """


              @param          index of list and the number to set
              @pre            an array of any size with elements in it that is not empty
              @post           an element in the array is changed based on the index and item given
              @complexity     best case: O(1) when the position of the hash table is None
                              worse case: O(n) Where n is the length of the hash table
         """

        self.count += 1
        pos = self.hash(key)
        tree = self.table[pos]
        probe = 0
        if self.table[pos] is None:
            my_tree = bst.BinarySearchTree()
            my_tree.__setitem__(key, value)
            self.table[pos] = my_tree
            return
        else:
            probe += tree.__len__()
            tree.__setitem__(key, value)

            self.collision += 1
            self.probe_total += probe
            if probe > self.probe_max:
                self.probe_max = probe
            return


    def __contains__(self, key):
        """
            Checks if a specific key is in the hash table

              @param          key
              @pre            a hashtable with the size of a prime number
              @post           returns True the the key is found False if its not
              @complexity     best case: O(1) where the key is found immediately
                              worse case: O(n) where the key is not in the hash table
         """
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def hash(self, key):
        """
            Sets a hash value for the key

              @param          key
              @pre            a hashtable with the size of a prime number
              @post           a hash value is associated with the key
              @complexity     best case: O(1)
                              worse case: O(n) where n is the length of the key
         """
        if type(key) == str:
            value = 0
            for i in range(len(key)):
                value = (value * self.base + ord(key[i])) % self.table_size
            return value
        else:
            raise KeyError

    def rehash(self):
        """
            expands the size of the hash table if the hash table gets full

              @param          None
              @pre            The hash table is full
              @post           The hash table is expanded two times ( or more) its original size
              @complexity     best case: O(1)
                              worse case: O(n) where n is the size of list of the prime numbers
         """
        primes = [3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 293, 353, 431, 521, 631, 761, 919,
                  1103, 1327, 1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591, 17519,
                  21023, 25229, 30313, 36353, 43627, 52361, 62851, 75521, 90523, 108631, 130363, 156437, 187751, 225307,
                  270371, 324449, 389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263, 1674319, 2009191,
                  2411033, 2893249, 3471899, 4166287, 4999559, 5999471, 7199369]
        self.table_size = self.table_size * 2

        for i in range(len(primes)):
            if self.table_size < primes[i]:
                self.table_size = primes[i]
                break

        temparray = self.table
        self.table = [None] * self.table_size
        for i in range(len(temparray)):
            self.__setitem__(temparray[i][0], temparray[i][1])

        return self.table

    def statistics(self):
        """
          Returns the statistics of the number of collision, total probe, maximum probe and the number of rehash

            @param          None
            @pre            None
            @post           returns statistics of collision, probing and rehash
            @complexity     best case: O(1)
                            worse case: O(1)
        """

        return (self.collision, self.probe_total, self.probe_max, self.count_rehash)


def load_dictionary_statistics(hash_base, table_size, filename, max_time=120):
    """
            This function calls load dictionary function and times how long the function takes to run

            @param          hash_base, table_size, filename, max_time
            @pre            filename must be in .txt
            @post           the time taken to read the file passed time_limit
            @complexity     best case: O(1) empty file
                            worse case: O(n*m) where n size of the file and m is the complexity of the hash table
                                        function that was called

     """


    table= HashTable(table_size, hash_base)
    try:
        time = task2.load_dictionary(table, filename, max_time)
        words = table.count
        collision_count, total_probe, max_probe, rehash_count = table.statistics()

        return words, time, collision_count, total_probe, max_probe, rehash_count
    except Exception:
        time = None
        words = table.count
        collision_count, total_probe, max_probe, rehash_count = table.statistics()

        return words, time, collision_count, total_probe, max_probe, rehash_count


def table_load_dictionary_statistics(max_time=120):
    """
            This function prints out the statistics of the hashed file, number of collision, maximum probe, longest
            probe and the number of time it rehashes and prints the output into a csv file.

            @param          max_time
            @pre            None
            @post           statistics outputted in the csv file
            @complexity     best case: O(n^4)
                            worse case: O(n^4)

     """
    b = [1, 27183, 250726]
    tablesize = [250727, 402221, 1000081]
    dic = ["english_small.txt", "english_large.txt", "french.txt"]
    with open('output_task5.csv', 'w') as openFile:  # create csv file

        writer = csv.writer(openFile)
        writer.writerow(['Dic', 'Tablesize', 'b', 'No. of words', 'time taken', 'collision', 'total probe', 'max probe', 'rehash count'])

        for i in range((len(dic))):
            counter = 0
            counter2 = 0
            for k in range(len(b) * len(tablesize)):
                base = b[counter2]
                table_Size = tablesize[counter]
                print(base, table_Size)
                word_n_time = load_dictionary_statistics(base, table_Size, dic[i], max_time)
                counter += 1

                if counter == 3:
                    counter = 0
                print(word_n_time)

                if word_n_time[1] is None:
                    writer.writerow([dic[i], table_Size, base, word_n_time[0], (max_time + 10),word_n_time[2], word_n_time[3], word_n_time[4], word_n_time[5]])
                else:
                    writer.writerow([dic[i], table_Size, base, word_n_time[0], word_n_time[1],word_n_time[2], word_n_time[3], word_n_time[4], word_n_time[5]])

                if counter == 0:
                    counter2 += 1

# table_load_dictionary_statistics(120)