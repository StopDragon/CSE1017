# -*- coding: utf-8 -*-
import random
def testSearchWidestGap():
    db = random.sample(range(500),100)
    print("Searching the widest gap...")
    db.sort()
    print(db)
    index, gap = searchWidestGap(db)
    print("The widest gap is:", gap)
    print("between", db[index], "and", db[index+1])
    print("at", index)
