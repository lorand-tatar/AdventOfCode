import numpy as np

import operator

file_path = 'inputs/day12_input.txt'

original_moon_positions = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        (x, y, z) = line.split(',')
        original_moon_positions.append((int(x), int(y), int(z)))

for dim in range(3):
    x = []
    orig_x = []
    for i in range(4):
        orig_x.append(original_moon_positions[i][dim])
        x.append(original_moon_positions[i][dim])
    moon_velocities = [0, 0, 0, 0]
    time_tick = 0
    while (time_tick == 0) or ((x != orig_x) or (moon_velocities != [0, 0, 0, 0])):
        # Adjust velocities
        for moon in range(4):
            for other_moon in range(4):
                if moon != other_moon:
                    other_x = x[other_moon]
                    vel_change_x = np.sign(other_x - x[moon])
                    moon_velocities[moon] += vel_change_x
        # Adjust positions
        for moon in range(4):
            x[moon] += moon_velocities[moon]
        time_tick += 1

    print("Ticks for 1 dim coords only:", time_tick)
    # Then I calculated the lcp of the three