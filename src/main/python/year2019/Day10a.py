import numpy as np
import sys

file_path = 'inputs/day10_input.txt'


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


asteroid_map = np.empty((40, 40))
asteroid_catalog = []
line = None
with open(file_path, 'r') as file:
    line = file.readline()
    row = 0
    while line != "":
        char_pointer = 0
        line = line.rstrip()
        for char in line:
            if char == '#':
                element = 1
                asteroid_catalog.append((char_pointer, row))
            else:
                element = 0
            asteroid_map[char_pointer][row] = element
            char_pointer += 1
        line = file.readline()
        row += 1

asteroid_map = asteroid_map.astype(int)
np.set_printoptions(threshold=sys.maxsize)

max_visible = 0
for one_asteroid in asteroid_catalog:
    asteroids_visible = 0
    (x_focus, y_focus) = one_asteroid
    for other_asteroid in asteroid_catalog:
        (x_other, y_other) = other_asteroid
        if (x_focus != x_other) or (y_focus != y_other):
            x_distance = x_other - x_focus
            y_distance = y_other - y_focus
            gcd_of_coord = abs(gcd(x_distance, y_distance))
            reduced_x = int(x_distance / gcd_of_coord)
            reduced_y = int(y_distance / gcd_of_coord)
            rolling_x = reduced_x
            rolling_y = reduced_y
            visible = True
            while rolling_x != x_distance or rolling_y != y_distance:
                if asteroid_map[x_focus + rolling_x][y_focus + rolling_y] == 1:
                    visible = False
                    break
                rolling_x += reduced_x
                rolling_y += reduced_y
            if visible:
                asteroids_visible += 1
    if asteroids_visible > max_visible:
        max_visible = asteroids_visible

print("Max visible asteroids:", max_visible)