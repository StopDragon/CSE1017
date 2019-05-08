# -*- coding: utf-8 -*-
# sudok6x6
import random
def create_board():
    seed = [1,2,3,4,5,6]
    random.shuffle(seed)
    seed1 = [seed[1], seed[2], seed[3], seed[4], seed[5], seed[0]]
    seed2 = [seed[1], seed[0], seed[3], seed[2]]
    seed3 = [seed[3], seed[2], seed[1], seed[0]]
    seed4 = 
    seed5 = 
    return [seed, seed1, seed2, seed3, seed4 ,seed5]
print(create_board())

def sudok6x6()
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
    print("잘 하셨습니다. 또 들려주세요.")