# -*- coding: utf-8 -*-
def transpose(board):
    transposed = []  
    for _ in range(len(board)):
        transposed.append([])
    for row in board:
        transposed[0].append(row[0])
        transposed[1].append(row[1])
        transposed[2].append(row[2])
        transposed[3].append(row[3])
    return transposed
board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(transpose(board))