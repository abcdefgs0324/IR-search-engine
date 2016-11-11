#encoding=utf-8
import jieba
import codecs

jieba.set_dictionary('D:/Anaconda/Lib/site-packages/jieba/extra_dict/dict.txt.big')

fiNames = codecs.open('source/fileNames_utf8.txt', 'r')

for count in xrange(1200):
    name = fiNames.readline()
    if name == '':
        break
    name = name.strip()
    name = name[name.find('2')+1:]
    print '2' + name
    filePath = '../articles/'
    filePath += u'聯2' + name
    # print filePath

    f = open(filePath, 'r')
    ss = ""
    while True:
        i = f.readline()
        if i == '':
            break
        ss += i

    cut = jieba.cut_for_search(ss)
    # x = iter(cut)
    z = list(cut)
    x_length = sum(1 for _ in z)
    print x_length
    # x = iter(cut)

    op = codecs.open("source/index.txt", "a", encoding='utf-8')
    # y = x.next()
    for y in z:
        op.write(y+",\n")
        # y = x.next()
    op.close()

