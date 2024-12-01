file_path = 'inputs/day5.txt'

seeds = []
mappings = []
with open(file_path, 'r') as file:
    start = True
    current_mapping = []
    for line in file:
        if start:
            seeds = [int(i) for i in line.split(": ")[1].split()]
            start = False
        elif ':' in line and (len(current_mapping) != 0):
            mappings.append(current_mapping)
            current_mapping = []
        elif line != "\n" and not ':' in line:
            current_mapping.append([int(i) for i in line.split()])
    mappings.append(current_mapping)


# print(seeds)
# print(mappings)

seed_locations = []
for seed in seeds:
    target = seed
    for mapping_layer in mappings:
        for one_mapping in mapping_layer:
            # print("target is", target, "checking range", one_mapping)
            if target in range(one_mapping[1], one_mapping[1] + one_mapping[2]):
                # print("Wooohooo, found the range")
                target = one_mapping[0] + target - one_mapping[1]
                break
    seed_locations.append(target)

print(min(seed_locations))

i = 0
seed_intervals = []
for seed_coordinate in seeds:
    if i % 2 == 0:
        int_start = seed_coordinate
    else:
        seed_intervals.append([int_start, seed_coordinate])
    i += 1

print(seed_intervals)

actual_intervals = seed_intervals
for mapping_layer in mappings:
    for one_mapping in mapping_layer:
        # mapping contains actual
        # actual contains mapping
        # actual's end half in mapping
        # actual's starting half in mapping
