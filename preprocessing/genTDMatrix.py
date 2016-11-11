#encoding=utf-8
import codecs

indexFile = codecs.open('source/index_all.txt', 'r')
outputFile = codecs.open('source/TDmatrix.txt', 'w', encoding='utf-8')

for i in range(1,1201):
    outputFile.write(',' + str(i))

allLines = indexFile.readlines()
for thisIndex in allLines:
    print thisIndex.strip()
    thisIndex = thisIndex.strip()
    print thisIndex
    outputFile.write('\n' + thisIndex.decode('utf-8'))
    for docNum in xrange(1,1201):
        filePath = '../articles' + str(docNum) + '.txt'
        f = open(filePath, 'r')
        count = 0
        ss = ""
        docAllLine = f.readlines()
        for i in docAllLine:
            count += i.count(thisIndex)
        outputFile.write(',' + str(count))
        f.close()
        print count





indexFile.close()
outputFile.close()
