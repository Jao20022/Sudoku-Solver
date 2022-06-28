import test_sudoku
import numpy as np
import check
from time import time

def backtracking(sudoku: np.array) -> np.array:
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




easy = np.array(test_sudoku.easy)
#print(easy)

x = backtracking(easy)
q = time()
#print(check.check_sudoku(x) )
s = time()
print(s - q)