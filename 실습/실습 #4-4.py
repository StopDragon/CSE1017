def insertionsort(ns):
    def insert(n,ss):
        if ss != []:
            if n <= ss[0]:
                return [n] + ss
            else:
                return [ss[0]] + insert(n,ss[1:])
        else:
            return [n]
    def loop(ns,ss):
        if ns != []:
            return loop(ns[1:],insert(ns[0],ss))
        else:
            return ss
    return loop(ns,[])
