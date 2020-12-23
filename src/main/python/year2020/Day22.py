import queue

file_path = 'inputs/day22_input.txt'

player1 = queue.Queue()
player2 = queue.Queue()
first_half = True
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        if first_half and line != "" and not line.startswith("Player "):
            player1.put(int(line))
        elif line == "":
            first_half = False
        elif not line.startswith("Player "):
            player2.put(int(line))

print(player1.queue, player2.queue)

while not player1.empty() and not player2.empty():
    card1 = player1.get()
    card2 = player2.get()
    if card1 > card2:
        player1.put(card1)
        player1.put(card2)
    else:
        player2.put(card2)
        player2.put(card1)

print(player1.queue, player2.queue)
print([i for i in range(50, 0, -1)])
sum_points = 0
for i in range(50, 0, -1):
    sum_points += player2.get() * i

print(sum_points)
