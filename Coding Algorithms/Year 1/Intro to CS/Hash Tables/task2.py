import task1
import timeit
import csv

def load_dictionary(hash_table, filename,time_limit= None):
    """
            This function reads the filename and adds the words in the file into the hashtable
            and raises and exception if the time takes to read the file passes the time limit

            @param          hash_table, filename, time_limit
            @pre            filename must be in .txt
            @post           the time taken to read the file passed time_limit
            @complexity     best case: O(1) empty file
                            worse case: O(n*m) where n size of the file and m is the complexity of the hash table
                                        function that was called

     """

    start = timeit.default_timer()
    with open(filename, 'r') as file:
        for line in file:
            item = line.strip('\n')
            hash_table[item] = 1
            end = (timeit.default_timer() - start)
            if time_limit is not None and end > time_limit:
                raise Exception
        file.close()

    return end


def load_dictionary_time(hash_base, table_size, filename, max_time):
    """
            This function calls load dictionary function and times how long the function takes to run

            @param          hash_base, table_size, filename, max_time
            @pre            filename must be in .txt
            @post           the time taken to read the file passed time_limit
            @complexity     best case: O(1) empty file
                            worse case: O(n*m) where n size of the file and m is the complexity of the hash table
                                        function that was called

     """
    table = task1.HashTable(table_size,hash_base)
    try:
        start = timeit.default_timer()
        load_dictionary(table, filename, max_time)
        end = (timeit.default_timer() - start)
        return (table.count, end)
    except TimeoutError:
        return (table.count,None)



def table_dictionary_time(max_time):
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
    dic = ["english_small.txt","english_large.txt","french.txt"]

    with open('output_task2.csv', 'w') as openFile:  # create csv file

        writer = csv.writer(openFile)
        writer.writerow(['Dic','Tablesize', 'b', 'No. of words', 'time taken'])

        for i in range((len(dic))):
            counter = 0
            counter2 = 0
            for k in range(len(b)*len(tablesize)):
                base = b[counter2]
                table_Size = tablesize[counter]
                print(base, table_Size)
                word_n_time = load_dictionary_time(base, table_Size, dic[i], max_time)
                counter += 1

                if counter == 3:
                    counter = 0
                print(word_n_time)

                if word_n_time[1] is None:
                    writer.writerow([dic[i], table_Size, base, word_n_time[0],(max_time+10)])
                else:
                    writer.writerow([dic[i], table_Size, base, word_n_time[0], word_n_time[1]])

                if counter == 0:
                    counter2 += 1

