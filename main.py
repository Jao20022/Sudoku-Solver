import numpy as np
from timeit import timeit
import algorithm.backtracking as backtracking
import algorithm.constraints as constraints
import algorithm.check as check
import test_sudoku
'''
Applicatie spaghetti
'''

def menu():
  print("Kies een optie")
  print("1. Los een sudoku op")
  print("2. Vul je eigen sudoku in")
  print("3. Check sudoku (werkt alleen voor complete sudokus)")
  print("4. Sluit de applicatie")
  while True:
    try:
      x = int(input(': '))
      if x in range(1,5):
        return x
      else:
        print("vul een getal tussen 1-5 in.")
    except:
      print("vul een getal tussen 1-5 in.")


  

def solve(custom):
  easy = np.array(test_sudoku.easy)
  medium = np.array(test_sudoku.medium)
  hard = np.array(test_sudoku.hard)
  very_hard = np.array( test_sudoku.very_hard)

  print("Kies een optie")
  print("1. Easy")
  print("2. Medium")
  print("3  Hard")
  print("4. Very Hard")
  print("5. Eigen")
  while True:
    try:
      x = input(': ')
      x = int(x)
    except:
      print("vul een getal tussen 1-5 in.")
    if x == 1:
      pick_algorithm(easy)
      break
    if x == 2:
      pick_algorithm(medium)
      break
    if x == 3:
      pick_algorithm(hard)
      break
    if x == 4:
      pick_algorithm(very_hard)
      break
    if x == 5:
      if custom is False:
        custom = create_sudoku()
      pick_algorithm(custom)
      break 
    else:
      print("vul een getal tussen 1-5 in.")
    
def pick_algorithm(sudoku):
  print("Kies een optie")
  print("1. Constraint")
  print("2. Backtracking")

  while True:
    try:
      x = input(': ')
      x = int(x)
    except:
      print("vul een getal tussen 1-2 in.")
    if x in range(1,3):
      if x == 1:
        start = timeit()
        solve = constraints.constraint(sudoku)
        end = timeit()
      if x == 2:
        start = timeit()
        solve = backtracking.backtracking(sudoku)
        end = timeit()
      time = end - start
      if time < 0:
        time = time * -1

      if solve is None:
        print('Sudoku heeft geen oplossing')
      elif check.check_sudoku(solve):
        print(solve)
        print('time: ', round(time, 4), 's', sep='')
      else:
        print('Sudoku heeft geen oplossing')
      break
    else:
      print("vul een getal tussen 1-2 in.")
    

def create_row(i):
  print('Vul een 0 in voor lege cellen')
  while True:
    x = []
    try:
      iput = input('vul de getallen op de '+ str(i) + 'e rij in\n: ')
      row = iput[:9]
      print(row)
      for itt in range(9):
        x.append(int(row[itt]))
      return x
    except:
      print('probeer opnieuw')
    

def create_sudoku():
  sudoku = []
  print(len(sudoku))
  i = 0
  while i < 8:
    i = len(sudoku)
    row = create_row(i+1)
    sudoku.append(row)
  sudoku = np.array(sudoku)
  print(sudoku)
  return sudoku

def check_sudoku(sudoku):
  if sudoku is False:
    print("Vul eerst een sudoku in")
  else:
    result = check.check_sudoku(sudoku)
    if result:
      print('Sudoku klopt')
    else:
      print('Sudoku Klopt niet')

sudoku = False


while True:
  x = menu()
  if x == 1:
    solve(sudoku)
  elif x == 2:
    sudoku = create_sudoku()
  elif x == 3:
    check_sudoku(sudoku)
  elif x == 4:
    break





