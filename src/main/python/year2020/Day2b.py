file_path = 'inputs/day2_input.txt'


def parse_line(line):
    line = line.rstrip()
    (rule, password) = line.split(": ")
    (amounts, character) = rule.split(" ")
    (first_number, second_number) = amounts.split("-")
    return (int(first_number), int(second_number), character, password)


with open(file_path, 'r') as file:
    no_of_correct_passwords = 0
    for line in file:
        (first_position_to_check, second_position_to_check, char_to_look_for, password) = parse_line(line)
        if (password[first_position_to_check - 1] == char_to_look_for) ^ (password[second_position_to_check - 1] == char_to_look_for):
            no_of_correct_passwords += 1

print("Number of correct passwords:", no_of_correct_passwords)
