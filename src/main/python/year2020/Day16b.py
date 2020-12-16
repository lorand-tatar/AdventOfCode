import re
import numpy as np
import math

file_path = 'inputs/day16_input.txt'

constraints = []
nearby_tickets_attributes = []
constraint_mapping = {}
with open(file_path, 'r') as file:
    phase = 0
    for line in file:
        line = line.rstrip()
        if phase == 0:
            if line == "":
                phase = 1
            else:
                constraint_matcher = re.search("^([^:]+):\\s(\\d+)-(\\d+)\\sor\\s(\\d+)-(\\d+)$", line)
                constraints.append((int(constraint_matcher.group(2)), int(constraint_matcher.group(3))))
                constraints.append((int(constraint_matcher.group(4)), int(constraint_matcher.group(5))))
                constraint_mapping[constraint_matcher.group(1)] = (int(constraint_matcher.group(2)), int(constraint_matcher.group(3)),
                                                                   int(constraint_matcher.group(4)), int(constraint_matcher.group(5)))
        elif phase == 1:
            if line == "":
                phase = 2
            else:
                if line != "your ticket:":
                    my_values = [int(numstr) for numstr in line.split(",")]
        elif phase == 2:
            if line != "nearby tickets:":
                ticket = [int(numstr) for numstr in line.split(",")]
                nearby_tickets_attributes.append(ticket)

valid_tickets = []
for ticket in nearby_tickets_attributes:
    valid_ticket = True
    for number in ticket:
        valid_number = False
        for constraint in constraints:
            valid_number = valid_number or (constraint[0] <= number <= constraint[1])
            if valid_number:
                break
        if not valid_number:
            valid_ticket = False
            break
    if valid_ticket:
        valid_tickets.append(ticket)

column_mapping = {}
column_no = 1
for column in np.transpose(valid_tickets):
    can_be = set()
    for rule in constraint_mapping.keys():
        valid = True
        for number in column:
            if number < constraint_mapping[rule][0] or constraint_mapping[rule][1] < number < constraint_mapping[rule][2]\
                    or constraint_mapping[rule][3] < number:
                valid = False
                break
        if valid:
            can_be.add(rule)
    column_mapping[column_no] = can_be
    column_no += 1

available_rules = set(constraint_mapping.keys())
final_mapping = {}
for i in range(20):
    for column_number in column_mapping.keys():
        if len(column_mapping[column_number]) == i + 1:
            final_mapping[column_number] = column_mapping[column_number].intersection(available_rules).pop()
            available_rules.remove(final_mapping[column_number])

print(final_mapping)
dep_rules = []
for rule_no in final_mapping.keys():
    if final_mapping[rule_no].startswith("departure"):
        dep_rules.append(rule_no)
print("The product of departure rules on my ticket:", math.prod([my_values[rule_no - 1] for rule_no in dep_rules]))
