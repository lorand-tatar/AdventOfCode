file_path = 'inputs/day14.txt'

base_material = ""
rules = {}
with open(file_path, 'r') as file:
    read_rules = False
    for line in file:
        if not read_rules:
            if line.rstrip() == "":
                read_rules = True
            else:
                base_material = line.rstrip()
        else:
            (from_stuff, inserted_stuff) = line.rstrip().split(" -> ")
            rules[from_stuff] = inserted_stuff
# print(base_material)
# print(rules)

no_of_rounds = 10
new_material = base_material
for i in range(no_of_rounds):
    # print("@@@@@@@@@@ Round", i)
    prev_material = new_material
    new_material = ""
    # print("####### Blowing up", prev_material)
    for j in range(len(prev_material) - 1):
        if j == 0:
            new_material = new_material + prev_material[j]
        if prev_material[j] + prev_material[j + 1] in rules.keys():
            new_material = new_material + rules[prev_material[j] + prev_material[j + 1]]
        new_material = new_material + prev_material[j + 1]
    # print("Results", new_material)

material_histogram = {}
for material in new_material:
    if material not in material_histogram.keys():
        material_histogram[material] = 1
    else:
        material_histogram[material] += 1
print(material_histogram)
max_amount = 0
min_amount = 10000000
for letter in material_histogram.keys():
    if material_histogram[letter] > max_amount:
        max_amount = material_histogram[letter]
    if material_histogram[letter] < min_amount:
        min_amount = material_histogram[letter]
print("Diff of most and least frequent materiel:", max_amount - min_amount)


no_of_rounds = 40
starter_pairs = []
pair_histogram = {}
for i in range(len(base_material) - 1):
    pair = base_material[i] + base_material[i + 1]
    starter_pairs.append(pair)
    if pair not in pair_histogram.keys():
        pair_histogram[pair] = 1
    else:
        pair_histogram[pair] += 1
# print(starter_pairs)

for i in range(no_of_rounds):
    next_histogram = {}
    for pair_key in pair_histogram.keys():
        children = [pair_key[0] + rules[pair_key], rules[pair_key] + pair_key[1]]
        for child in children:
            if child not in next_histogram.keys():
                next_histogram[child] = pair_histogram[pair_key]
            else:
                next_histogram[child] += pair_histogram[pair_key]
    pair_histogram = next_histogram.copy()

letter_histogram = {}
for pair in pair_histogram.keys():
    for letter in pair:
        if letter not in letter_histogram.keys():
            letter_histogram[letter] = pair_histogram[pair]
        else:
            letter_histogram[letter] += pair_histogram[pair]
for letter in letter_histogram.keys():
    letter_histogram[letter] //= 2
letter_histogram[base_material[0]] += 1
letter_histogram[base_material[-1]] += 1
print(letter_histogram)
print("Diff between max and min:", max(letter_histogram.values()) - min(letter_histogram.values()))

