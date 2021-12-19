file_path = 'inputs/day14_test.txt'

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

rule_futures = {}
for rule in rules.keys():
    left_progenies = []
    right_progenies = []
    rolling_rule = rule[0] + rules[rule]
    for i in range(50):
        left_progenies.append(rolling_rule)
        rolling_rule = rolling_rule[0] + rules[rolling_rule]
    left_progenies.append(rolling_rule)
    rolling_rule = rules[rule] + rule[1]
    for i in range(50):
        right_progenies.append(rolling_rule)
        rolling_rule = rules[rolling_rule] + rolling_rule[1]
    right_progenies.append(rolling_rule)
    rule_futures[rule] = (left_progenies, right_progenies)

no_of_rounds = 3
starter_pairs = []
for i in range(len(base_material) - 1):
    starter_pairs.append(base_material[i] + base_material[i + 1])
print(starter_pairs)
ns = 0
vs = 0
all_letters = 0
for starter in starter_pairs:
    # print(rule_futures[starter])
    print("Investigating starter", starter)
    left_product = rule_futures[starter][0][no_of_rounds - 1][1]
    right_product = rule_futures[starter][1][no_of_rounds - 1][0]
    print("Left and right product of starter:", left_product, right_product)
    all_letters += 4
    if 'H' == left_product:
        ns += 1
    if 'H' == right_product:
        ns += 1
    if 'B' == left_product:
        vs += 1
    if 'B' == right_product:
        vs += 1
    investigated_pair = (rule_futures[starter][0][1][1] + rule_futures[starter][0][0][1], rule_futures[starter][1][0][0] + rule_futures[starter][1][1][0])
    for j in range(no_of_rounds - 2, 0, -1):
        print("New pair to check", investigated_pair, "for", j, "rounds")
        left_product = rule_futures[investigated_pair[0]][0][j - 1][1]
        right_product = rule_futures[investigated_pair[1]][1][j - 1][0]
        all_letters += 2
        print("Left and right product of starter:", left_product, right_product)
        if 'H' == left_product:
            ns += 1
        if 'H' == right_product:
            ns += 1
        if 'B' == left_product:
            vs += 1
        if 'B' == right_product:
            vs += 1
        investigated_pair = (rules[investigated_pair[0]] + investigated_pair[0][1], investigated_pair[1][0] + rules[investigated_pair[1]])

print("Ns, Vs:", ns, vs, "Difference:", vs - ns)
print(all_letters)

