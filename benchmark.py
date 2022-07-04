import ujson as json
import numpy as np
from time import time
from algorithm.backtracking import backtracking
from algorithm.constraints import constraint

# solves sudokus with both algorithms and saves all recorded times to a .json file

constraint_time = []
backtracking_time = []


for difficulty in range(81, 80 , -1): # difficulty of sudoku refers to names in /sudokus
    with open('sudokus/'+ str(difficulty)+ '.json', 'r') as file:
        data = json.load(file)
        keys = data.keys()
        i = 0
        for key in keys: # repeats test for all sudokus in difficulty file
            i = i + 1
            print('difficulty:', difficulty, '| sudoku:', i)
            puzzle = data[key]
            # test backtracking
            sudoku = np.array(puzzle)
            start = time()
            backtracking(sudoku)
            end = time()
            backtracking_time.append(end-start)

            # test constraint
            sudoku = np.array(puzzle)
            start = time()
            constraint(sudoku)
            end = time()
            constraint_time.append(end-start)
    dict = {}
    dict['constraint_time'] = constraint_time
    dict['backtracking_time'] = backtracking_time
    
    # writes test results to .json with difficulty as name
    with open('outputs/'+ str(difficulty)+ '.json', 'w') as file:
        json.dump(dict, file , indent=4)

