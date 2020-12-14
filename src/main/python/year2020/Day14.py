import  re

file_path = 'inputs/day14_input.txt'

memory = {}
and_filter = 0
or_filter = 0
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        (command, value) = line.split(" = ")
        if command == "mask":
            and_filter = int(value.replace("X", "1"), 2)
            or_filter = int(value.replace("X", "0"), 2)
        else:
            addressmatcher = re.search("^mem\\[(\d+)\\]$", command)
            address = int(addressmatcher.group(1))
            memory[address] = (int(value) | or_filter) & and_filter

print("Sum of all memory values:", sum(memory.values()))
