from codecs import latin_1_decode
import numpy as np
from backtracking import backtracking
import check
import test_sudoku
import time

def generate_possible(sudoku):
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

def check_solved(sudoku):
    solved = True
    for i in range(9):
        if 0 in sudoku[i]:
            solved = False
    return solved

def one_cell(sudoku, possibles):
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

def count(sudoku, number):
    count = 0
    for row in range(9):
        count = count + np.count_nonzero(sudoku[row] == number)
    return count

def fill_in(sudoku, number):
    for y in range(9):
        for x in range(9):
            if check.check_cell(sudoku, x, y, number):
                sudoku[y][x] = number
                return sudoku

def one_left(sudoku):
    one_left = False
    l1 = count(sudoku, 1)
    if l1 == 1:
        sudoku = fill_in(sudoku, l1)
        one_left = True
    l2 = count(sudoku, 2)
    if l2 == 1:
        sudoku = fill_in(sudoku, l2)
        one_left = True
    l3 = count(sudoku, 3)
    if l3 == 1:
        sudoku = fill_in(sudoku, l3)
        one_left = True
    l4 = count(sudoku, 4)
    if l4 == 1:
        sudoku = fill_in(sudoku, l4)
        one_left = True
    l5 = count(sudoku, 5)
    if l5 == 1:
        sudoku = fill_in(sudoku, l5)
        one_left = True
    l6 = count(sudoku, 6)
    if l6 == 1:
        sudoku = fill_in(sudoku, l6)
        one_left = True
    l7 = count(sudoku, 7)
    if l7 == 1:
        sudoku = fill_in(sudoku, l7)
        one_left = True
    l8 = count(sudoku, 8)
    if l8 == 1:
        sudoku = fill_in(sudoku, l8)
        one_left = True
    l9 = count(sudoku, 9)
    if l9 == 1:
        sudoku = fill_in(sudoku, l9)
        one_left = True
    if one_left:
        return sudoku
    else:
        return False
    


def constraint(sudoku):
    while True:
        if check_solved(sudoku):
            break
        action = False
        possibles = generate_possible(sudoku)
        temp = one_cell(sudoku, possibles)
        if temp is not False:
            sudoku = temp
            action = True
        temp = one_left(sudoku)
        if temp is not False:
            sudoku = temp
            action = True
        if not action:
            return backtracking(sudoku)
    return sudoku
