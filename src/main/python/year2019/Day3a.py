file_path = 'inputs/day3a_input.txt'

coordinate_set1 = {(0, 0)}
coordinate_set2 = {(0, 0)}
commandses = []

with open(file_path, 'r') as file:
    for line in file:
        commands = [x for x in line.split(',')]
        commandses.append(commands)


def do_stufff(commands, coordinate_set):
    cc = (0, 0)
    for c in commands:
        command = c[0]
        value = int(c[1:])
        for i in range(value):
            if command == "R":
                cc = (cc[0] + 1, cc[1])
            elif command == "L":
                cc = (cc[0] - 1, cc[1])
            elif command == "U":
                cc = (cc[0], cc[1] + 1)
            elif command == "D":
                cc = (cc[0], cc[1] - 1)
            coordinate_set.add(cc)


do_stufff(commandses[0], coordinate_set1)
do_stufff(commandses[1], coordinate_set2)
results = [abs(x[0]) + abs(x[1]) for x in coordinate_set1 if x in coordinate_set2]

results.sort()
print("Hö Hö Hö én vagyok a Télapö", results[1])
