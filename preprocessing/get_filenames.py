#encoding=utf-8
import os
import codecs

for dirPath, dirNames, fileNames in os.walk("D:\Test"):
    print fileNames
    x = fileNames

f = codecs.open("fileNames.txt", "w")
for i in x:
    iStr = str(i) + '\n'
    f.write(iStr)
f.close()

