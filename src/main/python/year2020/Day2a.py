file_path = 'inputs/day2_input.txt'


def parse_line(line):
    line = line.rstrip()
    (rule, password) = line.split(": ")
    (amounts, character) = rule.split(" ")
    (min, max) = amounts.split("-")
    return (int(min), int(max), character, password)


with open(file_path, 'r') as file:
    no_of_correct_passwords = 0
    for line in file:
        (min_number_of_char, max_number_of_char, char_to_look_for, password) = parse_line(line)
        no_of_found_char = 0
        for char in password:
            if char == char_to_look_for:
                no_of_found_char += 1
        if min_number_of_char <= no_of_found_char <= max_number_of_char:
            no_of_correct_passwords += 1

print("Number of correct passwords:", no_of_correct_passwords)
