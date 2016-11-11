#encoding=utf-8
import codecs

indexFile = codecs.open('source/index_all.txt', 'r')
outputFile = codecs.open('source/PositionalList_new.txt', 'w', encoding='utf-8')


allLines = indexFile.readlines()
indexNum = 1
for thisIndex in allLines:
    print thisIndex
    thisIndex = thisIndex.strip()
    print thisIndex
    print indexNum
    indexNum += 1
    outputFile.write(thisIndex.decode('utf-8'))
    indexAllDoc = 0
    for docNum in xrange(1,1201):
        thisDocExi = 0
        filePath = '../articles' + str(docNum) + '.txt'
        f = open(filePath, 'r')
        docAllLine = f.readlines()
        ss = ""
        for i in docAllLine:
            ss += i.strip()

        if ss.find(thisIndex) != -1:
            indexAllDoc += ss.count(thisIndex)
            outputFile.write('#' + str(docNum))
            outputFile.write('$' + str(ss.count(thisIndex)))
            outputFile.write('&' + str(ss.find(thisIndex)))
            accu = ss.find(thisIndex)
            ss = ss[ss.find(thisIndex)+2:]
            while ss.find(thisIndex) != -1:
                outputFile.write('-' + str(ss.find(thisIndex)+accu+2))
                accu += ss.find(thisIndex) + 2
                ss = ss[ss.find(thisIndex)+2:]
        f.close()

    outputFile.write('@' + str(indexAllDoc) + '\n')

indexFile.close()
outputFile.close()
