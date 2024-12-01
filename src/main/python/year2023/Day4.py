import numpy as np

file_path = 'inputs/day4.txt'

games_raw = []
with open(file_path, 'r') as file:
    for line in file:
        games_raw.append(line.rstrip().split(':')[1].split("|"))

for game_raw in games_raw:
    game_raw[0] = game_raw[0].strip().split()
    game_raw[1] = game_raw[1].lstrip().split()
    x = 0
    y = 0
    for entries in game_raw:
        for number in entries:
            game_raw[y][x] = int(number)
            x += 1
        y += 1
        x = 0

# print(games_raw[:10])

matches = []
for game in games_raw:
    match_cnt = 0
    for mine in game[1]:
        if mine in game[0]:
            match_cnt += 1
    matches.append(match_cnt)


# print(matches, len(matches))

sum_points = 0
for match in matches:
    if match != 0:
        sum_points += (2 ** (match - 1))

print("Sum of won points:", sum_points)

game_card_counts = np.ones(len(matches))
i = 0
for game_card in matches:
    for j in range(i + 1, i + game_card + 1):
        game_card_counts[j] += game_card_counts[i]
    i += 1

print("Number of cards we end up with:", sum(game_card_counts))
