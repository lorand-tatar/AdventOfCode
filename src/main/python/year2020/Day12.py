import re

file_path = 'inputs/day12_input.txt'

moves = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        matcher = re.search("^([RLFESWN])(\\d+)$", line)
        command = matcher.group(1)
        amount = int(matcher.group(2))
        if command == "R":
            moves.append((0, 0, 0, -amount))
        elif command == "L":
            moves.append((0, 0, 0, amount))
        elif command == "F":
            moves.append((0, 0, amount, 0))
        elif command == "E":
            moves.append((amount, 0, 0, 0))
        elif command == "S":
            moves.append((0, amount, 0, 0))
        elif command == "W":
            moves.append((-amount, 0, 0, 0))
        elif command == "N":
            moves.append((0, -amount, 0, 0))
        else:
            print("Ooops, wrong command read", command)
            exit(-1)

position = (0, 0)
heading = (1, 0)
for move in moves:
    (x, y, forward, angle) = move
    if angle == 90 or angle == -270:
        new_heading = (heading[1], -heading[0])
        heading = new_heading
    elif angle == -90 or angle == 270:
        new_heading = (-heading[1], heading[0])
        heading = new_heading
    elif abs(angle) == 180:
        new_heading = (-heading[0], -heading[1])
        heading = new_heading
    new_x = heading[0] * forward + position[0] + x
    new_y = heading[1] * forward + position[1] + y
    position = (new_x, new_y)
    print("new pos:", position)
