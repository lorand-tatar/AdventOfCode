file_path = 'inputs/day3.txt'

engine_map = []
with open(file_path, 'r') as file:
    for line in file:
        engine_map.append(line.rstrip())

number_positions = []
row = 0
for engine_line in engine_map:
    column = 0
    mark = 0
    for character in engine_line:
        if character.isdigit():
            mark += 1
        elif mark > 0:
            current_number = int(engine_line[column - 1])
            if mark > 1:
                current_number += 10 * int(engine_line[column - 2])
            if mark == 3:
                current_number += 100 * int(engine_line[column - 3])
            number_positions.append([current_number, row, column - mark, column - 1, []])
            mark = 0
        else:
            mark = 0
        column += 1
    if mark > 0:
        current_number = int(engine_line[column - 1])
        if mark > 1:
            current_number += 10 * int(engine_line[column - 2])
        if mark == 3:
            current_number += 100 * int(engine_line[column - 3])
        number_positions.append([current_number, row, column - mark, column - 1, []])
    row += 1

# print(engine_map[:3])

# print(number_positions)

sum_of_engine_parts = 0
table_dimensions = [len(engine_map), len(engine_map[0])]
for number in number_positions:
    # print(number)
    valid_part = False
    for x in range(number[2] - 1, number[3] + 2):
        for y in range(number[1] - 1, number[1] + 2):
            if 0 <= x < table_dimensions[0] and 0 <= y < table_dimensions[1]:
                if (not engine_map[y][x].isdigit()) and engine_map[y][x] != '.':
                    # print("Found char", engine_map[y][x], x, y)
                    valid_part = True
                    if engine_map[y][x] == '*':
                        number[4].append([y, x])
    if valid_part:
        sum_of_engine_parts += number[0]

print(sum_of_engine_parts)

gears = {}
for number in number_positions:
    for gear_around in number[4]:
        if str(1000 * gear_around[0] + gear_around[1]) in gears.keys():
            gears[str(1000 * gear_around[0] + gear_around[1])].append(number[0])
        else:
            numberlist = [number[0]]
            gears[str(1000 * gear_around[0] + gear_around[1])] = numberlist

sum_of_gear_powers = 0
for gear in gears.keys():
    if len(gears[gear]) == 2:
        sum_of_gear_powers += gears[gear][0] * gears[gear][1]

print(sum_of_gear_powers)
