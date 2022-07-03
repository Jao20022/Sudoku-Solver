import ujson as json
import numpy as np
from time import time
from algorithm.backtracking import backtracking
from algorithm.constraints import constraint


constraint_time = []
backtracking_time = []


for difficulty in range(17,81):
    with open('sudokus/'+ str(difficulty)+ '.json', 'r') as file:
        data = json.load(file)
        keys = data.keys()
        i = 0
        for key in keys:
            i = i + 1
            print('difficulty:', difficulty, '| sudoku:', i)
            puzzle = data[key]
            sudoku = np.array(puzzle)
            start = time()
            backtracking(sudoku)
            end = time()
            backtracking_time.append(end-start)

            sudoku = np.array(puzzle)
            start = time()
            constraint(sudoku)
            end = time()
            constraint_time.append(end-start)
    dict = {}
    dict['constraint_time'] = constraint_time
    dict['backtracking_time'] = backtracking_time

    with open('outputs/'+ str(difficulty)+ '.json', 'r') as file1:
        json.dump(dict, file1, indent=4)

