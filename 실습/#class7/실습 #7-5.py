# -*- coding: utf-8 -*-
def show_board(board):
    print()
    print('S','|','1','2','3','4')
    print('-','+','-','-','-','-')
    i = 1
    for row in board:
        for a in range(len(row)):
            if row[a] == 0:
                row[a] = '.'
        print(i, '|', row[0],row[1],row[2],row[3])
        i += 1
    print()

show_board([[0,3,0,0],[2,4,0,0],[3,1,2,0],[0,2,1,0]])