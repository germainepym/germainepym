
class Node:
    """
    The Node class for the Trie
    """

    def __init__(self, size=27):
        """
            This function creates the nodes of the Trie
            Arguments:          size = 27
            Time complexity:    Best case: O(1)
                                Worst case: O(1)

            Space complexity: O(s+l+c) for s is size, l is self.link and c is self.char
            Aux space complexity: O(l+c) for l is self.link and c is self.char
            Return: does not return anything
        """
        self.link = [None] * size
        self.freq = 0
        self.char = []
        self.terminal = False

# The Trie class
class Trie:
    """
    Class for the Trie, to insert strings and search for strings
    """

    def __init__(self, text):
        """
        This function pre-processes text into the trie
        Precondition: the element in text are strings
        Arguments:          text = a list of strings
        Time complexity:    Best case: O(1) when text is an empty list
                            Worst case: O(T) for T is the total number of characters in text

        Space complexity: O(k+n) for k is the number of strings in text and n is the root node
        Aux space complexity: O(n) for n is the root node
        Return: does not return anything
        """
        self.root = Node()
        for i in range(len(text)):
            self.insert(text[i])

    def insert(self, key):
        """
        Add word into the Trie
        Precondition: key is a string
        Arguments:          key = a string to be inserted in to the Trie
        Time complexity:    Best case: O(1) if key is an empty string
                            Worst case: O(k) for k is the total number of characters in key

        Space complexity: O(k+n) for k is the length of the key and n is for current node
        Aux space complexity: O(n) for n is current node
        Return:  does not return anything
        """
        current = self.root
        count = 0
        self.insert_aux(current, key, count)

    def insert_aux(self, current, key, count):
        """
                Question 1: Add words into the Trie
                Precondition: key is a string
                Arguments:          current = list of the size of 27
                                    key = a string to be inserted in to the Trie
                                    count = keep track of which position of key it is at
                                            (eg, if key = abc, if count = 2, then it is at c)

                Time complexity:    Best case: O(1) if key is an empty string
                                    Worst case: O(k) for k is the total number of characters in key

                Space complexity: O(n+k) for n is the current node and k is the length of key
                Aux space complexity: O(1)
                Return:  does not return anything
            """
        # base
        if len(key) == 0:
            return
        # recursion
        else:
            # After traversing down the trie, till the last alphabet of the string, check for terminal
            if count == (len(key)):
                # if there is a terminal (means there is duplicate word)
                if current.link[0] is not None:
                    current = current.link[0]
                    current.char.append(key)
                    current.freq += 1  # add the frequency
                    return
                else:
                    # if there is no terminal (means the word is new to the trie)
                    current.link[0] = Node()  #create a new node
                    current = current.link[0]
                    current.terminal = True
                    current.char.append(key)
                    current.freq += 1  # add the frequency
                    return

            index = (ord(key[count]) - 97) + 1
            # if the path exists, continue traversing down the trie
            if current.link[index] is not None:
                current = current.link[index]

                # to ensure that the count is not more than the length of the key
                if len(key) > count:
                    count += 1
                    current.freq += 1
                    self.insert_aux(current, key, count)

                return
            # if the path doesn't exist, create a new node
            else:
                current.link[index] = Node()
                current = current.link[index]
                count += 1
                current.freq += 1
                self.insert_aux(current, key, count)

    def string_freq(self, query_str):
        """
            Question 2: Search the trie for query_str, if query_str is in the trie, find out the frequency of the
                       word
            Precondition: query_str is a string
            Arguments:          query_str = a string to be searched

            Time complexity:    Best case: O(1) if query_str is an empty string
                                Worst case: O(q) for q is the length of the query_str

            Space complexity: O(q+c) for q is the length of the query_str and c is the root node
            Aux space complexity: O(c) for c is the root node
            Return: the frequency of query_str
        """
        current = self.root
        count = 0
        return self.string_freq_aux(current, query_str, count)

    def string_freq_aux(self, current, query_str, count):
        """
            Question 2: Search the trie for query_str, if query_str is in the trie, find out the frequency of the
                       word
            Precondition: query_str is a string
            Arguments:          current = list of the size of 27
                                query_str = a string to be searched
                                count = keep track of which position of key it is at
                                        (eg, if key = abc, if count = 2, then it is at c)

            Time complexity:    Best case: O(1) if query_str is an empty string
                                Worst case: O(q) for q is the length of the query_str

            Space complexity: O(c+q) for c is the current node and q is the length of query_str
            Aux space complexity: O(1)
            Return: the frequency of query_str
        """
        if len(query_str) == 0:
            return 0
            # recursion
        else:
            # after reaching the last alphabet if the string, return the frequency of the words that matches the
            # query_str
            if count == (len(query_str)):
                if current.link[0] is not None:
                    current = current.link[0]
                    return current.freq
                # if the query_str is None (means its not in the trie) return 0
                else:
                    return 0

            index = (ord(query_str[count]) - 97) + 1
            # if the path exist, then continue traversing down the trie
            if current.link[index] is not None:
                current = current.link[index]

                # to ensure that the count is not more than the length of the key
                if len(query_str) > count:
                    count += 1
                    freq = self.string_freq_aux(current, query_str, count)
                    return freq

                return current.freq
            # if the path doesn't exist return because no such string exist in the trie
            else:
                return 0

    def prefix_freq(self, query_str):
        """
           Question 3: Search the trie for query_str, find out the frequency of the words that has that query_str
                        as part of its prefix or words that is query_str

           Precondition: query_str is a string

           Arguments:          query_str = a string to be searched

           Time complexity:    Best case: O(1) if query_str is an empty string
                               Worst case: O(q) for q is the length of the query_str

           Space complexity: O(q+c) for q is the length of the query_str and c is the root node
           Aux space complexity: O(c) for c is the root node
           Return: the frequency of query_str and the words that contain the prefix of query_str
        """
        current = self.root
        count = 0
        return self.prefix_freq_aux(current, query_str, count)

    def prefix_freq_aux(self, current, query_str, count):
        """
            Question 3: Search the trie for query_str, find out the frequency of the words that has that query_str
                        as part of its prefix or words that is query_str

            Precondition: query_str is a string

            Arguments:          current = list of the size of 27
                                query_str = a string to be searched
                                count = keep track of which position of key it is at
                                        (eg, if key = abc, if count = 2, then it is at c)

            Time complexity:    Best case: O(1) if query_str is an empty string
                                Worst case: O(q) for q is the length of the query_str

            Space complexity: O(c+q) for c is the current node and q is the length of query_str
            Aux space complexity: O(1)
            Return: the frequency of query_str and the words that contain the prefix of query_str
        """
        if len(query_str) == 0:
            return 0
            # recursion
        else:
            if count == (len(query_str)):
                # if the query_str is in the trie return
                if current.link[0] is not None:
                    return current.freq
                # if the query_str is None (means its not in the trie) return 0
                else:
                    return 0

            index = (ord(query_str[count]) - 97) + 1
            # if the path exist, then continue traversing down the trie
            if current.link[index] is not None:
                current = current.link[index]

                # to ensure that the count is not more than the length of the key
                if len(query_str) > count:
                    count += 1
                    pre_freq = self.prefix_freq_aux(current, query_str, count)
                    if len(query_str) == count:
                        return current.freq
                    else:
                        return pre_freq

                return current.freq
                # if the path doesn't exist return because no such string exist in the trie
                # if the query_str is not in the trie return 0
            else:
                return 0

    def wildcard_prefix_freq(self, query_str):
        """
           Question 4: Search the trie for query_str that contains a wildcard, the wildcard can be any alphabet that
                        matches the content of the trie, find out the frequency of the words that has that query_str
                        as part of its prefix or words that is query_str

           Precondition: query_str is a string

           Arguments:          query_str = a string to be searched

           Time complexity:    Best case: O(1) if query_str is an empty string
                               Worst case: O(q) for q is the length of the query_str

           Space complexity: O(q+c+o) for q is the length of the query_str and c is the root node and o is output
           Aux space complexity: O(c+o) for c is the root node and is output

           Return: a list of strings in the lexicographical order that has the prefix query_str
        """
        current = self.root
        count = 0
        output = []
        return self.wildcard_prefix_freq_aux(current, query_str, count, output)

    def wildcard_prefix_freq_aux(self, current, query_str, count, output):
        """
            Question 4: Search the trie for query_str that contains a wildcard, the wildcard can be any alphabet that
                        matches the content of the trie, find out the frequency of the words that has that query_str
                        as part of its prefix or words that is query_str

            Precondition: query_str is a string

            Arguments:          current = list of the size of 27
                                query_str = a string to be searched
                                count = keep track of which position of key it is at
                                        (eg, if key = abc, if count = 2, then it is at c)
                                output = a list of strings that contains the prefix query_str

            Time complexity:    Best case: O(1) if query_str is an empty string
                                Worst case: O(q+s) for q is the length of the query_str and s is the total number of
                                characters in all strings of the text

            Space complexity: O(c+q+o) for c is the current node, q is the length of query_str and o is output
            Aux space complexity: O(1)

            Return: a list of strings in the lexicographical order that has the prefix query_str
        """
        track = 0
        if len(query_str) == 0:
            return []
            # recursion
        else:
            # if we reach the last alphabet of the query_str
            if count == (len(query_str)):
                # enter the recursion to traverse to the rest of the tree to obtain the strings that has the same prefix
                # of query_str
                self.retrieve_the_rest(current, output)
                return output

            # if one of the alphabet of query_str if '?', enter
            if query_str[count] == '?':
                for i in range(len(current.link)):
                    if i == 0:
                        pass
                    # if the first character of query_str is '?'
                    elif query_str[0] == '?':
                        if current.link[i] is not None:
                            count += 1
                            self.wildcard_prefix_freq_aux(current.link[i], query_str, count, output)
                            count -= 1

                    # if the last character of query_str is '?'
                    elif query_str[len(query_str) - 1] == '?':
                        if current.link[i] is not None:
                            if count != len(query_str):
                                count += 1
                                self.wildcard_prefix_freq_aux(current.link[i], query_str, count, output)
                            else:
                                self.wildcard_prefix_freq_aux(current.link[i], query_str, count, output)

                    # if the any character in between the first and last characters of query_str is '?'
                    else:
                        if current.link[i] is not None:
                            count += 1
                            self.wildcard_prefix_freq_aux(current.link[i], query_str, count, output)
                            count -= 1

                return output
            index = (ord(query_str[count]) - 97) + 1
            # if the path exist, then continue traversing down the trie
            if current.link[index] is not None:

                # to ensure that the count is not more than the length of the key
                if len(query_str) > count:
                    count += 1
                    self.wildcard_prefix_freq_aux(current.link[index], query_str, count, output)

                return output

                # if the path doesn't exist return because no such string exist in the trie
            else:
                return []

    def retrieve_the_rest(self, current, output):
        """
            Traverses down the tree, starting from the prefix onwards to obtain and append the strings that has the
            prefix into output

            Arguments:          current = list of the size of 27
                                output = a list of strings that contains the prefix query_str

            Time complexity:    Best case: O(s) for s is the total number of characters in all strings of the text
                                Worst case: O(s) for s is the total number of characters in all strings of the text

            Space complexity: O(c+o) for c is the current node and o is output
            Aux space complexity: O(1)
            Return: a list of strings in lexicographical order
    """
        # if its None, means that there is no more node to continue traversing down the tree
        if current is None:
            return output
        else:
            # if is not None, means that is a node, and if current.terminal is postive, means that the node is a
            # terminal, hence it is added into output
            if current.terminal:
                output += current.char
                return output

        # traversing down the Trie
        for i in range(len(current.link)):
            self.retrieve_the_rest(current.link[i], output)

