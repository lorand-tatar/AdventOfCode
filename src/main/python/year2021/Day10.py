file_path = 'inputs/day10.txt'

expressions = []
with open(file_path, 'r') as file:
    for line in file:
        expressions.append(line.rstrip())

syntax_error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
sum_score = 0
valid_expressions_closings = []
for expression in expressions:
    expectation_stack = []
    valid = True
    for character in expression:
        if character == '{':
            expectation_stack.append('}')
        elif character == '[':
            expectation_stack.append(']')
        elif character == '(':
            expectation_stack.append(')')
        elif character == '<':
            expectation_stack.append('>')
        else:
            if expectation_stack.pop() != character:
                sum_score += syntax_error_scores[character]
                valid = False
                break
    if valid:
        expectation_stack.reverse()
        valid_expressions_closings.append(expectation_stack)
print("Sum syntax error scores:", sum_score)
# print(valid_expressions_closings)

closing_scores = []
closing_score_by_char = {')': 1, ']': 2, '}': 3, '>': 4}
for closing in valid_expressions_closings:
    closing_score = 0
    for character in closing:
        closing_score *= 5
        closing_score += closing_score_by_char[character]
    closing_scores.append(closing_score)
closing_scores.sort()
# print(closing_scores)
print("Middle closing score value:", closing_scores[len(closing_scores) // 2])
