from create_sudoku import create_sudoku
import ujson as json

# Creates sudoku's between specified difficulty ranges and writes it to a .json file
# Difficulty is defined by the number of known cells
# ex. 17 is hardest 80 is easiest


for difficulty in range(17,81):
    dict = {}
    sudokus = []
    tries = 0
    while len(dict) < 10000: # creates 10000 sudokus per difficulty
        tries = tries + 1
        sudoku = create_sudoku(difficulty) 
        dict[len(dict)+1] = sudoku.tolist()
        sudokus.append(sudoku.tolist())
        print('difficulty:', (difficulty), '| tries:', tries, '| sudokus: ', len(dict))

    with open('sudokus/'+ str(difficulty) +'.json', 'w') as file:
        print('writing to '+ str(difficulty)+ '.json...')
        json.dump(dict, file, indent=4)


