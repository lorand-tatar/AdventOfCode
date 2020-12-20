import re

file_path = 'inputs/day18_input.txt'

expressions = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip().replace(" ", "")
        expressions.append(line)


def evaluate_expression(expr):
    i = 0
    flattened_expression = []
    while i < len(expr):
        number_matcher = re.search("^(\\d+)[^\\d]?.*", expr[i:])
        if expr[i] == '(':
            start = i + 1
            par_balance = 1
            while par_balance != 0:
                i += 1
                if expr[i] == '(':
                    par_balance += 1
                elif expr[i] == ')':
                    par_balance -= 1
            # print("Evaling", expr[start:i])
            this_number = evaluate_expression(expr[start:i])
            i += 1
        elif number_matcher is not None:
            number_string = number_matcher.group(1)
            number_length = len(number_string)
            this_number = int(number_string)
            i += number_length
        elif expr[i] == '+' or expr[i] == '*':
            flattened_expression.append(this_number)
            flattened_expression.append(expr[i])
            i += 1
    flattened_expression.append(this_number)
    # print("Flattened:", flattened_expression)
    factors = []
    sum = 0
    for element in flattened_expression:
        if type(element) == int:
            sum += element
        elif element == '*':
            factors.append(sum)
            sum = 0
    if sum != 0:
        factors.append(sum)
    # print("Factors:", factors)
    prod = 1
    for factor in factors:
        prod *= factor
    return int(prod)


# results = [evaluate_expression(expression) for expression in updated_expression]
# print(sum(results))
print(sum([evaluate_expression(expression) for expression in expressions]))
