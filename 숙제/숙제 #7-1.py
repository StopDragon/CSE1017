# -*- coding: utf-8 -*-
import random

# create_board
def create_board():
    seed = [1,2,3,4,5,6]
    random.shuffle(seed)
    seed1 = [seed[1], seed[2], seed[3], seed[4], seed[5], seed[0]]
    seed2 = [seed[2], seed[3], seed[4], seed[5], seed[0], seed[1]]
    seed3 = [seed[3], seed[4], seed[5], seed[0], seed[1], seed[2]]
    seed4 = [seed[4], seed[5], seed[0], seed[1], seed[2], seed[3]]
    seed5 = [seed[5], seed[0], seed[1], seed[2], seed[3], seed[4]]
    return [seed, seed1, seed2, seed3, seed4 ,seed5]

# shuffle
def shuffle_ribbons(board):
    top_half = board[0:3]
    random.shuffle(top_half)
    bottom_half = board[3:7]
    random.shuffle(bottom_half)
    return top_half + bottom_half

# transpose
import random
def transpose(board):
    transposed = []
    for _ in range(len(board)):
        transposed.append([])
    for row in board:
        for x in range(len(row)):
            transposed[x] += [row[x]]
    return transposed

# solution
def create_solution_board():
    board = create_board()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

# get_level
def get_level():
    print('[sudok6x6] \n만든이: ICT 융합학부 정지용(2019027747)\n')
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if level == '상':
        return 14
    elif level == '중':
        return 10
    elif level == '하':
        return 6
    # level 이 '하' 이면  return  6
    # level 이 '중' 이면  return  10
    # level 이 '상' 이면  return  14

# make_holes
def make_holes(board,no_of_holes):
    holeset = set()
    while no_of_holes > 0:
        i = random.randint(0,5)
        j = random.randint(0,5)
        if board[i][j] == 0:
            continue
        else:
            board[i][j] = 0
            holeset.add((i,j))
            no_of_holes -= 1
    return (board, holeset)

# copy_board
def copy_board(board):
    board_clone = []
    for row in board :
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone

# show_board
def show_board(board):
    print()
    print('S','|','1','2','3','4','5','6')
    print('-','+','-','-','-','-','-','-')
    i = 1
    for row in board:
        for a in range(len(row)):
            if row[a] == 0:
                row[a] = '.'
        print(i, '|', row[0],row[1],row[2],row[3],row[4],row[5])
        i += 1
    print()

# get_integer
def get_integer(message,i,j):
    number = input(message)
    while not (number.isdigit() and (i <= int(number) <= j)):
        number = input(message)
    return int(number)

# sudok6x6
def sudok6x6():
    solution = create_solution_board()
    no_of_holes = get_level()
    puzzle = copy_board(solution)
    (puzzle,holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle)
    while no_of_holes > 0:
        i = get_integer("가로줄번호(1~6): ",1,6) - 1
        j = get_integer("세로줄번호(1~6): ",1,6) - 1
        if (i,j) not in holeset:
            print("빈칸이 아닙니다.")
            continue
        n = get_integer("숫자(1~6): ",1,6)
        sol = solution[i][j]
        if n == sol:
            puzzle[i][j] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes -= 1
        else:
            print(n,"가 아닙니다. 다시 해보세요.")
    return "잘 하셨습니다. 또 들려주세요."

print(sudok6x6())