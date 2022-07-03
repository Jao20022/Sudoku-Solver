from create_sudoku import create_sudoku
from algorithm.backtracking import backtracking
from algorithm.constraints import constraint
import numpy as np
from time import time
import json



for difficulty in range(17,18):
    dict = {}
    sudokus = []
    tries = 0
    while len(dict) < 10000:
        tries = tries + 1
        sudoku = create_sudoku(difficulty)
        dict[len(dict)+1] = sudoku.tolist()
        sudokus.append(sudoku.tolist())
        print('difficulty:', (difficulty), '| tries:', tries, '| sudokus: ', len(dict))

    with open('sudokus/'+ str(difficulty) +'.json', 'w') as file:
        print('writing to '+ str(difficulty)+ '.json...')
        json.dump(dict, file, indent=4)


