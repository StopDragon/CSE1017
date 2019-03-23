# -*- coding: utf-8 -*-
def smallerOdd(x,y):
    if x % 2 == 1 and y % 2 == 1:
        if x >= y:
            return y
        elif x < y:
            return x
    elif x % 2 == 1 and y % 2 != 1:
        return x
    elif x % 2 != 1 and y % 2 == 1:
        return y
    else:
        return None

def smallestOdd(x,y,z):
    if z % 2 == 1:
        if x % 2 != 1 and y % 2 != 1:
            return z
        elif smallerOdd(x,y) >= z:
            return z
        elif smallerOdd(x,y) < z:
            return smallerOdd(x,y)
    elif z % 2 != 1:
        return smallerOdd(x,y)
    elif z % 2 != 1 and smallerOdd(x,y) % 2 != 1:
        return None
print(smallestOdd(3,2,2)) # returns 3
print(smallestOdd(3,5,7)) # returns 3
print(smallestOdd(3,5,1)) # returns 1
print(smallestOdd(8,3,4)) # returns 3
print(smallestOdd(8,3,5)) # returns 3
print(smallestOdd(8,5,3)) # returns 3
print(smallestOdd(2,8,3)) # returns 3
print(smallestOdd(2,8,4)) # returns None
