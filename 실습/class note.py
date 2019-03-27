# -*- coding: utf-8 -*-
def smallerOdd(x,y):
            if x>y :
                if y%2==1 :
                    return y
                if x%2==1 and y%2==0 :
                    return x
            elif x<=y :
                if x%2==1 and y%2==0 :
                    return x
                if x%2==0 and y%2==1 :
                    return y
                if x%2==1 and x%2==1 :
                    return x
            else :
                return None
def smallestOdd(x,y,z):
    if smallerOdd(x,y) >z:
        if z%2==1:
            return z
        if z%2==0 :
            return smallerOdd(x,y)
    elif smallerOdd(x,y) <z:
        if z%2==0 :
            return smallerOdd(x,y)
        if z%2==1 :
            return smallerOdd(x,y)
    else:
        return None
print(smallestOdd(3,2,2)) # returns 3
print(smallestOdd(3,5,7)) # returns 3
print(smallestOdd(3,5,1)) # returns 1
print(smallestOdd(8,3,4)) # returns 3
print(smallestOdd(8,3,5)) # returns 3
print(smallestOdd(8,5,3)) # returns 3
print(smallestOdd(2,8,3)) # returns 3
print(smallestOdd(2,8,4)) # returns None
