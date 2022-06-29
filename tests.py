import pytest
import numpy as np
import algorithm.check as check
from algorithm.backtracking import backtracking
from algorithm.constraints import constraint
import test_sudoku

#Tests all functions
#type "pytest tests.py" in terminal to test.


def test_get_sector():
    assert check.get_sector(0) == (0,3)
    assert check.get_sector(1) == (0,3)
    assert check.get_sector(2) == (0,3)
    assert check.get_sector(3) == (3,6)
    assert check.get_sector(4) == (3,6)
    assert check.get_sector(5) == (3,6)
    assert check.get_sector(6) == (6,9) 
    assert check.get_sector(7) == (6,9)
    assert check.get_sector(8) == (6,9)

def test_check_row():
    array = np.array([[0]*9]*9)
    assert check.check_row(array, 0, 0) == False
    assert check.check_row(array, 0, 1) == True
    
def test_check_collumn():
    array = np.array([[0]*9]*9)
    assert check.check_collumn(array, 0, 0) == False
    assert check.check_collumn(array, 0, 1) == True
def test_check_square():
    array = np.array([[0]*9]*9)
    assert check.check_square(array, 0, 0, 0) == False
    assert check.check_square(array, 0, 0, 1) == True
def test_check_cell():
    false = np.array([[0]*9]*9)
    assert check.check_cell(false, 0, 0, 0) == False
    assert check.check_cell(false, 0, 0, 1) == True
def test_check_sudoku():
    false = np.array([[0]*9]*9)
    true = np.array([[2, 3, 7, 4, 6, 1, 8, 9, 5],
           [1, 5, 8, 2, 3, 9, 4, 6, 7],
           [4, 6, 9, 5, 7, 8, 3, 2, 1],
           [3, 2, 1, 6, 8, 5, 9, 7, 4],
           [8, 4, 6, 1, 9, 7, 2, 5, 3],
           [7, 9, 5, 3, 2, 4, 1, 8, 6],
           [5, 7, 4, 9, 1, 2, 6, 3, 8],
           [9, 8, 3, 7, 4, 6, 5, 1, 2],
           [6, 1, 2, 8, 5, 3, 7, 4, 9]])
    assert check.check_sudoku(false) == False
    assert check.check_sudoku(true) == True

def test_backtracking():
    easy = np.array(test_sudoku.easy)
    medium = np.array(test_sudoku.medium)
    hard = np.array(test_sudoku.hard)
    very_hard = np.array(test_sudoku.very_hard)
    assert check.check_sudoku(backtracking(easy)) == True
    assert check.check_sudoku(backtracking(medium)) == True
    assert check.check_sudoku(backtracking(hard)) == True
    assert check.check_sudoku(backtracking(very_hard)) == True

def test_constraints():
    easy = np.array(test_sudoku.easy)
    medium = np.array(test_sudoku.medium)
    hard = np.array(test_sudoku.hard)
    very_hard = np.array(test_sudoku.very_hard)
    assert check.check_sudoku(constraint(easy)) == True
    assert check.check_sudoku(constraint(medium)) == True
    assert check.check_sudoku(constraint(hard)) == True
    assert check.check_sudoku(constraint(very_hard)) == True
    

