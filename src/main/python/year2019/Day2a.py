file_path = 'inputs/day2_input.txt'


def do_stuff(pos):
    if ints[pos] == 1:
        ints[ints[pos + 3]] = ints[ints[pos + 1]] + ints[ints[pos + 2]]
    elif ints[pos] == 2:
        ints[ints[pos + 3]] = ints[ints[pos + 1]] * ints[ints[pos + 2]]


with open(file_path, 'r') as file:
    sequence = file.readline()

ints = [int(x) for x in sequence.split(',')]
ints[1] = 12
ints[2] = 2

pos = 0
while ints[pos] != 99:
    do_stuff(pos)
    pos += 4

print("itt van hë", ints[0])
