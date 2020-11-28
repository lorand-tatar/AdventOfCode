file_path = 'day3a_input.txt'

coordinate_set1 = {(0, 0, 0)}
coordinate_set2 = {(0, 0, 0)}
commandses = []

with open(file_path, 'r') as file:
    for line in file:
        commands = [x for x in line.split(',')]
        commandses.append(commands)


def do_stufff(commands, coordinate_set):
    cc = (0, 0, 0)
    for c in commands:
        command = c[0]
        value = int(c[1:])
        for i in range(value):
            if command == "R":
                cc = (cc[0] + 1, cc[1], cc[2] + 1)
            elif command == "L":
                cc = (cc[0] - 1, cc[1], cc[2] + 1)
            elif command == "U":
                cc = (cc[0], cc[1] + 1, cc[2] + 1)
            elif command == "D":
                cc = (cc[0], cc[1] - 1, cc[2] + 1)
            coordinate_set.add(cc)


do_stufff(commandses[0], coordinate_set1)
do_stufff(commandses[1], coordinate_set2)

# distances_to_origo = [abs(x[0]) + abs(x[1]) for x in coordinate_set1 if x in coordinate_set2]
# distances_to_origo.sort()
# print("Closest intersection to origo - which is not origo", distances_to_origo[1])

# Nagyon trash, le sem tud futni rendesen, borzalmas performance!
min_path_lengths_from_origo = 6400000
for x in coordinate_set1:
    for y in coordinate_set2:
        if x[0] == y[0] and x[1] == y[1] and (x[2] + y[2] < min_path_lengths_from_origo) and x[2] + y[2] != 0:
            print("found one: ", x, y)
            min_path_lengths_from_origo = x[2] + y[2]

print("Intersection which has the minimal paths: ", min_path_lengths_from_origo)
