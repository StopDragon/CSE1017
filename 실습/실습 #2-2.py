# -*- coding: utf-8 -*-
# 둘 중 작은 수 찾기 함수 
def smaller(x,y):
    if x <= y:
        return x
    elif x > y:
        return y
print(smaller(3,5)) # returns 3
print(smaller(5,3)) # returns 3
print(smaller(3,3)) # returns 3
