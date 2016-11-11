#encoding=utf-8
import codecs

fiNames = codecs.open('source/fileNames_utf8.txt', 'r')

count = 1
while count < 1201:
    name = fiNames.readline()
    if name == '':
        break
    name = name.strip()
    name = name[name.find('2')+1:]
    print '2' + name
    filePath = '../articles'
    filePath += u'聯2' + name

    f = open(filePath, 'r')
    outPath = '../articles_transfer' + str(count) + ".txt"
    out = codecs.open(outPath, 'w', encoding='utf-8')

    while True:
        i = f.readline()
        if i == '':
            break
        out.write(i.decode('utf-8'))

    out.close()
    f.close()

    print count
    count += 1




fiNames.close()


