from task2 import ListADT

def read_text_file(name):
    """
                    Reads the text file and return the content of the file in a list

                    @param          name of the file
                    @pre            none
                    @post           an array is created
                    @complexity     best case: O(n)
                                    worse case: O(n)

    """
    listadt = ListADT()
    with open(name,'r') as file:
        #files = file.read().splitlines()
        for line in file:
            item = line.strip('\n')
            listadt.append(item)
        file.close()
    return listadt

#print(read_text_file('TestFile.txt'))





