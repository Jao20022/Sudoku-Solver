import numpy as np
import algorithm.check as check
from random import randrange


def backtracking(sudoku: np.array,) -> np.array:
  '''
  itterates through every cell of a sudoku
  until a solution is found or the end is reached

  sudoku: sudoku to be solved

  returns: solved sudoku or none in case no possible solution
  '''
  for y in range(9):
    for x in range(9):
      if sudoku[y][x] == 0:
        for i in range(1,10):
          if check.check_cell(sudoku, x, y, i):
            sudoku[y][x] = i
            solve = backtracking(sudoku)
            if solve is not None:
              return solve
            sudoku[y][x] = 0
        return
  return sudoku

