def insert(n,ss):
    def loop(ss,left):
        if ss != []:
            if n <= ss[0]:
                return left + [n] + ss
            else:
                return loop(ss[1:],left + [ss[0]])
        else:
            return left + [n] + ss
    return loop(ss,[])
