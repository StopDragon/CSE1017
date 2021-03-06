# -*- coding: utf-8 -*-
def fastgcd(m,n):
    k = 1
    while not (m == 0 or n == 0):
        if m % 2 == 0 and n % 2 == 0:
            m, n, k = m//2, n//2 ,k*2
        elif m % 2 == 0 and n % 2 == 1:
            m = m//2
        elif m % 2 == 1 and n % 2 == 0:
            n = n//2
        elif m <= n:
            n = (n-m)//2
        else:
            m, n = n, (m-n)//2
    if m == 0:
        return abs(k * n)
    else: # n == 0
        return abs(k * m)
