def minsteps (n):
    memo = [0] * (n + 1)
    for x in range(2,n+1):
        memo[x] = memo[x-1] + 1
        if x % 2 == 0:
            memo[x] = min(memo[x],memo[x//2]+1)
        if x % 3 == 0:
            memo [x] = min(memo[x],memo[x//3]+1)
    return memo[n]
