import re

file_path = 'inputs/day4_input.txt'

OBLIGATORY_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

cards = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        fields = line.split(' ')
        card = []
        for field in fields:
            (key, value) = field.split(':')
            card.append((key, value))
        cards.append(card)


def find_value(card, field_name):
    for field in card:
        if field[0] == field_name:
            return field[1]
    return -1


def validate(field_name, value):
    if field_name == "byr":
        matcher = re.search("^\\d{4}$", value)
        valid = matcher is not None and (1920 <= int(value) <= 2002)
    elif field_name == "iyr":
        matcher = re.search("^\\d{4}$", value)
        valid = matcher is not None and (2010 <= int(value) <= 2020)
    elif field_name == "eyr":
        matcher = re.search("^\\d{4}$", value)
        valid = matcher is not None and (2020 <= int(value) <= 2030)
    elif field_name == "hgt":
        matcher = re.search("^(\\d+)(in|cm)$", value)
        if matcher is not None and matcher.group(2) == "in":
            valid = matcher.group(0) is not None and (59 <= int(matcher.group(1)) <= 76)
        elif matcher is not None and matcher.group(2) == "cm":
            valid = matcher.group(0) is not None and (150 <= int(matcher.group(1)) <= 193)
        else:
            valid = False
    elif field_name == "hcl":
        matcher = re.search("^#[0-9a-f]{6}$", value)
        valid = matcher is not None
    elif field_name == "ecl":
        matcher = re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", value)
        valid = matcher is not None
    elif field_name == "pid":
        matcher = re.search("^[0-9]{9}$", value)
        valid = matcher is not None
    else:
        print("Ooops, unknown field name")
        exit(-1)
    return valid


no_of_valid = 0
for card in cards:
    valid = True
    for field in OBLIGATORY_FIELDS:
        found = False
        for data in card:
            if field == data[0]:
                found = True
                break
        if not found:
            valid = False
            break
    if valid:
        values_ok = True
        for field_name in OBLIGATORY_FIELDS:
            value = find_value(card, field_name)
            values_ok = values_ok and validate(field_name, value)
        if values_ok:
            no_of_valid += 1

print("Number of valid cards:", no_of_valid)
