file_path = 'inputs/day8_input.txt'

instructions = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        (command, value) = line.split(" ")
        instructions.append((command, int(value)))

normal_termination = False
i = 0
while not normal_termination:
    if instructions[i][0] in ("jmp", "nop"):
        copy_of_inst = []
        for inst in instructions:
            copy_of_inst.append(inst)
        if instructions[i][0] == "jmp":
            copy_of_inst[i] = ("nop", copy_of_inst[i][1])
        elif instructions[i][0] == "nop":
            copy_of_inst[i] = ("jmp", copy_of_inst[i][1])

        accumulator = 0
        position = 0
        visited_positions = set()
        while (position not in visited_positions) and position < len(copy_of_inst):
            visited_positions.add(position)
            (command, value) = copy_of_inst[position]
            if command == "acc":
                accumulator += value
                position += 1
            elif command == "jmp":
                position += value
            elif command == "nop":
                position += 1
            else:
                print("Ooops wrong command!")
        normal_termination = position >= len(copy_of_inst)
    i += 1

print("Last acc value:", accumulator)
