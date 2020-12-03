import numpy as np
import sys

file_path = 'inputs/day3_input.txt'

START_X = 0
START_Y = 0
SLOPE_HEIGHT = 323
PATTERN_WIDTH = 31


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Need to repeat the map 33 times to the right!
tree_map_pattern = np.empty((40, 400))
line = None
with open(file_path, 'r') as file:
    line = file.readline()
    row = 0
    while line != "":
        char_pointer = 0
        line = line.rstrip()
        for char in line:
            if char == '#':
                tree_map_pattern[char_pointer][row] = 1
            else:
                tree_map_pattern[char_pointer][row] = 0
            char_pointer += 1
        line = file.readline()
        row += 1

tree_map_pattern = tree_map_pattern.astype(int)
np.set_printoptions(threshold=sys.maxsize)

slopes_to_try = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

product_of_all_hit_trees = 1
for slope in slopes_to_try:
    (step_x, step_y) = slope
    rolling_x = START_X
    rolling_y = START_Y
    no_of_hit_trees = 0
    while rolling_y < SLOPE_HEIGHT:
        if tree_map_pattern[START_X + rolling_x][START_Y + rolling_y] == 1:
            no_of_hit_trees += 1
        rolling_x += step_x
        if rolling_x > PATTERN_WIDTH - 1:
            rolling_x = rolling_x - PATTERN_WIDTH
        rolling_y += step_y
    print(no_of_hit_trees)
    product_of_all_hit_trees = product_of_all_hit_trees * no_of_hit_trees

print("The product of all hit trees on the slopes:", product_of_all_hit_trees)
