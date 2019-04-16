# -*- coding: utf-8 -*-
def findAllSentences(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    count = 0
    while True:
        idx = text.find('.')
        part = text.partition('.')
        if idx == -1 and part[0].find(key) == -1:
            outfile.write("'" + key + "' appears " + str(count) + ' times in ' + str(count) + ' sentences.\n')
            break
        if part[0].find(key) != -1:
            outfile.write("'" + key + "'" + ' appears 1 time.\n')
            outfile.write(part[0].strip() + '.\n\n')
            count += 1
        text = part[2].strip()
    return
    outfile.close()
    infile.close()
print("done")
