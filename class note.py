# -*- coding: utf-8 -*-
def square(n):# while 문
    n = abs(n)
    a = 0
    while n > 0:
        n, a = (n - 1), (a + 2 * n - 1)
        return a + n
    return

print(square(0)) # => 0
print(square(1)) # => 1
print(square(-2)) # => 4
print(square(3)) # => 9
print(square(-4)) # => 16
print(square(5)) # => 25
