import numpy as np
import algorithm.check as check
import algorithm.backtracking as backtracking


def generate_possible(sudoku: np.array) -> list:
    '''
    Creates a list with every possible input for every cell

    sudoku: np.array for which list is generated

    returns: 3D list with every possible input
    '''
    collumn = []
    for y in range(9):
        row = []
        for x in range(9):
            cell = []
            for i in range(1,10):
                if check.check_cell(sudoku, x, y, i) and sudoku[y][x] == 0:
                    cell.append(i)
            row.append(cell)
        collumn.append(row)
    return collumn

def check_solved(sudoku: np.array) -> bool:
    '''
    checks if a given sudoku is finished

    sudoku: np.array to be checked

    returns bool if sudoku is done
    '''
    solved = True
    for i in range(9):
        if 0 in sudoku[i]:
            solved = False
    return solved

def one_cell(sudoku, possibles) -> np.array:
    '''
    sudoku: np.array sudoku to be solved
    possibles: list with poosibles created by generate_possibles

    returns: np array sudoku to be solved
    or boolean if nothing got changed
    '''
    one_left = False
    for y in range(9):
        for x in range(9):
            if len(possibles[y][x]) == 1:
                sudoku[y][x] = possibles[y][x][0]
                one_left = True
    if one_left:
        return sudoku
    else:
        return False
  

def constraint(sudoku: np.array) -> np.array:
    '''
    tries to solve the sudoku using constraints
    if it can't find a move it will use backtracking to solve the rest

    sudoku: np.array sudoku to be solved

    returns: np.array solved sudoku or None if there isn't a solution
    '''
    while True:
        if check_solved(sudoku):
            break
        action = False
        possibles = generate_possible(sudoku)
        temp = one_cell(sudoku, possibles)
        if temp is not False:
            sudoku = temp
            action = True
        if not action:
            return backtracking.backtracking(sudoku)
    return sudoku
