# -*- coding: utf-8 -*-
def oneSentencePerLine(filename) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    count = 0
    while True:
        dtext = text.find('.')
        qtext = text.find('?')
        if dtext == -1 and qtext == -1:
            outfile.write("There are " + str(count) + " sentences in total.\n")
            break
        elif dtext < qtext or dtext != -1 and qtext == -1 :
            part = text.partition('.')
            outfile.write(part[0].strip() + part[1] + '\n\n')
        elif dtext > qtext or dtext == -1 and qtext != -1:
            part = text.partition('?')
            outfile.write(part[0].strip() + part [1] + '\n\n')
        text = part[2].strip()
        count += 1
    outfile.close()
    infile.close()
print("Done")
