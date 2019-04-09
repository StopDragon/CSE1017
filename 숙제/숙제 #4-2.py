# -*- coding: utf-8 -*-
def radixsort(ds,length):
    n=[[],[],[],[],[],[],[],[],[],[]]
    nn=[[],[],[],[],[],[],[],[],[],[]]
    nnn=[[],[],[],[],[],[],[],[],[],[]]
    l=[[],[],[],[],[],[],[],[],[],[]]
    if ds!=[]:
        while length >= 1:
            for a in [ds]: #일의 자리 수
                if a[-1] == '0':
                    a[-1] = n[0]
                elif a[-1] == '1':
                    a[-1] = n[1]
                elif a[-1] == '2':
                    a[-1] = n[2]
                elif a[-1] == '3':
                    a[-1] = n[3]
                elif a[-1] == '4':
                    a[-1] = n[4]
                elif a[-1] == '5':
                    a[-1] = n[5]
                elif a[-1] == '6':
                    a[-1] = n[6]
                elif a[-1] == '7':
                    a[-1] = n[7]
                elif a[-1] == '8':
                    a[-1] = n[8]
                elif a[-1] == '9':
                    a[-1] = n[9]

            for aa in [ds]: #십의 자리 수
                if aa[-2] == '0':
                    aa[-2] = nn[0]
                elif aa[-2] == '1':
                    aa[-2] = nn[1]
                elif aa[-2] == '2':
                    aa[-2] = nn[2]
                elif aa[-2] == '3':
                    aa[-2] = nn[3]
                elif aa[-2] == '4':
                    aa[-2] = nn[4]
                elif aa[-2] == '5':
                    aa[-2] = nn[5]
                elif aa[-2] == '6':
                    aa[-2] = nn[6]
                elif aa[-2] == '7':
                    aa[-2] = nn[7]
                elif aa[-2] == '8':
                    aa[-2] = nn[8]
                elif aa[-2] == '9':
                    aa[-2] = nn[9]

            for aaa in [ds]: #백의 자리 수
                if aaa[-2] == '0':
                    aaa[-2] = nnn[0]
                elif aaa[-2] == '1':
                    aaa[-2] = nnn[1]
                elif aaa[-2] == '2':
                    aaa[-2] = nnn[2]
                elif aaa[-2] == '3':
                    aaa[-2] = nnn[3]
                elif aaa[-2] == '4':
                    aaa[-2] = nnn[4]
                elif aaa[-2] == '5':
                    aaa[-2] = nnn[5]
                elif aaa[-2] == '6':
                    aaa[-2] = nnn[6]
                elif aaa[-2] == '7':
                    aaa[-2] = nnn[7]
                elif aaa[-2] == '8':
                    aaa[-2] = nnn[8]
                elif aaa[-2] == '9':
                    aaa[-2] = nnn[9]
        e
            for aaaa in [ds]: #천의 자리 수
                if aaaa[-2] == '0':
                    aaaa[-2] = l[0]
                elif aaaa[-2] == '1':
                    aaaa[-2] = l[1]
                elif aaaa[-2] == '2':
                    aaaa[-2] = l[2]
                elif aaaa[-2] == '3':
                    aaaa[-2] = l[3]
                elif aaaa[-2] == '4':
                    aaaa[-2] = l[4]
                elif aaaa[-2] == '5':
                    aaaa[-2] = l[5]
                elif aaaa[-2] == '6':
                    aaaa[-2] = l[6]
                elif aaaa[-2] == '7':
                    aaaa[-2] = l[7]
                elif aaaa[-2] == '8':
                    aaaa[-2] = l[8]
                elif aaaa[-2] == '9':
                    aaaa[-2] = l[9]

        return l
    else:
        return []



print(radixsort([],3))
# []
print(radixsort(["239"],3))
# ['239']
print(radixsort(["170",'045','075','090','002','024','802','066'],3))
# ['002', '024', '045', '066', '075', '090', '170', '802']
print(radixsort(["239",'234','879','878','123','358','416','317','137','225'],3))
# ['123', '137', '225', '234', '239', '317', '358', '416', '878', '879']
print(radixsort(["0508", "0515", "1225", "0915", "1111", "0101", "0318", "0301", "0815"],4))
# ['0101', '0301', '0318', '0508', '0515', '0815', '0915', '1111', '1225']
