import queue

file_path = 'inputs/day22_input.txt'

player1_init = queue.Queue()
player2_init = queue.Queue()
first_half = True
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        if first_half and line != "" and not line.startswith("Player "):
            player1_init.put(int(line))
        elif line == "":
            first_half = False
        elif not line.startswith("Player "):
            player2_init.put(int(line))


def play_game(player1, player2):
    states = []
    while not player1.empty() and not player2.empty():
        # print("##### Decks:", player1.queue, player2.queue)
        # print("States so far:", states)
        current_state = (list(player1.queue), list(player2.queue))
        if current_state in states:
            return [True, list(player1.queue), list(player2.queue)]
        states.append(current_state)
        card1 = player1.get()
        card2 = player2.get()
        # print("Compared cards", card1, card2)
        # print("Size of queues", player1.qsize(), player2.qsize())
        if player1.qsize() >= card1 and player2.qsize() >= card2:
            subplayer1 = queue.Queue()
            subplayer2 = queue.Queue()
            [subplayer1.put(number) for number in list(player1.queue)[:card1]]
            [subplayer2.put(number) for number in list(player2.queue)[:card2]]
            # print("Starting a subgame with ", subplayer1, subplayer2)
            player1_wins = play_game(subplayer1, subplayer2)[0]
        else:
            player1_wins = card1 > card2
        # print("Player 1 won the round" if player1_wins else "Player 2 won the round")
        if player1_wins:
            player1.put(card1)
            player1.put(card2)
        else:
            player2.put(card2)
            player2.put(card1)
    return [player2.empty(), list(player1.queue), list(player2.queue)]


results = play_game(player1_init, player2_init)
player1_won = results[0]
player1_hand = results[1]
player2_hand = results[2]
sum_points = 0
if player1_won:
    print("Player 1 won")
    winner_hand = player1_hand
else:
    print("Player 2 won")
    winner_hand = player2_hand
for i in range(len(winner_hand), 0, -1):
    sum_points += winner_hand[-i] * i

print(sum_points)
