# -*- coding: utf-8 -*-
def findAllNCount(filename,key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    count = 0
    if position == -1:
        outfile.write(key + ' is not found')
    else:
        while position != -1:
            lastkey, count = position + 1, count + 1
            position = text.find(key,lastkey)
        else:
            if count == 1:
                outfile.write(key + " is found " + str(count) + " time.\n")
            else:
                outfile.write(key + " is found " + str(count) + " times.\n")
    outfile.close()
    infile.close()
print("Done")
