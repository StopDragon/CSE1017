# -*- coding: utf-8 -*-
def findAllSentences(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    c = 0# 문장에 나오는 횟수
    cs = 0# 문장 갯수
    sentence = 0# key값이 발견된 문장
    count = 0# key값이 나온 총 문장 수
    while True:
        dtext = text.find('.')
        qtext = text.find('?')
        if dtext == -1 and qtext == -1:
            break
        if dtext < qtext or dtext != -1 and qtext == -1 :
            if text.find(key) != -1:
                outfile.write("'" + key + "'" + ' appears ' + c + ' time.\n' + sentence + '\n')
                count = count + 1
                cs = cs + 1
                c = 1
            else:
                None

        elif dtext > qtext or dtext == -1 and qtext != -1:
            if text.find(key) != -1:
                outfile.write("'" + key + "'" + ' appears ' + c + ' time.\n' + sentence + '\n')
                count = count + 1
                cs = cs + 1
                c = 1
            else:
                None
    outfile.write("'" + key + "'" + 'appears' + count + 'times in' + cs + 'sentences.\n')
    outfile.close()
    infile.close()
print("done")
findAllSentences('article.txt','apple')
