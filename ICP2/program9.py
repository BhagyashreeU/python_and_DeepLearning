wordCountDict = dict()                                          # create WordCountDict dictonary
inputContent = []

def getCount():
    with open("inputFile.txt", "r") as infile:   # open text file using with open (it automatically closes file once control comes out of block)
        for line in infile:
            inputContent.append(line)                      # save contents of inputfile
            line = line.strip()                            # removes leading and trailing spaces
            line = line.lower()                            # converts characters  to lower case
            words = line.split(" ")                        # divides line into list of words

            '''
            checking if encountered word is present in dictionary if it is there then
            increment count of word by 1 otherwise, add word to dictionary and set count as 1 
            '''

            for word in words:
                if word in wordCountDict:
                    wordCountDict[word] = wordCountDict[word] + 1
                else:
                    wordCountDict[word] = 1
getCount()

with open("output.txt", "w") as outfile:  # using with open function opening output.txt in write mode
    outfile.writelines(inputContent)      # writes contents of inputfile
    outfile.write("\n\nWord Count: \n")
    for key in wordCountDict:                                           # iterating dictonary
        outfile.writelines(key + ':' +  str(wordCountDict[key])+ "\n")  # writing both key and values of dictonary in output file