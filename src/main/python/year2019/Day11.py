import sys

import numpy as np

file_path = 'inputs/day11_input.txt'


# 56702 -> 2, 7, 6, 5
def parse_instruction(instruction):
    #         Command,
    return [instruction - (instruction // 100) * 100,
            # Parameter mode for parameter 1
            instruction // 100 - (instruction // 1000) * 10,
            # Parameter mode for parameter 2
            instruction // 1000 - (instruction // 10000) * 10,
            # Parameter mode for parameter 3
            instruction // 10000]


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
            exit(-1)
    return data


def keyboard_input():
    inp = int(input("Please add an input: "))
    if inp == 99:
        exit(-1)
    return inp


def stdout_output(value):
    print("Program output:", value)


def execute_command(instruction_pointer, relative_param_mode_base, input_callback=keyboard_input, output_callback=stdout_output):
    command_and_modes = parse_instruction(instructions_and_data[instruction_pointer])
    command_code = command_and_modes[0]
    if command_code == 1:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   instructions_and_data[instruction_pointer + 3], command_and_modes[1:], relative_param_mode_base)
        instructions_and_data[operands[2]] = operands[0] + operands[1]
        return [4, 0, 0]
    elif command_code == 2:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   instructions_and_data[instruction_pointer + 3], command_and_modes[1:], relative_param_mode_base)
        instructions_and_data[operands[2]] = operands[0] * operands[1]
        return [4, 0, 0]
    elif command_code == 3:
        operands = retrieve_data_and_write_address([], instructions_and_data[instruction_pointer + 1], command_and_modes[1:],
                                                   relative_param_mode_base)
        input_value = input_callback()
        instructions_and_data[operands[0]] = input_value
        return [2, 0, 1]
    elif command_code == 4:
        value_to_output = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1]], -63000, command_and_modes[1:],
                                                          relative_param_mode_base)
        output_callback(value_to_output[0])
        return [2, 0, 1]
    elif command_code == 5:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   -63000, command_and_modes[1:], relative_param_mode_base)
        value_to_check = operands[0]
        position_to_jump_to = operands[1]
        if value_to_check != 0:
            return [position_to_jump_to - instruction_pointer, 0, 0]
        else:
            return [3, 0, 0]
    elif command_code == 6:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   -63000, command_and_modes[1:], relative_param_mode_base)
        value_to_check = operands[0]
        position_to_jump_to = operands[1]
        if value_to_check == 0:
            return [position_to_jump_to - instruction_pointer, 0, 0]
        else:
            return [3, 0, 0]
    elif command_code == 7:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   instructions_and_data[instruction_pointer + 3], command_and_modes[1:], relative_param_mode_base)
        instructions_and_data[operands[2]] = 1 if operands[0] < operands[1] else 0
        return [4, 0, 0]
    elif command_code == 8:
        operands = retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1], instructions_and_data[instruction_pointer + 2]],
                                                   instructions_and_data[instruction_pointer + 3], command_and_modes[1:], relative_param_mode_base)
        instructions_and_data[operands[2]] = 1 if operands[0] == operands[1] else 0
        return [4, 0, 0]
    elif command_code == 9:
        return [2, retrieve_data_and_write_address([instructions_and_data[instruction_pointer + 1]], -63000, command_and_modes[1:],
                                                   relative_param_mode_base)[0], 0]
    else:
        print("Ooops - wrong command code", command_code)
        exit(-1)


# Storage for program outputs
def store_output(value):
    global output_storage
    output_storage = value


np.set_printoptions(threshold=sys.maxsize)

with open(file_path, 'r') as file:
    sequence = file.readline()

# Arbitrary large memory, hoping it will always be enough for the instructions
instructions_and_data = [0] * 640000
i = 0
for x in sequence.split(','):
    instructions_and_data[i] = int(x)
    i += 1

# Robot hardware
# Trying to contain the whole movement, starting with black (0) panels
hull = np.zeros((200, 200))
hull = hull.astype(int)
# Robot starting in the middle
robot_position = (100, 100)
# According to the second part of day11 puzzle, it should be a single white (1) starter field - uncomment below to solve 11a
hull[robot_position] = 1
# Robot heads north initially
robot_head = 0

# Intcode computer reset
instruction_pointer = 0
relative_param_mode_base = 0
# Basic starter phase/provided robot rotation info for the last round == 0, read a color input==1, provided a paint color == 2
phase = 0
points_painted = []
while instructions_and_data[instruction_pointer] != 99:
    # Giving the camera picture(color) as input and expecting the program to store output value if any
    command_returned = execute_command(instruction_pointer, relative_param_mode_base, lambda: hull[robot_position], lambda a: store_output(a))
    prev_phase = phase
    # It will only really increase if an input/output command was executed
    phase += command_returned[2]
    # Just got our first output
    if phase == 2 and prev_phase == 1:
        hull[robot_position] = output_storage
        # Collect not yet visited but now painted panel
        if robot_position not in points_painted:
            points_painted.append(robot_position)
    # We have got our movement instruction
    if phase == 3:
        (current_x, current_y) = robot_position
        # Rotating robot according to program output
        robot_head = (robot_head + 1) % 4 if output_storage == 1 else robot_head - 1
        if robot_head == -1:
            robot_head = 3
        # Moving robot by one panel towards its heading
        if robot_head == 0:
            robot_position = (current_x, current_y - 1)
        elif robot_head == 1:
            robot_position = (current_x + 1, current_y)
        elif robot_head == 2:
            robot_position = (current_x, current_y + 1)
        elif robot_head == 3:
            robot_position = (current_x - 1, current_y)

    # Next instruction in IntCode computer
    instruction_pointer += command_returned[0]
    # Change the memory offset base (only changes with command no. 9 in reality)
    relative_param_mode_base += command_returned[1]
    # If we have just done with a movement we should wait for the next input
    if phase > 2:
        phase = 0

print("No of points painted at least once:", len(points_painted))

with open("output/hull_painting.txt", 'w') as out_file:
    for row in np.transpose(hull):
        for element in row:
            out_file.write(element.astype(str))
        out_file.write('\n')
    out_file.close()
