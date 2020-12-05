import sys
from os import system
import numpy as np
import time
import keyboard

file_path = 'inputs/day13_input.txt'


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
        # FIXME modified 3rd returned parameter for this puzzle! Probably should be changed for the next one
        return [2, 0, 0]
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


def draw_screen_in_file(screen):
    with open("output/game_board.txt", 'w', encoding="utf-8") as out_file:
        # Transposed game matrix as array handling made the x and y exchanged
        for row in np.transpose(screen):
            for element in row:
                if element == 0:
                    game_tile = '  '
                if element == 1:
                    game_tile = '██'
                if element == 2:
                    game_tile = '░░'
                if element == 3:
                    game_tile = '══'
                if element == 4:
                    game_tile = '\u256d\u256e'
                out_file.write(game_tile)
            out_file.write('\n')


def draw_screen(points, screen):
    system("cls")
    print("Points:", points)
    # Transposed game matrix as array handling made the x and y exchanged
    for row in np.transpose(screen):
        for element in row:
            if element == 0:
                game_tile = '  '
            if element == 1:
                game_tile = '██'
            if element == 2:
                game_tile = '░░'
            if element == 3:
                game_tile = '══'
            if element == 4:
                game_tile = '\u256d\u256e'
            print(game_tile, end="")
        print('\n', end="")


np.set_printoptions(threshold=sys.maxsize)

with open(file_path, 'r') as file:
    sequence = file.readline()

# Arbitrary large memory, hoping it will always be enough for the instructions
instructions_and_data = [0] * 640000
i = 0
for x in sequence.split(','):
    instructions_and_data[i] = int(x)
    i += 1

screen = np.zeros((40, 40))
screen = screen.astype(int)
phase = 0
points = 0
draw_screen(points, screen)
points_calculation = False
game_init = True
instructions_and_data[0] = 2

# Intcode computer reset
instruction_pointer = 0
relative_param_mode_base = 0


def check_keyboard_input():
    if keyboard.is_pressed("left"):
        return -1
    elif keyboard.is_pressed("right"):
        return 1
    return 0


while instructions_and_data[instruction_pointer] != 99:
    command_returned = execute_command(instruction_pointer, relative_param_mode_base, check_keyboard_input, store_output)
    prev_phase = phase
    phase = (phase + command_returned[2]) % 3
    if phase == 1 and prev_phase == 0:
        x = output_storage
        points_calculation = x == -1
        if points_calculation and game_init:
            game_init = False
    if phase == 2 and prev_phase == 1:
        y = output_storage
    if phase == 0 and prev_phase == 2:
        if not points_calculation:
            screen[x][y] = output_storage
        else:
            points = output_storage
        if not game_init:
            draw_screen(points, screen)
            time.sleep(0.001)

    # Next instruction in IntCode computer
    instruction_pointer += command_returned[0]
    # Change the memory offset base (only changes with command no. 9 in reality)
    relative_param_mode_base += command_returned[1]

block_cnt = 0
for row in screen:
    for element in row:
        if element == 2:
            block_cnt += 1
print("Remained blocks:", block_cnt)
