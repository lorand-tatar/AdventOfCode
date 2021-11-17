file_path = 'inputs/day14_input.txt'
# file_path = 'inputs/day14_test_input.txt'

rules = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        (left, right) = line.split(" => ")
        rule = []
        for component in left.split(", "):
            (amount, ingredient) = component.split(" ")
            rule.append([ingredient, int(amount)])
        (amount, product) = right.split(" ")
        rule.append([product, int(amount)])
        rules.append(rule)

print(rules)

need = dict({"FUEL": 1})
leftover = dict({})
ore_needed = 0
rules_applied = len(rules) * [0]


def need_to_process(need):
    for stuff in need:
        if need[stuff] != 0:
            return True
    return False


while need_to_process(need):
    for stuff_to_craft in need:
        if need[stuff_to_craft] != 0:
            break
    # Looking up stuff in the stores
    stuff_name = stuff_to_craft
    stuff_amount = need[stuff_to_craft]

    if stuff_name not in leftover:
        leftover[stuff_name] = 0
    recycled_amount = leftover[stuff_name]
    if recycled_amount < stuff_amount:
        leftover[stuff_name] = 0
        stuff_amount -= recycled_amount
        #     Looking up the rule to craft the stuff
        i = 0
        for rule_for_craft in rules:
            i += 1
            if rule_for_craft[len(rule_for_craft) - 1][0] == stuff_name:
                break

        how_many_times = stuff_amount // rule_for_craft[len(rule_for_craft) - 1][1]
        if stuff_amount % rule_for_craft[len(rule_for_craft) - 1][1] != 0:
            how_many_times += 1
        rules_applied[i - 1] = rules_applied[i - 1] + how_many_times
        # We don't need these produced - go to the stores
        leftover[stuff_name] = how_many_times * rule_for_craft[len(rule_for_craft) - 1][1] - stuff_amount

        # Now we need the LHS of the equation
        for ingredient in rule_for_craft:
            if ingredient[0] != stuff_name:
                if ingredient[0] != "ORE":
                    if ingredient[0] not in need:
                        need[ingredient[0]] = 0
                    need[ingredient[0]] += how_many_times * ingredient[1]
                else:
                    ore_needed += how_many_times * ingredient[1]
    else:
        leftover[stuff_name] -= stuff_amount
        if leftover[stuff_name] < 0:
            leftover[stuff_name] = 0
    need[stuff_name] = 0

print("Ore needed", ore_needed)
print("Rules applied", rules_applied)
print("Need array - should be empty", need)
print("Leftover stuff", leftover)
