input = [0, 12, 6, 13, 20, 1, 17]

last_spoken = {0: 1, 12: 2, 6: 3, 13: 4, 20: 5, 1: 6}
last_number = 17
current_turn = 8
while current_turn < 30000001:
    if last_number not in last_spoken.keys():
        last_spoken[last_number] = current_turn - 1
        last_number = 0
    else:
        new_number = current_turn - 1 - last_spoken[last_number]
        last_spoken[last_number] = current_turn - 1
        last_number = new_number
    current_turn += 1

print("Last number to speak:", last_number)
