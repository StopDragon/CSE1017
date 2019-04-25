# -*- coding: utf-8 -*-
def findAll(filename,key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    if position == -1:
        outfile.write(key + ' is not found.\n')
    else:
        while position != -1:
            lastkey = position + 1
            position = text.find(key,lastkey)
            outfile.write(key + " is at " + str(lastkey-1) + '.\n')
        return
    outfile.close()
    infile.close()
print("Done")
