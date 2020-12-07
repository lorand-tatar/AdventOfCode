import re

file_path = 'inputs/day7_input.txt'

rules = []
with open(file_path, 'r') as file:
    for line in file:
        line.rstrip()
        (wrapper, wrapped) = line.split(" bags contain ")
        (wrapper1, wrapper2) = wrapper.split(" ")
        wrappeds = wrapped.split(", ")
        wrappeds_details = []
        for wrapped in wrappeds:
            if len(wrapped.split(" ")) == 4:
                (amount, wrapped1, wrapped2, trash) = wrapped.split(" ")
                wrappeds_details.append((wrapped1, wrapped2, amount))
        rules.append(((wrapper1, wrapper2), wrappeds_details))

# print(rules)

contains_shiny_gold = set()
for rule in rules:
    (left, right) = (rule[0], rule[1])
    for potential in right:
        if potential[0] == "shiny" and potential[1] == "gold":
            container = [left[0], left[1]]
            contains_shiny_gold.add(left[0] + " " + left[1])
            break
prev_cnt = 0
cnt = len(contains_shiny_gold)
while prev_cnt != cnt:
    prev_cnt = cnt
    for rule in rules:
        (left, right) = (rule[0], rule[1])
        found = False
        for potential in right:
            for look_for in contains_shiny_gold:
                if potential[0] + " " + potential[1] == look_for:
                    container = left[0] + " " + left[1]
                    contains_shiny_gold.add(container)
                    found = True
                    break
            if found:
                break
    cnt = len(contains_shiny_gold)

print("This many type of bags could explicitly or implicitly contain a shiny gold bag:", cnt)


def count_bags(bag_list):
    count = 0
    print(bag_list)
    for bag in bag_list:
        count += int(bag[2])
        for rule in rules:
            if rule[0][0] == bag[0] and rule[0][1] == bag[1]:
                count += int(bag[2]) * count_bags(rule[1])
                break
    return count


shiny_gold_rule = None
to_explore = []
no_of_bags = 0
for rule in rules:
    if rule[0][0] == "shiny" and rule[0][1] == "gold":
        for pot in rule[1]:
            to_explore.append(pot)
        break

print(to_explore)
print(count_bags(to_explore))

