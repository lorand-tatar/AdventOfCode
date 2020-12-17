import numpy as np
import sys
import copy

file_path = 'inputs/day17_input.txt'

np.set_printoptions(threshold=sys.maxsize)
activity_map = np.zeros((22, 22, 22, 22)).astype(int)
j = 7
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        i = 7
        for char in line:
            if char == '#':
                activity_map[11][11][j][i] = 1
            i += 1
        j += 1


def neighbors_active(activity_map, w, i, j, k):
    active_count = 0
    for x in range(w - 1, w + 2):
        for l in range(i - 1, i + 2):
            for m in range(j - 1, j + 2):
                for n in range(k - 1, k + 2):
                    if i != l or j != m or k != n or x != w:
                        if activity_map[x][l][m][n] == 1:
                            active_count += 1
    return active_count


cycle = 0
new_state = copy.deepcopy(activity_map)
while cycle < 6:
    w = 0
    for timesheet in activity_map:
        i = 0
        for level in timesheet:
            j = 0
            for row in level:
                k = 0
                for box in row:
                    if w != 0 and i != 0 and j != 0 and k != 0 and w != 21 and i != 21 and j != 21 and k != 21:
                        active_neighbors = neighbors_active(activity_map, w, i, j, k)
                        if box == 0 and active_neighbors == 3:
                            new_state[w][i][j][k] = 1
                        elif box == 1 and not (active_neighbors == 2 or active_neighbors == 3):
                            new_state[w][i][j][k] = 0
                    k += 1
                j += 1
            i += 1
        w += 1
    activity_map = copy.deepcopy(new_state)
    cycle += 1
sum_of_boxes = 0
for w in activity_map:
    for i in w:
        for j in i:
            for k in j:
                sum_of_boxes += k

print("Number of active boxes:", sum_of_boxes)
