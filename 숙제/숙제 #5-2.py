# -*- coding: utf-8 -*-
import random
def testBinSearchClosest():
    db = random.sample(range(500),100)
    print("Binary search closest function test")
    db.sort()
    print(db)
    for _ in range(10):
        key = random.randrange(500)
        index = binSearchClosest(db, key)
        print("The closest value to", key, ":", db[index], "at index", index)
