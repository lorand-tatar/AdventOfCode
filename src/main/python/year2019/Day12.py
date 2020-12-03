import numpy as np

import operator

file_path = 'inputs/day12_input.txt'

moon_positions = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        (x, y, z) = line.split(',')
        moon_positions.append((int(x), int(y), int(z)))

moon_velocities = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

for time_tick in range(1000):
    # Adjust velocities
    for moon in range(4):
        (moon_x, moon_y, moon_z) = moon_positions[moon]
        (vel_x, vel_y, vel_z) = moon_velocities[moon]
        for other_moon in range(4):
            if moon != other_moon:
                (other_x, other_y, other_z) = moon_positions[other_moon]
                # print("######## Gravity between", moon, other_moon)
                # print("Velocities before:", moon_velocities)
                (vel_change_x, vel_change_y, vel_change_z) = (np.sign(other_x - moon_x), np.sign(other_y - moon_y), np.sign(other_z - moon_z))
                vel_x += vel_change_x
                vel_y += vel_change_y
                vel_z += vel_change_z
                moon_velocities[moon] = (vel_x, vel_y, vel_z)
                # print("Velocities after:", moon_velocities)

    # Adjust positions
    for moon in range(4):
        (moon_x, moon_y, moon_z) = moon_positions[moon]
        (vel_x, vel_y, vel_z) = moon_velocities[moon]
        moon_x += vel_x
        moon_y += vel_y
        moon_z += vel_z
        moon_positions[moon] = (moon_x, moon_y, moon_z)
    # print("New positions:", moon_positions)

# Calculate energy
total_energy = 0
for moon in range(4):
    potential_energy = abs(moon_positions[moon][0]) + abs(moon_positions[moon][1]) + abs(moon_positions[moon][2])
    kinetic_energy = abs(moon_velocities[moon][0]) + abs(moon_velocities[moon][1]) + abs(moon_velocities[moon][2])
    total_energy += potential_energy * kinetic_energy

print("Total energy after 1000 ticks:", total_energy)
