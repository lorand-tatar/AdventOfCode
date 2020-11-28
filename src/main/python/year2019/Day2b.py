file_path = 'inputs/day2a_input.txt'


def do_stuff(pos):
    if ints[pos] == 1:
        ints[ints[pos + 3]] = ints[ints[pos + 1]] + ints[ints[pos + 2]]
    elif ints[pos] == 2:
        ints[ints[pos + 3]] = ints[ints[pos + 1]] * ints[ints[pos + 2]]


def main_loop():
    pos = 0
    while ints[pos] != 99:
        do_stuff(pos)
        pos += 4


with open(file_path, 'r') as file:
    sequence = file.readline()

target_number = 19690720

for i in range(100):
    for j in range(100):
        ints = [int(x) for x in sequence.split(',')]
        ints[1] = i
        ints[2] = j
        main_loop()
        print("these are the input numbers you're looking for", i, j) if ints[0] == target_number else ""
