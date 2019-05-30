# -*- coding: utf-8 -*-
def loop(m,n): #교수님께 질문하기 
    if n > 1:
        if n % 2 == 0:
            return loop(m * 2,n // 2)
        else: # n % 2 != 0
            return m + loop(m * 2,n // 2)
    else: # n == 1
        return m
def rsmult0(m,n):
    if n > 0:
        return loop(m,n)
    else:
        return 0
