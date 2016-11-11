#encoding=utf-8
import codecs

def OneWordSearch(query):
    positionalFile = codecs.open('../source/PositionalList.txt', 'r')
    allLines = positionalFile.readlines()
    positionalFile.close()
    inList = 0
    allCount = 0
    docIDArr = []
    docCountArr = []
    ansStr = ""
    for line in allLines:
        thisIndex = line[:line.find('#')]
        if query == thisIndex:
            inList = 1
            line = line.strip()
            docFirstIndex = []
            while line.find('#') != -1:
                docIDArr.append(int(line[line.find('#')+1:line.find('$')]))
                docCountArr.append(int(line[line.find('$')+1:line.find('&')]))
                line = line[line.find('&'):]
                if line.find('#') != -1 and line.find('-') != -1 and line.find('-') < line.find('#'):
                    docFirstIndex.append(int(line[line.find('&')+1:line.find('-')]))
                    line = line[line.find('#'):]
                elif line.find('#') != -1:
                    docFirstIndex.append(int(line[line.find('&')+1:line.find('#')]))
                    line = line[line.find('#'):]
                elif line.find('-') != -1:
                    docFirstIndex.append(int(line[line.find('&')+1:line.find('-')]))
                else:
                    docFirstIndex.append(int(line[line.find('&')+1:line.find('@')]))
            for i in xrange(len(docIDArr)-1):
                for j in xrange(len(docIDArr)-1-i):
                    if docCountArr[j] < docCountArr[j+1]:
                        docCountArr[j] ^= docCountArr[j+1]
                        docCountArr[j+1] ^= docCountArr[j]
                        docCountArr[j] ^= docCountArr[j+1]
                        docIDArr[j] ^= docIDArr[j+1]
                        docIDArr[j+1] ^= docIDArr[j]
                        docIDArr[j] ^= docIDArr[j+1]
                        docFirstIndex[j] ^= docFirstIndex[j+1]
                        docFirstIndex[j+1] ^= docFirstIndex[j]
                        docFirstIndex[j] ^= docFirstIndex[j+1]
            for i in xrange(len(docIDArr)):
                ansStr += "@" + str(docIDArr[i])
            ansStr += "$" + str(sum(docCountArr))
            break

    if inList == 0:
        for docNum in xrange(1,1201):
            filePath = '../articles' + str(docNum) + '.txt'
            docFile = open(filePath, 'r')
            docAllLine = docFile.readlines()
            docLine = ""
            for ss in docAllLine:
                docLine += ss.strip()
            if docLine.find(query) != -1:
                docIDArr.append(docNum)
                docCountArr.append(docLine.count(query))
            docFile.close()

        if len(docIDArr) == 0:
            ansStr = "NOT FOUND"
        else:
            for i in xrange(len(docIDArr)-1):
                for j in xrange(len(docIDArr)-1-i):
                    if docCountArr[j] < docCountArr[j+1]:
                        docCountArr[j] ^= docCountArr[j+1]
                        docCountArr[j+1] ^= docCountArr[j]
                        docCountArr[j] ^= docCountArr[j+1]
                        docIDArr[j] ^= docIDArr[j+1]
                        docIDArr[j+1] ^= docIDArr[j]
                        docIDArr[j] ^= docIDArr[j+1]
            for i in xrange(len(docIDArr)):
                ansStr += "@" + str(docIDArr[i]) #
            ansStr += "$" + str(sum(docCountArr))
    return ansStr


def MulWordSearch(query):
    searchArr = []
    while query.find(' ') != -1:
        searchArr.append(query[:query.find(' ')])
        query = query[query.find(' ')+1:]
    searchArr.append(query)
    positionalFile = codecs.open('../source/PositionalList.txt', 'r')
    allLines = positionalFile.readlines()
    positionalFile.close()
    allDocID = []
    allDocQueryCount = []
    allDocFreCount = []
    for i in xrange(len(searchArr)):
        inList = 0
        docIDArr = []
        docCountArr = []
        for line in allLines:
            thisIndex = line[:line.find('#')]
            if searchArr[i] == thisIndex:
                inList = 1
                line = line.strip()
                while line.find('#') != -1:
                    docIDArr.append(int(line[line.find('#')+1:line.find('$')]))
                    docCountArr.append(int(line[line.find('$')+1:line.find('&')]))
                    line = line[line.find('&')+1:]
                break
        if inList == 0:
            for docNum in xrange(1,1201):
                filePath = '../articles/' + str(docNum) + '.txt'
                docFile = open(filePath, 'r')
                docAllLine = docFile.readlines()
                docLine = ""
                for ss in docAllLine:
                    docLine += ss.strip()
                if ss.find(query) != -1:
                    docIDArr.append(docNum)
                    docCountArr.append(docLine.count(thisIndex))
                docFile.close()

        if len(docIDArr) != 0:
            for j in xrange(len(docIDArr)):
                if allDocID.count(docIDArr[j]) == 0:
                    allDocID.append(docIDArr[j])
                    allDocQueryCount.append(1)
                    allDocFreCount.append(docCountArr[j])
                else:
                    allDocQueryCount[allDocID.index(docIDArr[j])] += 1
                    allDocFreCount[allDocID.index(docIDArr[j])] += docCountArr[j]
    for i in xrange(len(allDocID)):
        for j in xrange(len(allDocID)-1-i):
            if allDocQueryCount[j] < allDocQueryCount[j+1]:
                allDocID[j] ^= allDocID[j+1]
                allDocID[j+1] ^= allDocID[j]
                allDocID[j] ^= allDocID[j+1]
                allDocQueryCount[j] ^= allDocQueryCount[j+1]
                allDocQueryCount[j+1] ^= allDocQueryCount[j]
                allDocQueryCount[j] ^= allDocQueryCount[j+1]
                allDocFreCount[j] ^= allDocFreCount[j+1]
                allDocFreCount[j+1] ^= allDocFreCount[j]
                allDocFreCount[j] ^= allDocFreCount[j+1]
            elif allDocQueryCount[j] == allDocQueryCount[j+1] and allDocFreCount[j] < allDocFreCount[j+1]:
                allDocID[j] ^= allDocID[j+1]
                allDocID[j+1] ^= allDocID[j]
                allDocID[j] ^= allDocID[j+1]
                allDocQueryCount[j] ^= allDocQueryCount[j+1]
                allDocQueryCount[j+1] ^= allDocQueryCount[j]
                allDocQueryCount[j] ^= allDocQueryCount[j+1]
                allDocFreCount[j] ^= allDocFreCount[j+1]
                allDocFreCount[j+1] ^= allDocFreCount[j]
                allDocFreCount[j] ^= allDocFreCount[j+1]
    ansStr = ""
    if len(allDocID) == 0:
        ansStr = "NOT FOUND"
    else:
        for i in xrange(len(allDocID)):
            ansStr += "@" + str(allDocID[i])
    return ansStr


def proximitySearch(query):
    searchArr = []
    searchArr.append(query[:query.find(' ')])
    query = query[query.find(' ')+1:]
    distance = int(query[query.find('/')+1:query.find(' ')])
    searchArr.append(query[query.find(' ')+1:])

    positionalFile = codecs.open('../source/PositionalList.txt', 'r')
    allLines = positionalFile.readlines()
    positionalFile.close()
    searchPosArr = []
    allDocID = []
    allDocQueryCount = []
    allDocFreCount = []
    for i in xrange(len(searchArr)):
        inList = 0
        docIDArr = []
        docCountArr = []
        for line in allLines:
            thisIndex = line[:line.find('#')]
            if searchArr[i] == thisIndex:
                searchPosArr.append(line)
                inList = 1
                line = line.strip()
                while line.find('#') != -1:
                    docIDArr.append(int(line[line.find('#')+1:line.find('$')]))
                    docCountArr.append(int(line[line.find('$')+1:line.find('&')]))
                    line = line[line.find('&')+1:]
                break
        if inList == 0:
            for docNum in xrange(1,1201):
                filePath = '../articles/' + str(docNum) + '.txt'
                docFile = open(filePath, 'r')
                docAllLine = docFile.readlines()
                docLine = ""
                for ss in docAllLine:
                    docLine += ss.strip()
                if ss.find(query) != -1:
                    docIDArr.append(docNum)
                    docCountArr.append(docLine.count(thisIndex))
                docFile.close()

        if len(docIDArr) != 0:
            for j in xrange(len(docIDArr)):
                if allDocID.count(docIDArr[j]) == 0:
                    allDocID.append(docIDArr[j])
                    allDocQueryCount.append(1)
                    allDocFreCount.append(docCountArr[j])
                else:
                    allDocQueryCount[allDocID.index(docIDArr[j])] += 1
                    allDocFreCount[allDocID.index(docIDArr[j])] += docCountArr[j]

    bothQueryDocID = []
    for i in xrange(len(allDocID)):
        if allDocQueryCount[i] == 2:
            bothQueryDocID.append(allDocID[i])
    ansQueryID = []
    for i in xrange(len(bothQueryDocID)):
        searchPosArr[0] = searchPosArr[0][searchPosArr[0].find("#"+str(bothQueryDocID[i]))+1+len(str(bothQueryDocID[i])):]
        searchPosArr[1] = searchPosArr[1][searchPosArr[1].find("#"+str(bothQueryDocID[i]))+1+len(str(bothQueryDocID[i])):]
        if searchPosArr[0].find('#') == -1:
            str1 = searchPosArr[0][searchPosArr[0].find('&')+1:searchPosArr[0].find('@')] + "-"
        else:
            str1 = searchPosArr[0][searchPosArr[0].find('&')+1:searchPosArr[0].find('#')] + "-"
        if searchPosArr[1].find('#') == -1:
            str2 = searchPosArr[1][searchPosArr[1].find('&')+1:searchPosArr[1].find('@')] + "-"
        else:
            str2 = searchPosArr[1][searchPosArr[1].find('&')+1:searchPosArr[1].find('#')] + "-"
        loc1 = []
        loc2 = []
        while True:
            loc1.append(int(str1[:str1.find('-')]))
            if str1.count('-') > 1:
                str1 = str1[str1.find('-')+1:]
            else:
                break
        while True:
            loc2.append(int(str2[:str2.find('-')]))
            if str2.count('-') > 1:
                str2 = str2[str2.find('-')+1:]
            else:
                break
        for m in loc1:
            for n in loc2:
                if (n - m) > 0 and (n - m) <= (len(searchArr[0]) + distance*3):
                    ansQueryID.append(bothQueryDocID[i])

    ansQueryCount = []
    for i in xrange(len(ansQueryID)):
        ansQueryCount.append(allDocFreCount[allDocID.index(ansQueryID[i])])
    for i in xrange(len(ansQueryID)):
        for j in xrange(len(ansQueryID)-1-i):
            if ansQueryCount[j] < ansQueryCount[j+1]:
                ansQueryID[j] ^= ansQueryID[j+1]
                ansQueryID[j+1] ^= ansQueryID[j]
                ansQueryID[j] ^= ansQueryID[j+1]
                ansQueryCount[j] ^= ansQueryCount[j+1]
                ansQueryCount[j+1] ^= ansQueryCount[j]
                ansQueryCount[j] ^= ansQueryCount[j+1]

    ansNoDoubleID = []
    for i in ansQueryID:
        if ansNoDoubleID.count(i) == 0:
            ansNoDoubleID.append(i)

    ansStr = ""
    if len(ansNoDoubleID) == 0:
        ansStr = "NOT FOUND"
    else:
        for ans in ansNoDoubleID:
            ansStr += "@" + str(ans)
    return ansStr


def BooleanSearch(query):
    line = query + ' '
    searchArr = []
    while True:
        searchArr.append(line[:line.find(' ')])
        if line.count(' ') > 1:
            line = line[line.find(' ')+1:]
        else:
            break
    notArr = []
    while searchArr.count("not") > 0:
        num = 0
        for k in xrange(searchArr.index("not")):
            if searchArr[k] != "and" and searchArr[k] != "or":
                num += 1
        notArr.append(num)
        searchArr.remove("not")
    andArr = []
    while searchArr.count("and") > 0:
        num = 0
        for k in xrange(searchArr.index("and")):
            if searchArr[k] != "or":
                num += 1
        andArr.append(num)
        searchArr.remove("and")
    orArr = []
    while searchArr.count("or") > 0:
        num = 0
        for k in xrange(searchArr.index("or")):
            num += 1
        orArr.append(num)
        searchArr.remove("or")

    searchTDArr = []
    for i in xrange(len(searchArr)):
        TDfile = codecs.open('../source/TDmatrix.txt', 'r')
        allLines = TDfile.readlines()
        TDfile.close()
        inMatrix = 0
        for line in allLines:
            thisIndex = line[:line.find(',')]
            if searchArr[i] == thisIndex:
                searchTDArr.append(line)
                inMatrix = 1
                break
        if inMatrix == 0:
            thisIndex = searchArr[i]
            for docNum in xrange(1,1201):
                filePath = '../articles/' + str(docNum) + '.txt'
                f = open(filePath, 'r')
                docAllLine = f.readlines()
                f.close()
                count = 0
                for ss in docAllLine:
                    count += ss.count(searchArr[i])
                thisIndex += ',' + str(count)
            searchTDArr.append(thisIndex)

    if len(notArr) != 0:
        for i in xrange(len(notArr)):
            oldLine = searchTDArr[notArr[i]]
            newLine = oldLine[:oldLine.find(',')]
            oldLine = oldLine[oldLine.find(',')+1:] + ','
            while oldLine.find(',') != -1:
                num = int(oldLine[:oldLine.find(',')])
                if num == 0:
                    newLine += ',1'
                else:
                    newLine += ',0'
                if oldLine.count(',') == 1:
                    break
                else:
                    oldLine = oldLine[oldLine.find(',')+1:]
            searchTDArr[notArr[i]] = newLine

    if len(andArr) != 0:
        for i in xrange(len(andArr)):
            andResult = ""
            str1 = searchTDArr[andArr[i]].strip()
            str2 = searchTDArr[andArr[i]-1].strip()
            left = 1
            while str2 == "":
                left += 1
                str2 = searchTDArr[andArr[i]-left].strip()
            str1 = str1[str1.find(',')+1:] + ","
            str2 = str2[str2.find(',')+1:] + ","
            for j in xrange(1200):
                num1 = int(str1[:str1.find(',')])
                num2 = int(str2[:str2.find(',')])
                if num1 > 0 and num2 > 0:
                    andResult += ',' + str(num1+num2)
                else:
                    andResult += ',0'
                str1 = str1[str1.find(',')+1:]
                str2 = str2[str2.find(',')+1:]
            searchTDArr[andArr[i]-left] = andResult
            searchTDArr[andArr[i]] = ""

    if len(orArr) != 0:
        for i in xrange(len(orArr)):
            orResult = ""
            str1 = searchTDArr[orArr[i]].strip()
            str2 = searchTDArr[orArr[i]-1].strip()
            left = 1
            while str2 == "":
                left += 1
                str2 = searchTDArr[orArr[i]-left].strip()
            str1 = str1[str1.find(',')+1:] + ","
            str2 = str2[str2.find(',')+1:] + ","
            for j in xrange(1200):
                num1 = int(str1[:str1.find(',')])
                num2 = int(str2[:str2.find(',')])
                orResult += ',' + str(num1+num2)
                str1 = str1[str1.find(',')+1:]
                str2 = str2[str2.find(',')+1:]
            searchTDArr[orArr[i]-left] = orResult
            searchTDArr[orArr[i]] = ""

    ansIDArr = ""
    ansQueryID = []
    ansQueryCount = []
    for i in xrange(len(searchTDArr)):
        if searchTDArr[i] != "":
            thisLine = searchTDArr[i][searchTDArr[i].find(',')+1:].strip() + ","
            for docID in xrange(1,1201):
                num = int(thisLine[:thisLine.find(',')])
                if num > 0:
                    #
                    ansQueryID.append(docID)
                    ansQueryCount.append(num)
                thisLine = thisLine[thisLine.find(',')+1:]
            break
    
    for i in xrange(len(ansQueryID)-1):
        for j in xrange(len(ansQueryID)-1-i):
            if ansQueryCount[j] < ansQueryCount[j+1]:
                ansQueryCount[j] ^= ansQueryCount[j+1]
                ansQueryCount[j+1] ^= ansQueryCount[j]
                ansQueryCount[j] ^= ansQueryCount[j+1]
                ansQueryID[j] ^= ansQueryID[j+1]
                ansQueryID[j+1] ^= ansQueryID[j]
                ansQueryID[j] ^= ansQueryID[j+1]
    for docID in ansQueryID:
        ansIDArr += "@" + str(docID)
    return ansIDArr


if __name__ == '__main__':
    queryFile = codecs.open('../temp/query.txt', 'r')
    queryLine = queryFile.readline()
    queryLine = queryLine.strip()
    queryFile.close()
    result = open('../temp/output.txt' , 'w');
    queryResult = ""
    if queryLine.find('OR') == -1 and queryLine.find('or') == -1 and queryLine.find('NOT') == -1 and queryLine.find('not') == -1 and queryLine.find('AND') == -1 and queryLine.find('and') == -1 and queryLine.find('/') == -1:
        if queryLine.find(' ') == -1:
            queryResult = OneWordSearch(queryLine)
        else:
            queryResult = MulWordSearch(queryLine)
    else:
        if queryLine.find('/') != -1:
            queryResult = proximitySearch(queryLine)
        else:
            queryResult = BooleanSearch(queryLine)

    result.write(queryResult);
