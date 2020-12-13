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

waypoint_relative_pos = (10, -1)
ship_pos = (0, 0)
for move in moves:
    print("### After move", move)
    (x, y, forward, angle) = move
    if angle == 90 or angle == -270:
        new_heading = (waypoint_relative_pos[1], -waypoint_relative_pos[0])
        waypoint_relative_pos = new_heading
    elif angle == -90 or angle == 270:
        new_heading = (-waypoint_relative_pos[1], waypoint_relative_pos[0])
        waypoint_relative_pos = new_heading
    elif abs(angle) == 180:
        new_heading = (-waypoint_relative_pos[0], -waypoint_relative_pos[1])
        waypoint_relative_pos = new_heading
    waypoint_relative_pos = (waypoint_relative_pos[0] + x, waypoint_relative_pos[1] + y)
    ship_pos = (ship_pos[0] + forward * waypoint_relative_pos[0], ship_pos[1] + forward * waypoint_relative_pos[1])
    print("new pos:", ship_pos)
