# -*- coding: utf-8 -*-
def smallest(x,y,z):
    if x >= y >= z:
        return z
    elif x >= z >= y:
        return y
    elif y >= x >= z:
        return z
    elif y >= z >= x:
        return x
    elif z >= x >= y:
        return y
    elif z >= y >= x:
        return x
print(smallest(3,5,9)) # returns 3
print(smallest(5,3,9)) # returns 3
print(smallest(5,9,3)) # returns 3
print(smallest(3,9,5)) # returns 3
print(smallest(9,3,5)) # returns 3
print(smallest(9,5,3)) # returns 3
print(smallest(3,3,5)) # returns 3
print(smallest(5,3,3)) # returns 3
print(smallest(3,5,3)) # returns 3
print(smallest(3,3,3)) # returns 3
