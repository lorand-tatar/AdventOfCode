import itertools

file_path = 'inputs/day7a_input.txt'


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
        # Command offset, no input read, no output
        return [4, 0, -1]
    elif instr_with_modes[0] == 2:
        first_param = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        second_param = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]

        ints[ints[pos + 3]] = first_param * second_param
        # Command offset, no input read, no output
        return [4, 0, -1]
    elif instr_with_modes[0] == 3:
        if input_pick == 0:
            typed_value = phase
        else:
            typed_value = data_input
        ints[ints[pos + 1]] = typed_value
        # Command offset, input read, no output
        return [2, 1, -1]
    elif instr_with_modes[0] == 4:
        value_to_print = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        # print("Program output for amplifier", curr_amp, ":", value_to_print)
        # Command offset, no input read, output returned
        return [2, 0, value_to_print]
    elif instr_with_modes[0] == 5:
        value_to_check = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        position_to_jump_to = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]
        if value_to_check != 0:
            # Command offset, no input read, no output
            return [position_to_jump_to - pos, 0, -1]
        else:
            # Command offset, no input read, no output
            return [3, 0, -1]
    elif instr_with_modes[0] == 6:
        value_to_check = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        position_to_jump_to = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]
        if value_to_check == 0:
            # Command offset, no input read, no output
            return [position_to_jump_to - pos, 0, -1]
        else:
            # Command offset, no input read, no output
            return [3, 0, -1]
    elif instr_with_modes[0] == 7:
        first_param = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        second_param = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]

        ints[ints[pos + 3]] = 1 if first_param < second_param else 0
        # Command offset, no input read, no output
        return [4, 0, -1]
    elif instr_with_modes[0] == 8:
        first_param = ints[pos + 1] if instr_with_modes[1] == 1 else ints[ints[pos + 1]]
        second_param = ints[pos + 2] if instr_with_modes[2] == 1 else ints[ints[pos + 2]]

        ints[ints[pos + 3]] = 1 if first_param == second_param else 0
        # Command offset, no input read, no output
        return [4, 0, -1]
    else:
        print("Ooops - wrong command code")
        exit(-1)


with open(file_path, 'r') as file:
    sequence = file.readline()
# Original reset program
original_ints = [int(x) for x in sequence.split(',')]

# Phase sequence plan
valid_phases = (0, 1, 2, 3, 4)
phase_inputs = list(itertools.permutations(valid_phases))
maximum_thrust = 0
for phase_input in phase_inputs:
    # Starting data for the whole program
    data_input = 0
    output = -1
    for curr_amp in range(5):
        # Resetting moving pointer
        pos = 0
        # Resetting program to original
        ints = original_ints
        # Phase for this round
        phase = phase_input[curr_amp]
        # Next input param will take phase
        input_pick = 0
        while ints[pos] != 99:
            result = do_stuff(pos)
            # Program code offset
            pos += result[0]
            # An input has read, next input should read data
            if result[1] == 1:
                input_pick = 1
            # If we have an output from the command that should be saved - thus we only expect 1 output during program execution
            # or else we'll go with the last one
            if result[2] != -1:
                output = result[2]
        # Feeding the current amp's output to next one's input
        if output == -1:
            print("Ooops, -1 output, something went wrong")
            exit(-1)
        data_input = output

    # print("Output after all 5 amplifiers:", output)
    if output > maximum_thrust:
        maximum_thrust = output
        maximizing_permutation = phase_input

print("Max thrust is", maximum_thrust, "using the following phase permutation:", maximizing_permutation)
