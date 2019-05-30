# -*- coding: utf-8 -*-
def radixsort(ds,length):
    master=[[],[],[],[],[],[],[],[],[],[]]
    for x in range(length-1,-1,-1):
        for y in ds:
            for z in y[x]:
                master[int(z)] = master[int(z)] + [y]
        ds[:]=[]
        for w in master:
            ds = ds + w
        master=[[],[],[],[],[],[],[],[],[],[]]
    return ds
