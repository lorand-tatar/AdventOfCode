import re

file_path = 'inputs/day18_input.txt'

expressions = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip().replace(" ", "")[::-1]
        expressions.append(line)


def evaluate_expression(expr):
    if expr[0] == ')':
        par_balance = 1
        i = 1
        while par_balance != 0:
            if expr[i] == ')':
                par_balance += 1
            elif expr[i] == '(':
                par_balance -= 1
            i += 1
        if i == len(expr):
            # print("Calculating", expr[1:i - 1])
            return evaluate_expression(expr[1:i - 1])
        if expr[i] == '*':
            # print("Calculating", expr[1:i - 1], "and", expr[i + 1:])
            return evaluate_expression(expr[1:i - 1]) * evaluate_expression(expr[i + 1:])
        elif expr[i] == '+':
            # print("Calculating", expr[1:i - 1], "and", expr[i + 1:])
            return  evaluate_expression(expr[1:i - 1]) + evaluate_expression(expr[i + 1:])
    else:
        numbermatcher = re.search("^(\\d+)[^d]?", expr)
        number = numbermatcher.group(1)
        numbersize = len(number)
        number = int(number)
        if numbersize == len(expr):
            return number
        if expr[numbersize] == '*':
            # print("Calculating", expr[numbersize + 1:])
            return number * evaluate_expression(expr[numbersize + 1:])
        elif expr[numbersize] == '+':
            # print("Calculating", expr[numbersize + 1:])
            return  number + evaluate_expression(expr[numbersize + 1:])


results = [evaluate_expression(expression) for expression in expressions]
print(sum(results))
