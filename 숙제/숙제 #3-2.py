# -*- coding: utf-8 -*-
# 순열 permutation
# assume: n > 0, k > 0, n >= k
# 양수 인수만 제대로 처리하면 된다.
# 즉, 인수가 양수인지는 함수 호출하기 전에 이미 확인했다고 가정한다.
# 그리고  n < k 인 경우에는 0을 내주도록 해야 한다.
def permutation(n,k): #재귀
    if k > 0:
        return n * permutation(n-1,k-1)
    else:
        return 1

def permutation(n,k):# 꼬리 재귀
    def loop(n,k,a):
        if k > 0:
            return loop(n-1,k-1,n * a)
        else:
            return a
    return loop(n,k,1)


def permutation(n,k):# while
    a = 1
    while k > 0:
        n,k,a = n-1, k-1, n * a
    return a
print(permutation(1,1)) # => 1
print(permutation(2,1)) # => 2
print(permutation(2,2)) # => 2
print(permutation(3,1)) # => 3
print(permutation(3,2)) # => 6
print(permutation(3,3)) # => 6
print(permutation(4,1)) # => 4
print(permutation(4,2)) # => 12
print(permutation(4,3)) # => 24
print(permutation(4,4)) # => 24
