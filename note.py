def count_upto(n):
    ns = []
    while n > 0:
        n = n - 1
        ns = [n] + ns
    return ns
print(count_upto(5)) # [0, 1, 2, 3, 4, 5]
