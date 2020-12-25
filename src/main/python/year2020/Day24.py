file_path = 'inputs/day24_input.txt'

trips = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        north = False
        south = False
        trip = []
        for char in line:
            if north and char == 'w':
                trip.append((-1, 1))
                north = False
            elif north and char == 'e':
                trip.append((0, 1))
                north = False
            elif char == 'n':
                north = True
            elif char == 's':
                south = True
            elif south and char == 'w':
                trip.append((0, -1))
                south = False
            elif south and char == 'e':
                trip.append((1, -1))
                south = False
            elif char == 'w':
                trip.append((-1, 0))
            elif char == 'e':
                trip.append((1, 0))
        trips.append(trip)

# print(trips, len(trips))

white_hexas = set()
for i in range(-200, 200):
    for j in range(-200, 200):
        white_hexas.add((i, j))

black_hexas = set()
for trip in trips:
    pos = (0, 0)
    for move in trip:
        pos = (pos[0] + move[0], pos[1] + move[1])
    if pos in black_hexas:
        black_hexas.remove(pos)
    else:
        black_hexas.add(pos)

print("Number of black hexas at the end:", len(black_hexas))


def count_black_neighbors(hexa, black_hexas):
    black_cnt = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != j and (hexa[0] + i, hexa[1] + j) in black_hexas:
                black_cnt += 1
    return black_cnt


# print("Starter blacks:", black_hexas)
day = 0
while day < 100:
    new_white = white_hexas.copy()
    new_black = black_hexas.copy()
    for black in black_hexas:
        black_neighbor_cnt = count_black_neighbors(black, black_hexas)
        if black_neighbor_cnt == 0 or black_neighbor_cnt > 2:
            new_black.remove(black)
            new_white.add(black)
    for white in white_hexas:
        black_neighbor_cnt = count_black_neighbors(white, black_hexas)
        if black_neighbor_cnt == 2:
            new_black.add(white)
            new_white.remove(white)
    white_hexas = new_white
    black_hexas = new_black
    day += 1
    print("##### After day", day, len(black_hexas))
    # print(black_hexas)

print("Number of black hexas at the end:", len(black_hexas))
