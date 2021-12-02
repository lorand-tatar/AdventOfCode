file_path = 'inputs/day2.txt'

moves = []
with open(file_path, 'r') as file:
    for raw_move in file:
        raw_move.rstrip()
        (direction, amount) = raw_move.split(' ')
        move = (direction[0], int(amount))
        moves.append(move)

# print(moves)
# print(len(moves))

horizontal_move = 0
aim = 0
depth = 0
for move in moves:
    if move[0] == 'f':
        horizontal_move += move[1]
        depth += aim * move[1]
    elif move[0] == 'u':
        aim -= move[1]
    elif move[0] == 'd':
        aim += move[1]

print("Horizontal:", horizontal_move)
print("Achieved aim:", aim)
print("Answer a:", aim * horizontal_move)
print("Final depth:",  depth)
print("Answer b:", depth * horizontal_move)
