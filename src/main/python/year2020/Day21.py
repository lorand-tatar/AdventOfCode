import re

file_path = 'inputs/day21_input.txt'

allergene_mapping = {}
all_ingredients = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        matcher = re.search("^((\\w+\\s)+)\\(contains((\\s\\w+,)*)(\\s\\w+)\\)$", line)
        ingredients = set(matcher.group(1).rstrip().split(" "))
        for ingredient in ingredients:
            all_ingredients.append(ingredient)
        if matcher.group(3) is not None and matcher.group(3) != "":
            allergenes = matcher.group(3).lstrip() + matcher.group(5)
        else:
            allergenes = matcher.group(5)[1:]
        allergenes = allergenes.split(", ")
        for allergene in allergenes:
            if allergene not in allergene_mapping.keys():
                allergene_mapping[allergene] = ingredients
            else:
                allergene_mapping[allergene] = allergene_mapping[allergene].intersection(ingredients)
print(all_ingredients)
print(allergene_mapping)
all_allergene_containing = set()
for allergene in allergene_mapping.keys():
    for ingredient in allergene_mapping[allergene]:
        all_allergene_containing.add(ingredient)

print(all_allergene_containing)

non_allergic_count = 0
for ingredient in all_ingredients:
    if ingredient not in all_allergene_containing:
        non_allergic_count +=  1

print("So many non-allergic ingredient occurrences:", non_allergic_count)

# dairy -> dhfng
# wheat -> znrzgs
# shellfish -> nqbnmzx
# soy -> ntggc
# eggs -> pgblcd
# sesame -> dstct
# fish -> xhkdc
# peanuts -> ghlzj
# dhfng,pgblcd,xhkdc,ghlzj,dstct,nqbnmzx,ntggc,znrzgs