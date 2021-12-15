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
# print(material_histogram)
max_amount = 0
min_amount = 10000000
for letter in material_histogram.keys():
    if material_histogram[letter] > max_amount:
        max_amount = material_histogram[letter]
    if material_histogram[letter] < min_amount:
        min_amount = material_histogram[letter]
print("Diff of most and least frequent materiel:", max_amount - min_amount)

rule_loops = {}
for rule_left in rules.keys():
    left_progenies = []
    right_progenies = []
    rolling_rule = rule_left[0] + rules[rule_left]
    while rolling_rule not in left_progenies:
        left_progenies.append(rolling_rule)
        rolling_rule = rolling_rule[0] + rules[rolling_rule]
    left_progenies.append(rolling_rule)
    rolling_rule = rules[rule_left] + rule_left[1]
    while rolling_rule not in right_progenies:
        right_progenies.append(rolling_rule)
        rolling_rule = rules[rolling_rule] + rolling_rule[1]
    right_progenies.append(rolling_rule)
    rule_loops[rule_left] = (left_progenies, right_progenies)
# print(rule_loops)

loop_data = {}
for start_point in rule_loops.keys():
    left_last = rule_loops[start_point][0][-1]
    left_n_const = []
    left_n_mod = []
    left_v_const = []
    left_v_mod = []
    left_mod = 0
    i = 0
    const_phase = True
    for left_progeny in rule_loops[start_point][0]:
        seek_end = False
        if left_progeny == left_last and const_phase:
            const_phase = False
            seek_end = True
            i = 0
        if const_phase:
            if left_progeny[1] == 'V':
                left_v_const.append(i)
            elif left_progeny[1] == 'N':
                left_n_const.append(i)
        elif left_progeny != left_last or not seek_end:
            if left_progeny[1] == 'V':
                left_v_mod.append(i)
            elif left_progeny[1] == 'N':
                left_n_mod.append(i)
            left_mod += 1
        i += 1
    left_data = [left_v_const, left_v_mod, left_n_const, left_n_mod, left_mod]
    right_last = rule_loops[start_point][1][-1]
    right_n_const = []
    right_n_mod = []
    right_v_const = []
    right_v_mod = []
    right_mod = 0
    i = 0
    const_phase = True
    for right_progeny in rule_loops[start_point][1]:
        seek_end = False
        if right_progeny == right_last and const_phase:
            const_phase = False
            seek_end = True
            i = 0
        if const_phase:
            if right_progeny[0] == 'V':
                right_v_const.append(i)
            elif right_progeny[0] == 'N':
                right_n_const.append(i)
        elif right_progeny != right_last or not seek_end:
            if right_progeny[0] == 'V':
                right_v_mod.append(i)
            elif right_progeny[0] == 'N':
                right_n_mod.append(i)
            right_mod += 1
        i += 1
    right_data = [right_v_const, right_v_mod, right_n_const, right_n_mod, right_mod]
    loop_data[start_point] = [left_data, right_data]
print(loop_data)

steps = 40
vs = 0
ns = 0
for i in range(len(base_material) - 1):
    generated = rules[base_material[i] + base_material[i + 1]]
    starter_pair = (base_material[i] + generated, generated + base_material[i + 1])
    for step_cnt in range(steps, 1, -1):
        if step_cnt in loop_data[starter_pair[0]][0][0]:
            vs += 1
        elif step_cnt in loop_data[starter_pair[0]][0][2]:
            ns += 1
        elif step_cnt - (len(rule_loops[starter_pair[0]]) - 1 - loop_data[starter_pair[0]][0][4]) > 0:
            if step_cnt - (len(rule_loops[starter_pair[0]]) - 1 - loop_data[starter_pair[0]][0][4]) % loop_data[starter_pair[0]][0][4] in loop_data[starter_pair[0]][0][1]:
                vs += 1
            elif step_cnt - (len(rule_loops[starter_pair[0]]) - 1 - loop_data[starter_pair[0]][0][4]) % loop_data[starter_pair[0]][0][4] in loop_data[starter_pair[0]][0][3]:
                ns += 1
        if step_cnt in loop_data[starter_pair[1]][1][0]:
            vs += 1
        elif step_cnt in loop_data[starter_pair[1]][1][2]:
            ns += 1
        elif step_cnt - (len(rule_loops[starter_pair[1]]) - 1 - loop_data[starter_pair[1]][1][4]) > 0:
            if step_cnt - (len(rule_loops[starter_pair[1]]) - 1 - loop_data[starter_pair[1]][1][4]) % loop_data[starter_pair[1]][1][4] in loop_data[starter_pair[1]][1][1]:
                vs += 1
            elif step_cnt - (len(rule_loops[starter_pair[1]]) - 1 - loop_data[starter_pair[1]][1][4]) % loop_data[starter_pair[1]][1][4] in loop_data[starter_pair[1]][1][3]:
                ns += 1
        new_pair = (rules[starter_pair[0]] + starter_pair[0][1], starter_pair[1][0] + rules[starter_pair[1]])
        starter_pair = new_pair

print("Vs", vs, "Ns", ns)
