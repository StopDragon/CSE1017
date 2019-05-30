# -*- coding: utf-8 -*-
import random
def create_board():
    seed = [1,2,3,4]
    random.shuffle(seed)
    seed1 = [seed[2], seed[3], seed[0], seed[1]]
    seed2 = [seed[1], seed[0], seed[3], seed[2]]
    seed3 = [seed[3], seed[2], seed[1], seed[0]]
    return [seed, seed1, seed2, seed3]

print(create_board())
