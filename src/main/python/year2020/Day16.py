import re

file_path = 'inputs/day16_input.txt'

constraints = []
nearby_tickets_attributes = []
with open(file_path, 'r') as file:
    phase = 0
    for line in file:
        line = line.rstrip()
        if phase == 0:
            if line == "":
                phase = 1
            else:
                constraint_matcher = re.search("^[^:]+:\\s(\\d+)-(\\d+)\\sor\\s(\\d+)-(\\d+)$", line)
                constraints.append((int(constraint_matcher.group(1)), int(constraint_matcher.group(2))))
                constraints.append((int(constraint_matcher.group(3)), int(constraint_matcher.group(4))))
        elif phase == 1:
            if line == "":
                phase = 2
        elif phase == 2:
            if line != "nearby tickets:":
                ticket = [int(numstr) for numstr in line.split(",")]
                nearby_tickets_attributes.append(ticket)

invalid_sum = 0
valid_tickets = []
for ticket in nearby_tickets_attributes:
    valid_ticket = True
    for number in ticket:
        valid_number = False
        for constraint in constraints:
            valid_number = valid_number or (constraint[0] <= number <= constraint[1])
        if not valid_number:
            invalid_sum += number

print("Sum of all invalid numbers on all tickets:", invalid_sum)
