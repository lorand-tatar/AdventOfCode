import functools
import numpy as np
import sys

file_path = 'inputs/day10_input.txt'

LASER_X = 31
LASER_Y = 20


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def killed_first(coord1, coord2):
    (x1, y1) = coord1
    (x2, y2) = coord2
    quadrant1 = 0
    quadrant2 = 0
    if x1 - LASER_X >= 0 and y1 - LASER_Y < 0:
        quadrant1 = 1
    elif x1 - LASER_X > 0 and y1 - LASER_Y >= 0:
        quadrant1 = 2
    elif x1 - LASER_X <= 0 and y1 - LASER_Y > 0:
        quadrant1 = 3
    elif x1 - LASER_X < 0 and y1 - LASER_Y <= 0:
        quadrant1 = 4
    if x2 - LASER_X >= 0 and y2 - LASER_Y < 0:
        quadrant2 = 1
    elif x2 - LASER_X > 0 and y2 - LASER_Y >= 0:
        quadrant2 = 2
    elif x2 - LASER_X <= 0 and y2 - LASER_Y > 0:
        quadrant2 = 3
    elif x2 - LASER_X < 0 and y2 - LASER_Y <= 0:
        quadrant2 = 4

    if quadrant1 < quadrant2:
        return -1
    elif quadrant2 < quadrant1:
        return 1

    # The two points are in the same quadrant
    if y1 - LASER_Y == 0:
        return -1
    if y2 - LASER_Y == 0:
        return 1
    if x1 - LASER_X == 0:
        return -1
    if x2 - LASER_X == 0:
        return 1

    if quadrant1 == 1 or quadrant1 == 3:
        return -1 if (abs(x1 - LASER_X) / abs(y1 - LASER_Y)) < (abs(x2 - LASER_X) / abs(y2 - LASER_Y)) else 1
    else:
        return 1 if (abs(x1 - LASER_X) / abs(y1 - LASER_Y)) < (abs(x2 - LASER_X) / abs(y2 - LASER_Y)) else -1


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

visible_asteroids = []
for other_asteroid in asteroid_catalog:
    (x_other, y_other) = other_asteroid
    if (LASER_X != x_other) or (LASER_Y != y_other):
        x_distance = x_other - LASER_X
        y_distance = y_other - LASER_Y
        gcd_of_coord = abs(gcd(x_distance, y_distance))
        reduced_x = int(x_distance / gcd_of_coord)
        reduced_y = int(y_distance / gcd_of_coord)
        rolling_x = reduced_x
        rolling_y = reduced_y
        visible = True
        while rolling_x != x_distance or rolling_y != y_distance:
            if asteroid_map[LASER_X + rolling_x][LASER_Y + rolling_y] == 1:
                visible = False
                break
            rolling_x += reduced_x
            rolling_y += reduced_y
        if visible:
            visible_asteroids.append(other_asteroid)

visible_asteroids = sorted(visible_asteroids, key=functools.cmp_to_key(killed_first))
print("The 200th killed:", visible_asteroids[199])
