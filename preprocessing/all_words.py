#coding=utf-8
#encoding=utf-8
import codecs

fiNames = codecs.open('source/fileNames_utf8.txt', 'r')

for count in xrange(1200):
    name = fiNames.readline()
    name = name.strip()
    name = name[name.find('2')+1:]
    print '2' + name
    filePath = '../articles/'
    filePath += u'聯2' + name

    f = open(filePath, 'r')
    ss = ""
    while True:
        i = f.readline()
        if i == '':
            break
        ss += i.strip()

    op = codecs.open("source/index_one_word.txt", "a", encoding='utf-8')

    print ss.decode('utf-8')

    op.close()

