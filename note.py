def count_upto(n):
    ns = []
    while n >= 0:
        ns = [n] + ns
        n = n - 1
    return ns
print(count_upto(5)) # [0, 1, 2, 3, 4, 5]
