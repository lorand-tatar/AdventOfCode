file_path = 'inputs/day2.txt'

games_raw = []
with open(file_path, 'r') as file:
    for line in file:
        games_raw.append(line)

games = []
for game_raw in games_raw:
    game = []
    for draw_raw in game_raw.split(':')[1].split(';'):
        draw = {}
        for color_pick in draw_raw.split(','):
            draw.setdefault('red', 0)
            draw.setdefault('green', 0)
            draw.setdefault('blue', 0)
            draw[color_pick.split(' ')[2].rstrip()] = int(color_pick.split(' ')[1])
        game.append(draw)
    games.append(game)

game_id = 1
sum_of_valid_game_ids = 0
for game in games:
    check = True
    for draw in game:
        check = check and (draw['red'] <= 12) and (draw['green'] <= 13) and (draw['blue'] <= 14)
        # print("Checked draw", draw, "resulted in", check)
    # print("Checked for game", game_id, ":", check)
    if check:
        sum_of_valid_game_ids += game_id
    game_id += 1

print("Sum of game IDs that have a valid max number of cubes", sum_of_valid_game_ids)

sum_of_game_powers = 0
for game in games:
    minimums = {'red': 0, 'green': 0, 'blue': 0}
    for draw in game:
        for color in draw.keys():
            if draw[color] > minimums[color]:
                minimums[color] = draw[color]
    sum_of_game_powers += (minimums['red'] * minimums['green'] * minimums['blue'])

print("Sum of all minimal cube set powers:", sum_of_game_powers)
