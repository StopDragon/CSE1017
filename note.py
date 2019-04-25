def equiv_class(ns):
    ns.sort()
    if ns == [] :
        return []
    else :
        top = ns[0]
        nss = [[top]]
        for n in ns[1:] :
            top = nss[-1][0]
            if n == top :
                tops = nss[-1]
                nss = nss[:-1]
                nss.append(tops+[n])
            else :
                nss.append([n])
        return nss

print(equiv_class([])) # []
print(equiv_class([3])) # [[3]]
print(equiv_class([4,3,2,4,4])) # [[2],[3],[4,4,4]]
print(equiv_class([2,4,4,2,2,3])) # [[2,2,2],[3],[4,4]]
