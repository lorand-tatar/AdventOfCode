file_path = 'inputs/day12_input.txt'

moon_positions = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        (x, y, z) = line.split(',')
        moon_positions.append((int(x), int(y), int(z)))

moon_velocities = [0, 0, 0, 0]

print(moon_positions)
