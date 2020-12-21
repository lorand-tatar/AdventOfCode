import re

file_path = 'inputs/day19_input.txt'

rule_mapping = {}
data = []
with open(file_path, 'r') as file:
    rules_phase = True
    for line in file:
        line = line.rstrip()
        if rules_phase and line != "":
            (rule_id, rule) = line.split(": ")
            subrules = rule.split(" | ")
            if subrules[0].startswith("\""):
                subrule = subrules[0].strip("\"")
                subrules = [subrule]
            rule_mapping[rule_id] = subrules
        elif line == "":
            rules_phase = False
        else:
            data.append(line)


def assemble_regex(rule):
    if rule[0] == 'a' or rule[0] == 'b':
        return rule[0]
    if len(rule) == 1:
        subregex = ""
        for rule_to_concatenate in rule[0].split(' '):
            subregex = subregex + assemble_regex(rule_mapping[rule_to_concatenate])
        return subregex
    else:
        subregex = "("
        for subrule in rule:
            for subsubrule in subrule.split(" "):
                subregex = subregex + assemble_regex(rule_mapping[subsubrule])
            subregex = subregex + '|'
        return subregex.rstrip("|") + ')'


regex_31 = assemble_regex(rule_mapping['31'])
regex_42 = assemble_regex(rule_mapping['42'])
regex = "^(" + regex_42 + "){1}(?P<corresp42>(" + regex_42 + ")+)(?P<group31s>(" + regex_31 + ")+)$"

valid_messages_amount = 0
for message in data:
    matcher = re.search(regex, message)
    if matcher is not None:
        print(len(message))
        size_of_31 = len(matcher.group("group31s")) // 8
        print("Number_of_31s", size_of_31)
        size_of_42 = len(matcher.group("corresp42")) // 8
        print("Number of 42s before it", size_of_42)
        if size_of_42 >= size_of_31:
            valid_messages_amount += 1
print("We have", valid_messages_amount, "valid messages.")

