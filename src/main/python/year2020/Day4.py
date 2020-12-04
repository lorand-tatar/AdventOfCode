import re

file_path = 'inputs/day4_input.txt'

OBLIGATORY_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

cards = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        data = line.split(' ')
        cards.append(data)

no_of_valid = 0
for card in cards:
    valid = True
    for field in OBLIGATORY_FIELDS:
        found = False
        for data in card:
            matcher = re.search(field, data)
            if matcher is not None:
                found = True
                break
        if not found:
            valid = False
            break
    if valid:
        no_of_valid += 1

print("Number of valid cards:", no_of_valid)
