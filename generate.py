import numpy as np
import algorithm.check as check
from time import time
from random import randrange


time_begin = time()

def tries(): # Creates a random order for numbers 1-9
  list = []
  while True:
    i = randrange(1,10)
    if i not in list:
      list.append(i)
    if len(list) == 9:
      return list

def generate(sudoku: np.array,) -> np.array:
  '''
  reused code from backtracking, but now tries number in random order to create sudokus

  returns: np.array sudoku
  '''
  for y in range(9):
    for x in range(9):
      if sudoku[y][x] == 0:
        trie = tries()
        for i in trie:
          if check.check_cell(sudoku, x, y, i):
            sudoku[y][x] = i
            solve = generate(sudoku)
            if solve is not None:
              return solve
            sudoku[y][x] = 0
        return
  return sudoku

