import os
import math
import re


class docIndex:
    def __init__(Index):
        Index.createVariables()
        Index.createIndex()

    def createVariables(Index):
        Index.path = os.curdir
        Index.files = os.listdir(Index.path + '/data')

        Index.index = {}
        
        List = sorted(Index.index)
        Dictionary = {}
        for key in List:
            Dictionary[key] = Index.index[key]
        
        Index.stopList = []
        for word in open(Index.path + '/' + "stoplist.txt"):
            Index.stopList.append(word.strip())


        Index.index = Dictionary
        Index.documentIndex = {}

    def createIndex(Index):

        for Files in Index.files:

            Path1 = open(Index.path + '/data/' + Files)
            for line in Path1:
                
                readTerms = line.strip()
                readTerms = line.rstrip("\x00")
                readTerms = re.split('[ -/?.:;!\%\x00]', readTerms)

                if Files not in Index.documentIndex:
                    Index.documentIndex[Files] = len(readTerms)
                else:
                    Index.documentIndex[Files] += len(readTerms)

                for term in readTerms:
                    lower = term.lower()
                    lower = lower.strip()

                    if not lower in Index.stopList:
                        if lower in Index.index:

                            if Files in Index.index[lower][1]:
                                Index.index[lower][1][Files] += 1
                            else:
                                Index.index[lower][1][Files] = 1
                        else:
                            index = [1,{}]
                            Index.index[lower] = index
                            Index.index[lower][1][Files] = 1
                        Index.index[lower][0] = len(Index.index[lower][1])

    def Test(Index):
        print("Enter query surrounded by quotation marks, Enter ''quit'' to exit")

        while True:
            query = input(': ')
            query = query.lower()
            if query == "quit":
                return
            if query in Index.index:
                print("(Posting, TF, IDF, TF-IDF)")
                for posting in Index.index[query][1]:
                    tf = (float(Index.index[query][1][posting]))/(Index.documentIndex[posting])
                    idf = math.log(len(Index.documentIndex)/(Index.index[query][0]))
                    strOutput1 = str(tf)
                    strOutput2 = str(idf)
                    strOutput3 = str((tf*idf))
                    Output = ((posting), strOutput1, strOutput2, strOutput3)
                    print(Output)
            else:
                print("The Input does not exist, try again")
def main():
    Output = docIndex()
    Output.Test()

    return 0
if __name__ == "__main__":
    main()
