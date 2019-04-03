# -*- coding: utf-8 -*-
def fastmult(m,n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            m = 2*m
            n = n//2
        else:
            n = n-1
            ans = ans + m
    return ans
