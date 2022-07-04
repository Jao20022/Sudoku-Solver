import numpy as np
from random import randrange
from generate import generate

def create_field(): # creates a completed sudoku
    field = np.array([[0]*9]*9)
    sudoku = generate(field)
    return sudoku

def create_sudoku(filled):
    '''
    Creates a sudoku by emptying all but a few cells

    filled: int number filled cells

    returns: np.array sudoku
    '''
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
