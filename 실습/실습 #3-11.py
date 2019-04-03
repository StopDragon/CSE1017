# -*- coding: utf-8 -*-
def rsmult(m,n):
    a = 0
    while n > 1:
        if n % 2 == 0:
            m,n = (m * 2, n // 2)
        else :
            m,n,a= (m * 2, n // 2, a + m)
    return a + m
