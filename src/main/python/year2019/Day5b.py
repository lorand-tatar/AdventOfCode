file_path = 'inputs/day5_input.txt'


def parse_instr(command):
    return [command - (command // 100) * 100,
            command // 100 - (command // 1000) * 10,
            command // 1000 - (command // 10000) * 10,
            command // 10000]
# 56702 -> 2, 7, 6, 5


def do_stuff(pos):
    instr_with_modes = parse_instr(ints[pos])
    if instr_with_modes[0] == 1:
        first_param = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        second_param = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]

        ints[ints[pos + 3]] = first_param + second_param
        return 4
    elif instr_with_modes[0] == 2:
        first_param = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        second_param = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]

        ints[ints[pos + 3]] = first_param * second_param
        return 4
    elif instr_with_modes[0] == 3:
        typed_value = int(input("Please add an input: "))
        ints[ints[pos + 1]] = typed_value
        return 2
    elif instr_with_modes[0] == 4:
        value_to_print = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        print("Program output:", value_to_print)
        return 2
    elif instr_with_modes[0] == 5:
        value_to_check = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        position_to_jump_to = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]
        if value_to_check != 0:
            return position_to_jump_to - pos
        else:
            return 3
    elif instr_with_modes[0] == 6:
        value_to_check = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        position_to_jump_to = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]
        if value_to_check == 0:
            return position_to_jump_to - pos
        else:
            return 3
    elif instr_with_modes[0] == 7:
        first_param = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        second_param = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]

        ints[ints[pos + 3]] = 1 if first_param < second_param else 0
        return 4
    elif instr_with_modes[0] == 8:
        first_param = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        second_param = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]

        ints[ints[pos + 3]] = 1 if first_param == second_param else 0
        return 4
    else:
        print("Ooops - wrong code")
        exit(-1)


with open(file_path, 'r') as file:
    sequence = file.readline()

ints = [int(x) for x in sequence.split(',')]

pos = 0
while ints[pos] != 99:
    pos += do_stuff(pos)
