# -*- coding: utf-8 -*-
def gcd(m,n):
    if n != 0:
        return gcd(n,m%n)
    else:
        return abs(m)

print(gcd(-48,18))
