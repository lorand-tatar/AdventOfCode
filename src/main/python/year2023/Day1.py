file_path = 'inputs/day1.txt'

parameters = []
with open(file_path, 'r') as file:
    for parameter_line in file:
        parameters.append(parameter_line)

valid_digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = []
for parameter in parameters:
    number_row = []
    char_index = 0
    for char in parameter:
        if char.isdigit():
            number_row.append(int(char))
        else:
            for numberword in valid_digit_strings:
                if parameter[char_index:].startswith(numberword):
                    # print("Added", valid_digit_strings.index(numberword) + 1)
                    number_row.append(valid_digit_strings.index(numberword) + 1)
        char_index += 1
    # print("\n")
    if len(number_row) != 0:
        numbers.append(number_row)

double_digit_params = []
for number_block in numbers:
    double_digit_params.append(number_block[0] * 10 + number_block[-1])

print("Sum of all parameters:", sum(double_digit_params))
