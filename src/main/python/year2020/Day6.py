import re

input_file_path = 'inputs/day6_input.txt'

groups = []
forms = []
with open(input_file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        matcher = re.search("^(\\w*)$", line)
        if matcher.group(1) != "":
            forms.append(line)
        else:
            groups.append(forms)
            forms = []
    groups.append(forms)

all_yes = 0
for group in groups:
    letters = set()
    for form in group:
        for letter in form:
            letters.add(letter)
    print(letters)
    all_yes += len(letters)

print("Sum of all yes answers:", all_yes)

all_common_yes = 0
for group in groups:
    common_letters = set()
    for initial_letter in group[0]:
        common_letters.add(initial_letter)
    for form in group:
        own_letters = set()
        for letter in form:
            own_letters.add(letter)
        common_letters = common_letters.intersection(own_letters)
    all_common_yes += len(common_letters)

print("Sum of common yes per group:", all_common_yes)
