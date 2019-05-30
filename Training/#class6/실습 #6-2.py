def isidentity(sqmat):
    size = len(sqmat)
    for i in range(size):
        for j in range(size):
            if i == j and sqmat[j][i] != 1 :
                return False
            elif i != j and sqmat[j][i] != 0 :
                return False
    return True
