import numpy as np

row = [0]*9
grid = [row]*9

sudoku = np.array(grid)



def print_sudoku(grid):
  for row in grid:
    print('',row[0],'|',row[1],'|',row[2],'|',row[3],'|',row[4],'|',row[5],'|',row[6],'|',row[7],'|',row[8])
    print('-----------------------------------')


print_sudoku(sudoku)