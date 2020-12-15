import re

file_path = 'inputs/day14_input.txt'

memory = {}
mask = None
with open(file_path, 'r') as file:
    line_no = 0
    for line in file:
        line = line.rstrip()
        (command, value) = line.split(" = ")
        if command == "mask":
            mask = value
        else:
            addressmatcher = re.search("^mem\\[(\d+)\\]$", command)
            raw_address = addressmatcher.group(1)
            binary_raw_address = bin(int(raw_address))[2:]
            no_of_bits = len(binary_raw_address)
            binary_raw_address = ((36 - no_of_bits) * '0').__add__(binary_raw_address)
            i = 0
            masked_address = ""
            for bit in binary_raw_address:
                current_mask_bit = mask[i]
                if current_mask_bit != '0':
                    masked_address = masked_address.__add__(current_mask_bit)
                else:
                    masked_address = masked_address.__add__(bit)
                i += 1
            addresses_to_write = set()
            number_of_x = len([elem for elem in masked_address if elem == 'X'])
            # if line_no < 75:
            #     print("###########")
            #     print(raw_address, len(binary_raw_address), mask)
            #     print(masked_address, len(masked_address), number_of_x)
            for fill_pattern in range(pow(2, number_of_x)):
                new_address = masked_address
                binary_fill_pattern = bin(fill_pattern)[2:]
                binary_fill_pattern = ((number_of_x - len(binary_fill_pattern)) * '0').__add__(binary_fill_pattern)
                for x_bit in binary_fill_pattern:
                    new_address = new_address.replace('X', x_bit, 1)
                addresses_to_write.add(int(new_address, 2))
            # if line_no < 75:
            #     print(addresses_to_write)
            for address in addresses_to_write:
                memory[address] = int(value)
        line_no += 1
        # if line_no == 75:
        #     print("Entries:", len(memory.keys()))
        #     print(memory)
        #     subsum = 0
        #     for key in memory.keys():
        #         subsum += memory[key]
        #     print("Subsum:", sum(memory.values()), "vs", subsum)

print("Sum of all memory values:", sum(memory.values()))
