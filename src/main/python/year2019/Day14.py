file_path = 'inputs/day14_input.txt'

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

fuel_rule = None
for rule in rules:
    if rule[len(rule) - 1][0] == "FUEL":
        fuel_rule = rule
        break

necessary_materiel = fuel_rule[:len(fuel_rule) - 1]


def just_ore_needed(necessary_materiel):
    for entry in necessary_materiel:
        if entry[0] != "ORE":
            return False
    return True


while not just_ore_needed(necessary_materiel):
    new_stuff_needed = []
    for component in necessary_materiel:
        if component[0] != "ORE":
            for rule in rules:
                if rule[len(rule) - 1][0] == component[0]:
                    product_amount = rule[len(rule) - 1][1]
                    necessary_product_amount = component[1]
                    factor = (necessary_product_amount - 1) // product_amount + 1
                    for stuff in rule[:len(rule) - 1]:
                        stuff[1] = stuff[1] * factor
                        new_stuff_needed.append(stuff)
                    break
            component[1] = -1
    for stuff in new_stuff_needed:
        necessary_materiel.append(stuff)
    cleaned_list = []
    for component in necessary_materiel:
        if component[1] != -1:
            cleaned_list.append(component)
    for component in cleaned_list:
        name = component[0]
        saved = component[1]
        sum = 0
        if sum != -1:
            for other in cleaned_list:
                if other[1] != -1 and other[0] == name:
                    sum += other[1]
                    other[1] = -1
    # This is a mess - should build a whole new list, with summarized quantities
    # then the next -1 hunting is also unnecessary
            component[1] = sum
    print("Cleaned of resolved stuff, marked duplicates:", cleaned_list)
    necessary_materiel = []
    for component in cleaned_list:
        if component[1] != -1:
            necessary_materiel.append(component)
    print("After final cleanup", necessary_materiel)

print(necessary_materiel)
