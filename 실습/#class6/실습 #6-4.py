def transpose(mat):
    no_of_columns = len(mat[0])
    transposed = []
    for i in range(no_of_columns):
        list = []
        for j in range(no_of_columns):
            list += [mat[j][i]]
        transposed += [list]
    return transposed
