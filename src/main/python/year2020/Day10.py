file_path = 'inputs/day10_input.txt'

jolts = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        jolts.append(int(line))

device_jolt = max(jolts) + 3
jolts.append(device_jolt)
jolts.sort()
print(jolts)


i = 0
if jolts[0] == 1:
    diffs_of_1 = 1
    diffs_of_3 = 0
elif jolts[0] == 3:
    diffs_of_1 = 0
    diffs_of_3 = 1
prev_was_1 = diffs_of_1 == 1
section_length = 0
diff_1_section_lengths = []
while i != len(jolts) - 1:
    if jolts[i + 1] - jolts[i] == 1:
        if not prev_was_1:
            diff_1_section_lengths.append(section_length)
            section_length = 0
        diffs_of_1 += 1
        section_length += 1
        prev_was_1 = True
    elif jolts[i + 1] - jolts[i] == 3:
        diffs_of_3 += 1
        prev_was_1 = False
    i += 1
diff_1_section_lengths.append(section_length)

diff_1_section_lengths[0] = diff_1_section_lengths[0] + 1
print("The product of 1 and 3 diffs:", diffs_of_3 * diffs_of_1)
print(diff_1_section_lengths)
variations = []
factors = [1, 2, 4, 7]
for section in diff_1_section_lengths:
    variations.append(factors[section - 1])
all_possibilities = 1
for poss in variations:
    all_possibilities *= poss

print(variations)
print(all_possibilities)
