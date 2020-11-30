import numpy as np

file_path = 'inputs/day9a_input.txt'


def parse_instruction(instruction):
    #         Command,
    return [instruction - (instruction // 100) * 100,
            # Parameter mode for parameter 1
            instruction // 100 - (instruction // 1000) * 10,
            # Parameter mode for parameter 2
            instruction // 1000 - (instruction // 10000) * 10,
            # Parameter mode for parameter 3
            instruction // 10000]
# 56702 -> 2, 7, 6, 5


def retrieve_data_and_write_address(mem_read_parameters, mem_write_parameter, modes, relative_param_mode_base):
    data = []
    for i in range(len(mem_read_parameters)):
        parameter = mem_read_parameters[i]
        mode = modes[i]
        # Address mode
        if mode == 0:
            data.append(instructions_and_data[parameter])
        # Direct value mode
        elif mode == 1:
            data.append(parameter)
        # Relative offset address mode
        elif mode == 2:
            data.append(instructions_and_data[parameter + relative_param_mode_base])
        else:
            print("Ooops, wrong memory read parameter mode:", mode)
            exit(-1)
    # I know it's ugly - should have used another (boolean) parameter for that
    if mem_write_parameter != -63000:
        write_mode = modes[len(mem_read_parameters)]
        # Direct address to write to
        if write_mode == 0:
            data.append(mem_write_parameter)
        # Relative address to write to
        elif write_mode == 2:
            data.append(mem_write_parameter + relative_param_mode_base)
        else:
            print("Ooops, wrong memory write parameter mode", write_mode)
    return data


def execute_command(instruction_pointer, relative_param_mode_base):
    command_and_modes = parse_instruction(instructions_and_data[instruction_pointer])
    command_code = command_and_modes[0]
    if command_code == 1:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   instructions_and_data[instruction_pointer + 3], command_and_modes[1:], relative_param_mode_base)
        instructions_and_data[operands[2]] = operands[0] + operands[1]
        return [4, 0]
    elif command_code == 2:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   instructions_and_data[instruction_pointer + 3], command_and_modes[1:], relative_param_mode_base)
        instructions_and_data[operands[2]] = operands[0] * operands[1]
        return [4, 0]
    elif command_code == 3:
        operands = retrieve_data_and_write_address([], instructions_and_data[instruction_pointer + 1], command_and_modes[1:], relative_param_mode_base)
        typed_value = int(input("Please add an input: "))
        instructions_and_data[operands[0]] = typed_value
        return [2, 0]
    elif command_code == 4:
        value_to_print = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1]], -63000, command_and_modes[1:], relative_param_mode_base)
        print("Program output:", value_to_print[0])
        return [2, 0]
    elif command_code == 5:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   -63000, command_and_modes[1:], relative_param_mode_base)
        value_to_check = operands[0]
        position_to_jump_to = operands[1]
        if value_to_check != 0:
            return [position_to_jump_to - instruction_pointer, 0]
        else:
            return [3, 0]
    elif command_code == 6:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   -63000, command_and_modes[1:], relative_param_mode_base)
        value_to_check = operands[0]
        position_to_jump_to = operands[1]
        if value_to_check == 0:
            return [position_to_jump_to - instruction_pointer, 0]
        else:
            return [3, 0]
    elif command_code == 7:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   instructions_and_data[instruction_pointer + 3], command_and_modes[1:], relative_param_mode_base)
        instructions_and_data[operands[2]] = 1 if operands[0] < operands[1] else 0
        return [4, 0]
    elif command_code == 8:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   instructions_and_data[instruction_pointer + 3], command_and_modes[1:], relative_param_mode_base)
        instructions_and_data[operands[2]] = 1 if operands[0] == operands[1] else 0
        return [4, 0]
    elif command_code == 9:
        return [2, retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1]], -63000, command_and_modes[1:], relative_param_mode_base)[0]]
    else:
        print("Ooops - wrong command code", command_code)
        exit(-1)


with open(file_path, 'r') as file:
    sequence = file.readline()

# Arbitrary large memory, hoping it will always be enough
instructions_and_data = [0] * 64000000
i = 0
for x in sequence.split(','):
    instructions_and_data[i] = int(x)
    i += 1

instruction_pointer = 0
relative_param_mode_base = 0
while instructions_and_data[instruction_pointer] != 99:
    offsets = execute_command(instruction_pointer, relative_param_mode_base)
    instruction_pointer += offsets[0]
    relative_param_mode_base += offsets[1]
