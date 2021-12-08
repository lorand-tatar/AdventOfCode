file_path = 'inputs/day8.txt'

entries = []
with open(file_path, 'r') as file:
    for line in file:
        (ten_digits, output) = line.rstrip().split(" | ")
        digit_samples = ten_digits.split(' ')
        outputs = output.split(' ')
        entries.append([digit_samples, outputs])
# print(entries[0], "\n", entries[1], "\n", entries[2])
# print(len(entries))

count_of_easy_digits = 0
for entry in entries:
    output = entry[1]
    for output_digit in output:
        if len(output_digit) in {2, 4, 3, 7}:
            count_of_easy_digits += 1

print("Count of 1, 4, 7, 8 in the outputs:", count_of_easy_digits)

sum_of_numbers = 0
for entry in entries:
    digit_sample = entry[0]
    output = entry[1]
    stuff_1 = []
    stuff_4 = []
    stuff_7 = []
    length_5 = []
    length_6 = []
    # Collecting numbers' character parts
    for digit in digit_sample:
        if len(digit) == 2:
            stuff_1 = []
            for alpha in digit:
                stuff_1.append(alpha)
        if len(digit) == 4:
            stuff_4 = []
            for alpha in digit:
                stuff_4.append(alpha)
        if len(digit) == 3:
            stuff_7 = []
            for alpha in digit:
                stuff_7.append(alpha)
        if len(digit) == 5:
            collect5 = []
            for alpha in digit:
                collect5.append(alpha)
            length_5.append(collect5)
        if len(digit) == 6:
            collect6 = []
            for alpha in digit:
                collect6.append(alpha)
            length_6.append(collect6)
    segments_to_letters = 10 * ['x']
    remainders_of_4 = []
    # What is not in 1 but is in 7, that's the upside segment
    for letter in stuff_7:
        if letter not in stuff_1:
            segments_to_letters[0] = letter
    # Based on 4 and 1, we can collect upper left and the middle segments
    for letter in stuff_4:
        if letter not in stuff_1:
            remainders_of_4.append(letter)
    # What's not in either 1, 4, or 7 is the lower left and the bottom segments
    lower_left_stuff = []
    for letter in {'a', 'b', 'c', 'd', 'e', 'f', 'g'}:
        if letter not in stuff_1 and letter not in stuff_4 and letter not in stuff_7:
            lower_left_stuff.append(letter)
    # Amongst the 6-segment numbers, only 9 does not use the lower left segment, the bottom segment is always used.
    # So we can determine which one is which
    for six_segment in length_6:
        for to_check in lower_left_stuff:
            if to_check not in six_segment:
                segments_to_letters[4] = to_check
    for other in lower_left_stuff:
        if other != segments_to_letters[4]:
            segments_to_letters[6] = other
    # Out of the two segments of 1, the upper right is not used only by one 6-segment number, 6
    # The bottom right segment is the other segment of 1
    for elements_of_1 in stuff_1:
        for six_segment in length_6:
            if elements_of_1 not in six_segment:
                segments_to_letters[2] = elements_of_1
    for elements_of_1 in stuff_1:
        if elements_of_1 != segments_to_letters[2]:
            segments_to_letters[5] = elements_of_1
    # 4 segments are always used by 6-segment numbers. We already know three out of that four so we can determine the fourth
    # - the upper left segment
    remainder_set_of_6 = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    for six_segment in length_6:
        for segment in {'a', 'b', 'c', 'd', 'e', 'f', 'g'}:
            if segment not in six_segment:
                remainder_set_of_6.remove(segment)
    for remainder in remainder_set_of_6:
        if remainder != segments_to_letters[0] and remainder != segments_to_letters[5] and remainder != segments_to_letters[6]:
            segments_to_letters[1] = remainder
    # The only missing segment is the middle one. Let's check what we haven't used so far
    all_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    for used in {'a', 'b', 'c', 'd', 'e', 'f', 'g'}:
        for determined in segments_to_letters:
            if determined == used:
                all_letters.remove(used)
    segments_to_letters[3] = all_letters.pop()

    # Creating the mapping from (alphabetically ordered) segment lists -> to numbers.
    # Easy digits are determined by length as above, 5 and 6-segment ones are determined based on the letter -> segment mapping we just created
    digit_mapping = {}
    for digit in digit_sample:
        digit = ''.join(sorted(digit))
        if len(digit) == 2:
            digit_mapping[digit] = 1
        if len(digit) == 4:
            digit_mapping[digit] = 4
        if len(digit) == 3:
            digit_mapping[digit] = 7
        if len(digit) == 7:
            digit_mapping[digit] = 8
        if segments_to_letters[0] in digit and segments_to_letters[1] in digit and segments_to_letters[2] in digit and segments_to_letters[3] not in digit and segments_to_letters[4] in digit and segments_to_letters[5] in digit and segments_to_letters[6] in digit:
            digit_mapping[digit] = 0
        if segments_to_letters[0] in digit and segments_to_letters[1] not in digit and segments_to_letters[2] in digit and segments_to_letters[3] in digit and segments_to_letters[4] in digit and segments_to_letters[5] not in digit and segments_to_letters[6] in digit:
            digit_mapping[digit] = 2
        if segments_to_letters[0] in digit and segments_to_letters[1] not in digit and segments_to_letters[2] in digit and segments_to_letters[3] in digit and segments_to_letters[4] not in digit and segments_to_letters[5] in digit and segments_to_letters[6] in digit:
            digit_mapping[digit] = 3
        if segments_to_letters[0] in digit and segments_to_letters[1] in digit and segments_to_letters[2] not in digit and segments_to_letters[3] in digit and segments_to_letters[4] not in digit and segments_to_letters[5] in digit and segments_to_letters[6] in digit:
            digit_mapping[digit] = 5
        if segments_to_letters[0] in digit and segments_to_letters[1] in digit and segments_to_letters[2] not in digit and segments_to_letters[3] in digit and segments_to_letters[4] in digit and segments_to_letters[5] in digit and segments_to_letters[6] in digit:
            digit_mapping[digit] = 6
        if segments_to_letters[0] in digit and segments_to_letters[1] in digit and segments_to_letters[2] in digit and segments_to_letters[3] in digit and segments_to_letters[4] not in digit and segments_to_letters[5] in digit and segments_to_letters[6] in digit:
            digit_mapping[digit] = 9
    i = 1000
    # print(digit_mapping)
    # Interpreting output digits as a 4-digit decimal
    for output_digit in output:
        output_digit = ''.join(sorted(output_digit))
        sum_of_numbers += digit_mapping[output_digit] * i
        i = i // 10

print("Sum of all outputs:", sum_of_numbers)
