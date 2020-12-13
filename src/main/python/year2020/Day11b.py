file_path = 'inputs/day11_input.txt'

seats_raw = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        seat_line = []
        for place in line:
            if place == '.':
                seat_line.append(0)
            elif place == 'L':
                seat_line.append(1)
        seats_raw.append(seat_line)

padding_line = [0] * (len(seat_line) + 2)
seats = [padding_line]
for seatline in seats_raw:
    new_seatline = [0]
    for raw_seat in seatline:
        new_seatline.append(raw_seat)
    new_seatline.append(0)
    seats.append(new_seatline)
seats.append(padding_line)


def print_all(seats):
    for line in seats:
        for seat in line:
            print(seat, end="")
        print("\n")


def check_empty_directions(seats, i, j):
    max_x = len(seats)
    max_y = len(seats[0])
    run_x = i
    run_y = j
    while run_x in range(0, max_x) and run_y in range(0, max_y):
        if (run_x != i or run_y != j) and seats[run_x][run_y] == 1:
            break
        if seats[run_x][run_y] == 2:
            return False
        run_x -= 1
        run_y -= 1
    run_x = i
    run_y = j
    while run_x in range(0, max_x) and run_y in range(0, max_y):
        if (run_x != i or run_y != j) and seats[run_x][run_y] == 1:
            break
        if seats[run_x][run_y] == 2:
            return False
        run_x += 1
        run_y += 1
    run_x = i
    run_y = j
    while run_x in range(0, max_x) and run_y in range(0, max_y):
        if (run_x != i or run_y != j) and seats[run_x][run_y] == 1:
            break
        if seats[run_x][run_y] == 2:
            return False
        run_x += 1
        run_y -= 1
    run_x = i
    run_y = j
    while run_x in range(0, max_x) and run_y in range(0, max_y):
        if (run_x != i or run_y != j) and seats[run_x][run_y] == 1:
            break
        if seats[run_x][run_y] == 2:
            return False
        run_x -= 1
        run_y += 1
    run_x = i
    while run_x in range(0, max_x):
        if (run_x != i) and seats[run_x][j] == 1:
            break
        if seats[run_x][j] == 2:
            return False
        run_x -= 1
    run_x = i
    while run_x in range(0, max_x):
        if (run_x != i) and seats[run_x][j] == 1:
            break
        if seats[run_x][j] == 2:
            return False
        run_x += 1
    run_y = j
    while run_y in range(0, max_y):
        if (run_y != j) and seats[i][run_y] == 1:
            break
        if seats[i][run_y] == 2:
            return False
        run_y -= 1
    run_y = j
    while run_y in range(0, max_y):
        if (run_y != j) and seats[i][run_y] == 1:
            break
        if seats[i][run_y] == 2:
            return False
        run_y += 1
    return True


def too_crowdy(seats, i, j):
    taken_count = 0
    max_x = len(seats)
    max_y = len(seats[0])
    run_x = i
    run_y = j
    while run_x in range(0, max_x) and run_y in range(0, max_y):
        if seats[run_x][run_y] == 1:
            break
        if (run_x != i or run_y != j) and seats[run_x][run_y] == 2:
            taken_count += 1
            break
        run_x -= 1
        run_y -= 1
    run_x = i
    run_y = j
    while run_x in range(0, max_x) and run_y in range(0, max_y):
        if seats[run_x][run_y] == 1:
            break
        if (run_x != i or run_y != j) and seats[run_x][run_y] == 2:
            taken_count += 1
            break
        run_x += 1
        run_y += 1
    run_x = i
    run_y = j
    while run_x in range(0, max_x) and run_y in range(0, max_y):
        if seats[run_x][run_y] == 1:
            break
        if (run_x != i or run_y != j) and seats[run_x][run_y] == 2:
            taken_count += 1
            break
        run_x += 1
        run_y -= 1
    run_x = i
    run_y = j
    while run_x in range(0, max_x) and run_y in range(0, max_y):
        if seats[run_x][run_y] == 1:
            break
        if (run_x != i or run_y != j) and seats[run_x][run_y] == 2:
            taken_count += 1
            break
        run_x -= 1
        run_y += 1
    run_x = i
    while run_x in range(0, max_x):
        if seats[run_x][j] == 1:
            break
        if (run_x != i) and seats[run_x][j] == 2:
            taken_count += 1
            break
        run_x -= 1
    run_x = i
    while run_x in range(0, max_x):
        if seats[run_x][j] == 1:
            break
        if (run_x != i) and seats[run_x][j] == 2:
            taken_count += 1
            break
        run_x += 1
    run_y = j
    while run_y in range(0, max_y):
        if seats[i][run_y] == 1:
            break
        if (run_y != j) and seats[i][run_y] == 2:
            taken_count += 1
            break
        run_y -= 1
    run_y = j
    while run_y in range(0, max_y):
        if seats[i][run_y] == 1:
            break
        if (run_y != j) and seats[i][run_y] == 2:
            taken_count += 1
            break
        run_y += 1
    return taken_count >= 5


changed = True
while changed:
    changed = False
    i = 1
    new_seating = [seats[0]]
    while i < len(seats) - 1:
        j = 1
        new_seatline = [0]
        seat_line = seats[i]
        while j < len(seat_line) - 1:
            if seat_line[j] == 1 and check_empty_directions(seats, i, j):
                new_seatline.append(2)
                changed = True
            elif seat_line[j] == 2 and too_crowdy(seats, i, j):
                new_seatline.append(1)
                changed = True
            else:
                new_seatline.append(seat_line[j])
            j += 1
        new_seatline.append(0)
        new_seating.append(new_seatline)
        i += 1
    new_seating.append(seats[0])
    seats = new_seating

count = 0
for line in seats:
    for seat in line:
        if seat == 2:
            count += 1

print("Count of all taken seats:", count)
