import matplotlib.pyplot as plt
import numpy as np
import ujson as json

start = 29
finish = 81
plt_diff = []
back_min = []
cons_min = []
back_max = []
cons_max = []
back_average = []
cons_average = []

# get all data from .json files and calculate average min and max time
for difficulty in range(start, finish+1):
  with open('outputs/'+ str(difficulty) + '.json', 'r') as file:
    data: dict = json.load(file)
    backtracking_time: list = data['backtracking_time']
    constraint_time: list = data['constraint_time']
    plt_diff.append(difficulty)
    back_max.append(max(backtracking_time))
    cons_max.append(max(constraint_time))
    back_min.append(min(backtracking_time))
    cons_min.append(min(constraint_time))
    back_average.append(np.average(backtracking_time))
    cons_average.append(np.average(constraint_time))
    print('difficulty:', difficulty)
    
# convert lists to np arrays
plt_diff = np.array(plt_diff)
back_min = np.array(back_min)
cons_min = np.array(cons_min)
back_max = np.array(back_max)
cons_max = np.array(cons_max)
back_average = np.array(back_average)
cons_average = np.array(cons_average)

# create plots for min, max and average

# plot average
plt.xlabel('difficulty')
plt.ylabel("Time (seconds)")
plt.title("Average")
plt.plot(plt_diff, cons_average, color='r', label='constraint')
plt.plot(plt_diff, back_average, color='g', label='backtracking')


plt.legend()
plt.show()

# plot min
plt.xlabel("Difficulty")
plt.ylabel("Time (seconds)")
plt.title("Min")
plt.plot(plt_diff, cons_min, color='r', label='constraint')
plt.plot(plt_diff, back_min, color='g', label='backtracking')


plt.legend()
plt.show()

#plot max
plt.xlabel("Difficulty")
plt.ylabel("Time (seconds)")
plt.title("Max")
plt.plot(plt_diff, cons_max, color='r', label='constraint')
plt.plot(plt_diff, back_max, color='g', label='backtracking')





plt.legend()
plt.show()