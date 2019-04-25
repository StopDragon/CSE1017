# -*- codig: utf-8 -*-
# no.1
def complement9(n): # 자연수라고 가정
      s = str(n)
      ans = ""
      for c in s:
            d = 9 - int(c)
            ans = ans + str(d)
      return int(ans)

# no.2
def search(key,ns):
    index = 0
    ans = []
    for n in ns:
        if key == n:
            ans = ans + [index]
            index += 1
        else:
            index += 1
    if index == len(ns):
        return ans
    else:
        return ans

# no.3
def count_upto(n):
    def loop(n,ns):
        if n < 0:
            return ns
        else:
            return loop(n-1, [n] + ns)
    return loop(n,[])

# no.4
def count_upto(n):
    ns = []
    while n >= 0:
        count_upto(n-1)
        ns = ns + [n]
    return ns

# no.5
def zippo(xs,ys):
    def loop(xs,ys,zs):
        if xs == [] or ys == []:
            return xs + ys
        else:
            return [xs[0]+ys[0]] + zippo(xs[1:],ys[1:])
    return loop(xs,ys,[])

#
