file_path = 'inputs/day13.txt'

coordinates = []
instructions = []
with open(file_path, 'r') as file:
    instruction_phase = False
    for line in file:
        if not instruction_phase:
            if line.rstrip() == "":
                instruction_phase = True
            else:
                (x, y) = line.rstrip().split(',')
                coordinates.append([int(x), int(y)])
        else:
            (dim, amount) = line.rstrip().split(' ')[2].split("=")
            instructions.append([dim, int(amount)])
# print(coordinates, instructions)

first_fold = instructions[0]
max_x = 0
min_x = 10000
max_y = 0
min_y = 10000
for point in coordinates:
    max_x = max(max_x, point[0])
    max_y = max(max_y, point[1])
    min_x = min(min_x, point[0])
    min_y = min(min_y, point[1])

print("Min-max width, min-max length of the whole sheet:", min_x, max_x, min_y, max_y, first_fold)

paper = []
for y in range(max_y + 1):
    paper_row = []
    for x in range(max_x + 1):
        paper_row.append(0)
    paper.append(paper_row)

for point in coordinates:
    paper[point[1]][point[0]] = 1

new_x_range = max_x + 1
new_y_range = max_y + 1
for instruction in instructions:
    old_x = new_x_range
    old_y = new_y_range
    if instruction[0] == 'x':
        # print("Folding by x", instruction[1])
        new_x_range = instruction[1]
        for y in range(old_y):
            for x in range(new_x_range):
                if paper[y][old_x - x - 1] == 1:
                    # print("Found a folded 1 on", old_x - x, y, "goes to", x, y)
                    paper[y][x] = 1
    else:
        # print("Folding by y", instruction[1])
        new_y_range = instruction[1]
        for y in range(new_y_range):
            for x in range(old_x):
                if paper[old_y - y - 1][x] == 1:
                    # print("Found a folded 1 on", x, old_y - y, "goes to", x, y)
                    paper[y][x] = 1

for y in range(6):
    for x in range(40):
        print(paper[y][x], end='')
    print("\n")
# print(paper)
