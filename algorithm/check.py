import numpy as np

def get_sector(coord: int) -> int | int:
  '''
  returns the right values for the list slice
  used by check square
  
  coord: x or y coordinate.

return: int, int
  
    ''' 
  if coord in range(0,3):
    x1, x2 = 0, 3
  elif coord in range(3,6):
    x1, x2 = 3, 6
  elif coord in range(6,9):
     x1, x2 = 6, 9
  return x1 , x2

def check_row(sudoku: np.array, y: int , value: int) -> bool:
  '''
  checks if a value can be placed in a row. 
  
  sudoku: sudoku puzzle to be checked
  y: the y coordinate of the row to be checked against.
  value: the value to be checked

  returns: boolean
    '''
  if value in sudoku[y]:
    return False
  else:
    return True


def check_collumn(sudoku: np.array, x: int , value: int) -> bool:
  '''
  checks if a value can be placed in a collumn. 
  
  sudoku: sudoku puzzle to be checked
  x: the x coordinate of the collumn to be checked against.
  value: the value to be checked

  returns: boolean
    '''


  for y in range(9):
    if value == sudoku[y][x]:
      return False
  return True

def check_square(sudoku: np.array , x: int, y: int , value: int) -> bool:
  '''
  checks if a value can be placed in a 3x3 square. 
  
  sudoku: sudoku puzzle to be checked
  x: the x coordinate of the collumn to be checked against.
  value: the value to be checked

  returns: boolean
    '''
    
  y1, y2 = get_sector(y)
  x1, x2 = get_sector(x)
  if value in sudoku[y1:y2, x1:x2]:
    return False
  else:
    return True


def check_cell(sudoku: np.array, x: int, y: int, value: int ) -> bool:
  '''
  checks if a value can be placed in a cell. 
  
  sudoku: sudoku puzzle to be checked
  x: the x coordinate of the cell to be checked.
  y: the y coordinate of the cell to be checked
  value: the value to be checked

  returns: boolean
    '''  
  row = check_row(sudoku, y , value)
  square = check_square(sudoku , x, y , value)
  collumn = check_collumn(sudoku, x , value)
  if row and square and collumn: 
    return True
  else:
    return False

def check_sudoku(sudoku: np.array) -> bool:
  '''
  checks every cell of a given sudoku
  sudoku: sudoku to be checked

  returns: boolean True/False if sudoku is valid
  '''
  for y in range(9):
      for x in range(9):
          value, sudoku[y][x] = sudoku[y][x], 0
          cell = check_cell(sudoku, x, y, value)
          sudoku[y][x] = value
          if not cell:
              return False
  return True