file_path = 'inputs/day3.txt'

binary_inputs = []
with open(file_path, 'r') as file:
    for binary in file:
        binary_inputs.append(binary.rstrip())

no_of_inputs = len(binary_inputs)
turning_point = no_of_inputs / 2
width_of_input = len(binary_inputs[0])
print("All binaries count:", no_of_inputs, "\nTurning point", turning_point)

gamma_collector = [0] * width_of_input
# print("Gamma collector initially", gamma_collector)
for binary in binary_inputs:
    digit_cnt = 0
    for digit in binary:
        if digit == '1':
            gamma_collector[digit_cnt] += 1
        digit_cnt += 1
# print("Collected one digits:", gamma_collector)

gamma = ""
epsilon = ""
for gamma_counter in gamma_collector:
    if gamma_counter > turning_point:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
# print("Gamma, epsilon:", gamma, epsilon)
gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)
print("The product is", gamma * epsilon)


def eliminate_by_bit_criteria(candidates, checking_oxygen):
    checked_bit = 0
    global ones
    while len(candidates) > 1:
        # print("####### Comparing bit number", checked_bit)
        actual_no_of_candidates = len(candidates)
        # print("Number of candidates so far", actual_no_of_candidates)
        ones = 0
        for candidate in candidates:
            if candidate[checked_bit] == '1':
                ones += 1
        ones_won = ones > actual_no_of_candidates / 2
        zeros_won = ones < actual_no_of_candidates / 2
        # print(ones, "ones found,", "ones won" if ones_won else "zeros won")
        filtered_candidates = []
        for candidate in candidates:
            bit_value = candidate[checked_bit]
            if filtering_predicate(bit_value, ones_won, zeros_won, checking_oxygen):
                filtered_candidates.append(candidate)
        candidates = filtered_candidates
        # print("Now all remaining candidates should have", "1" if ones_won else "0", "in bit position", checked_bit)
        # print(candidates)
        checked_bit += 1
    return candidates[0]


def filtering_predicate(bit_value, ones_won, zeros_won, checking_oxygen):
    tie = not ones_won and not zeros_won
    if checking_oxygen:
        return ((ones_won or tie) and bit_value == '1') or (zeros_won and bit_value == '0')
    else:
        return ((ones_won or tie) and bit_value == '0') or (zeros_won and bit_value == '1')


candidates = binary_inputs
oxygen_indicator = int(eliminate_by_bit_criteria(candidates, True), base=2)
candidates = binary_inputs
co2_indicator = int(eliminate_by_bit_criteria(candidates, False), base=2)
print("Oxygen binary, co2 binary", oxygen_indicator, co2_indicator)
print("Health product", oxygen_indicator * co2_indicator)
