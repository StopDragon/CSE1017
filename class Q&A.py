# -*- coding: utf-8 -*-
#질문 n,a를 묶어서 계산할 때랑 묶어서 계산하지 않을 때 값이 다른 이유

def square(n):# while 문
    n = abs(n)
    a = 0
    while n > 0:
        n, a = (n - 1), (a + 2 * n - 1)
    return a + n

def square(n):# while 문
    n,a = abs(n), 0
    while n > 0:
        n, a = (n - 1), (a + 2 * n - 1)
    return a + n
