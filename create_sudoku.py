import numpy as np
from random import randrange
from algorithm.backtracking import backtracking

def create_field():
    field = np.array([[0]*9]*9)
    sudoku = backtracking(field)
    return sudoku

def create_sudoku(filled):

    if filled > 81:
        raise ("filled cannot be more than 81")
    sudoku = create_field()
    erase = 81 - filled
    erased = []
    while len(erased) != erase:
        x = randrange(9)
        y = randrange(9)
        if [x,y] not in erased:
            erased.append([x,y])
            sudoku[y][x] = 0
    return sudoku
