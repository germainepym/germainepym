import task6


class Freq:


    def __init__(self):
        self.word_frequency = task6.HashTable()
        self.array = []
        self.max = 0
        self.word = 0

    def add_file(self, filename):
        """
                       This function counts the frequency of the words of the book in the text file through the hash
                       table.

                       @param          filename
                       @pre            filename must be in .txt
                       @post           all words of each line being hashed into
                       @complexity     best case: O(n^2) if there is no punctuations connected to the word
                                       worse case: O(n^3) if there is a punctiation connected to the word

        """

        punctuations = ['.', ':', ';', ' " ', '(', ')']

        with open(filename, 'r') as file:
            for line in file:
                item = line.strip('\n')
                word = item.split()
                for w in word:
                    new = list(w)
                    for i in range(len(new)):
                        if new[i] in punctuations:
                            new[i] = ''
                    words = ''.join(new)
                    if words in self.word_frequency:
                        self.word_frequency[words] = self.word_frequency[words] + 1
                        if self.max < self.word_frequency[words]:
                            self.max = self.word_frequency[words]
                            self.word = words
                    else:
                        self.word_frequency[words] = 1

            file.close()
        return self.word_frequency.table

    def rarity(self, word):
        """
                This function returns the score based on the number of occurrence of the word

                    @param          word
                    @pre            if the word is found in the table
                    @post           the score of the particular word
                    @complexity     best case: O(1) as the key is found on the first iteration then compared
                                                using the if conditions
                                    worse case: O(n) where n is the table_capacity as the program iterates
                                                through the table n times as it depends on the getitem

        """
        score = 0
        try:
            if self.word_frequency[word] >= self.max / 100:
                score = 0

            elif self.word_frequency[word] < self.max / 1000:
                score = 2

            elif self.max / 100 < self.word_frequency[word] < self.max / 1000:
                score = 1
        except KeyError:
                score = 3


        return score

    def evaluate_frequency(self, other_filename):
        """
                This function evaluates the percentage based on how rare is the word which is (rarity/total)

                @param          other_filename
                @pre            the filename does exist in the file directory
                @post           all percentage of common, uncommon, rare, errors
                @complexity     best case: O(1) is because when the first item is the item to be retrieved as it
                                                uses rarity function which alsocalls getitem in the hash table
                                worse case: O(n) here the program iterates through the whole table to retrieved
                                                    the item which is at the end of the tablewhich uses rarity
                                                    and calls getitem in the hash table

                """
        """
                This function evaluates the percentage based on how rare is the word which is (rarity/total)
                :param      other_filename: the filename to be read to get the word
                :return:    a tuple consisting of percentage of common, uncommmon, rare, errors
                @bigO:      best case:  O(1) is because when the first item is the item to be retrieved as it uses rarity function which also
                                        calls getitem in the hash table
                            worst case: O(n) where the program iterates through the whole table to retrieved the item which is at the end of the table
                                        which uses rarity and calls getitem in the hash table
                @pre:       the filename does exist in the file directory
                @post:      all percentage of common, uncommon, rare, errors
                """
        common = 0
        rare = 0
        uncommon = 0
        errors = 0
        punctuations = ['.', ':', ';', ' " ', '(', ')']
        with open(other_filename, 'r') as file:
            for line in file:
                item = line.strip('\n')
                word = item.split()
                for w in word:
                    new = list(w)
                    for i in range(len(new)):
                        if new[i] in punctuations:
                            new[i] = ''
                    words = ''.join(new)
                    if words in self.array:
                        pass
                    else:
                        self.array.append(words)
            file.close()


        for i in self.array:
            score = self.rarity(i)
            if score == 0:
                common += 1
            elif score == 1:
                rare += 1
            elif score == 2:
                uncommon += 1
            elif score == 3:
                errors += 1

        common = (common / len(self.array))*100
        uncommon = (uncommon / len(self.array)) *100
        rare = (rare / len(self.array)) *100
        errors = (errors / len(self.array)) *100

        return (common, uncommon, rare, errors)

freq = Freq()
# print(freq.add_file("words_simple.txt"))
# print(freq.evaluate_frequency("words_perm.txt"))
# print(freq.rarity('Project'))