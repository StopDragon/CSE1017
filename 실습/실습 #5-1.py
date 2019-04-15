# -*- coding: utf-8 -*-
def findLast(filename,key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    keyresult = text.find(key)
    if keyresult == -1:
        outfile.write(key + " is not found.\n")
    else:
        while keyresult != -1:
            lastkey = keyresult + 1
            keyresult = text.find(key,lastkey)
        return outfile.write(key + " is at " + str(lastkey-1) + " the last time.\n")
    outfile.close()
    infile.close()
print("Done")
