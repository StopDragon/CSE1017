def issudoku(mat):
    size = len(mat)
    list = []
    for i in range(size):
        for j in range(size):
            list = list + [mat[i][j]]
    for x in range(1,size**2+1):
        if x not in list:
            return False
    return True
