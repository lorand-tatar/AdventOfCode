import numpy as np
import sys

file_path = 'inputs/day10_input.txt'

asteroid_map = np.empty((40, 40))
line = None
with open(file_path, 'r') as file:
    line = file.readline()
    row = 0
    while line != "":
        char_pointer = 0
        line = line.rstrip()
        for char in line:
            element = 1 if char == '#' else 0
            asteroid_map[row][char_pointer] = element
            char_pointer += 1
        line = file.readline()
        row += 1

asteroid_map = asteroid_map.astype(int)
np.set_printoptions(threshold=sys.maxsize)
# print(asteroid_map)

#
