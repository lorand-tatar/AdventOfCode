import numpy as np
file_path = 'inputs/day5.txt'

line_segments = []
with open(file_path, 'r') as file:
    for line in file:
        (left, right) = line.rstrip().split(" -> ")
        (left_x, left_y) = left.split(",")
        (right_x, right_y) = right.split(",")
        left_point = [int(left_x), int(left_y)]
        right_point = [int(right_x), int(right_y)]
        line_segments.append([left_point, right_point])

# print(line_segments)

verticals_and_horizontals = []
diagonals = []
for line_segment in line_segments:
    if line_segment[0][0] == line_segment[1][0] or line_segment[0][1] == line_segment[1][1]:
        verticals_and_horizontals.append(line_segment)
    else:
        diagonals.append(line_segment)
# print(len(verticals_and_horizontals), "\n", verticals_and_horizontals)

map = []
planned_size = 1000
for i in range(planned_size):
    map.append(planned_size * [0])
# print(map)

for line_segment in verticals_and_horizontals:
    # print("points for line segment", line_segment)
    signum_x = np.sign(line_segment[1][0] - line_segment[0][0])
    signum_y = np.sign(line_segment[1][1] - line_segment[0][1])
    if signum_x == 0:
        signum_x = 1
    if signum_y == 0:
        signum_y = 1
    for x in range(line_segment[0][0], line_segment[1][0] + signum_x, signum_x):
        for y in range(line_segment[0][1], line_segment[1][1] + signum_y    , signum_y ):
            # print(x, y, end=';')
            map[y][x] += 1
    # print("\n")
# print(map)

for line_segment in diagonals:
    # print("points for line segment", line_segment)
    signum_x = np.sign(line_segment[1][0] - line_segment[0][0])
    signum_y = np.sign(line_segment[1][1] - line_segment[0][1])
    if signum_x == 0:
        signum_x = 1
    if signum_y == 0:
        signum_y = 1
    y = line_segment[0][1]
    for x in range(line_segment[0][0], line_segment[1][0] + signum_x, signum_x):
        # print(x, y, end=';')
        map[y][x] += 1
        y += signum_y
    # print("\n")
# print(map)

overlapped_vents_cnt = 0
for y in map:
    for x in y:
        if x >= 2:
            overlapped_vents_cnt += 1
print("Overlapped vent spots count", overlapped_vents_cnt)
