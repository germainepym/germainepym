class HashTable:

    def __init__(self, table_capacity = 100, hash_base = 31):

        self.table_size = table_capacity
        self.table = [None] * table_capacity
        self.base = hash_base
        self.count = 0


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
        for _ in range(self.table_size):
            if self.table[pos] is None:
                raise KeyError("key not found")
            elif self.table[pos][0] == key:
                return self.table[pos][1]
            else:
                pos = (pos + 1) % self.table_size

        raise KeyError("key not found")

    def __setitem__(self, key, value):
        """
            inserts the key with their value in the hash table

              @param          key and value
              @pre            the key must be a string
              @post           the key with the value is in the hash table
              @complexity     best case: O(1) when the position of the hash table is None
                              worse case: O(n) Where n is the length of the hash table
         """

        pos = self.hash(key)
        for _ in range(self.table_size):
            if self.table[pos] is None:
                self.table[pos] = (key, value)
                self.count += 1
                return
            elif self.table[pos][0] == key:
                self.table[pos] = (key, value)
                return
            else:
                pos = (pos + 1) % self.table_size

        self.rehash()
        self.__setitem__(key, value)

    def __contains__(self, key):
        """
            Checks if a specific key is in the hash table

              @param          key
              @pre            a hashtable with the size of a prime number
              @post           returns True the the key is found False if its not
              @complexity     best case: O(1) where the key is found immediately
                              worse case: O(n) where the key is not in the hash table
         """

        for i in range(len(self.table)):
            if self.table[i] is None:
                pass
            elif key == self.table[i][0]:
                return True
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
            
            return value
        else:
            raise KeyError

    def rehash(self):
        """
            expands the size of the hash table if the hash table gets full

              @param          -
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

        if self.table_size > primes[-1]:
            raise ValueError

        temparray = self.table
        self.table = [None] * self.table_size
        for i in range(len(temparray)):
            self.__setitem__(temparray[i][0], temparray[i][1])

        return self.table

