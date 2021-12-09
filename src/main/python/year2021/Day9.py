from typing import List

file_path = 'inputs/day9.txt'

map = []
with open(file_path, 'r') as file:
    for line in file:
        map_line = []
        for depth in line.rstrip():
            map_line.append(int(depth))
        map.append(map_line)
# print(map)

i = 0
j = 0
low_extremes = []
for y in map:
    i = 0
    for x in y:
        # print("Checking point", i, j)
        low_extreme = True
        if i - 1 >= 0:
            low_extreme = low_extreme and map[j][i - 1] > x
        if i + 1 < len(y):
            low_extreme = low_extreme and map[j][i + 1] > x
        if j - 1 >= 0:
            low_extreme = low_extreme and map[j - 1][i] > x
        if j + 1 < len(map):
            low_extreme = low_extreme and map[j + 1][i] > x
        if low_extreme:
            low_extremes.append([[i, j], x])
        i += 1
    j += 1

sum_risk = 0
for extreme in low_extremes:
    sum_risk += extreme[1] + 1
print("Sum risk:", sum_risk)
# print(low_extremes)

basin_sizes = {}
for low_point in low_extremes:
    basin_sizes[(low_point[0][0], low_point[0][1])] = 0
# print(basin_sizes)

for y in range(100):
    for x in range(100):
        current_point = map[y][x]
        if current_point != 9:
            # print("############ Flowing from", x, y)
            flowing_point = [y, x]
            while (flowing_point[1], flowing_point[0]) not in basin_sizes.keys():
                # print("Not a low point, so flowing towards", end='')
                gradients: list[int] = [10, 10, 10, 10]
                if flowing_point[1] - 1 >= 0:
                    gradients[3] = map[flowing_point[0]][flowing_point[1] - 1] - current_point
                if flowing_point[1] + 1 < 100:
                    gradients[1] = map[flowing_point[0]][flowing_point[1] + 1] - current_point
                if flowing_point[0] - 1 >= 0:
                    gradients[0] = map[flowing_point[0] - 1][flowing_point[1]] - current_point
                if flowing_point[0] + 1 < 100:
                    gradients[2] = map[flowing_point[0] + 1][flowing_point[1]] - current_point
                min_grad = min(gradients)
                for i in range(4):
                    if gradients[i] == min_grad:
                        if i == 0:
                            flowing_point[0] -= 1
                        if i == 1:
                            flowing_point[1] += 1
                        if i == 2:
                            flowing_point[0] += 1
                        if i == 3:
                            flowing_point[1] -= 1
                        current_point = map[flowing_point[0]][flowing_point[1]]
                        break
                # print(flowing_point[0], flowing_point[1], "value", current_point, end="\n")
            # print("Low point reached!")
            basin_sizes[(flowing_point[1], flowing_point[0])] += 1

# print(basin_sizes)
sizes = list(basin_sizes.values())
sizes.sort(reverse=True)
# print(sizes)
print("The multiple of the sizes of the three biggest basins:", sizes[0] * sizes[1] * sizes[2])
