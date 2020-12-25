import collections
import time

# ROUND_NO = 100
ROUND_NO = 10000000
# CUP_COUNT = 9
CUP_COUNT = 1000000

starter_setup = [int(cup) for cup in "916438275"]

cup_ring = collections.deque(starter_setup, maxlen=CUP_COUNT)
if CUP_COUNT > 9:
    [cup_ring.append(number) for number in range(10, CUP_COUNT + 1)]
    # [print(cup_ring[i], end=' ') for i in range(0, 30)]
    # [print(cup_ring[i], end=' ') for i in range(999990, 1000000)]

cup_round = 0
while cup_round < ROUND_NO:
    print("##### Start", time.process_time())
    current_cup = cup_ring.popleft()
    picked_cups = [cup_ring.popleft(), cup_ring.popleft(), cup_ring.popleft()]
    cup_ring.append(current_cup)
    print("After pop out", time.process_time())
    # print("Picked up 3", cup_ring)
    destination_cup = current_cup - 1 if current_cup in range(2, CUP_COUNT + 1) else CUP_COUNT
    while destination_cup in picked_cups:
        destination_cup = (destination_cup - 1) if destination_cup in range(2, CUP_COUNT + 1) else CUP_COUNT
    print("After destination calc", time.process_time())
    # print("Destination cup is", destination_cup)
    dest_index = cup_ring.index(destination_cup) + 1
    print("After finding destination", time.process_time())
    [cup_ring.insert(dest_index, picked) for picked in picked_cups[::-1]]
    print("After inserting 3", time.process_time())
    # print("Placed the 3", cup_ring)
    # if cup_round % 1000 == 0:
    cup_round += 1

position1 = cup_ring.index(1)
print("Coin hideouts:", cup_ring[(position1 + 1) % CUP_COUNT], cup_ring[(position1 + 2) % CUP_COUNT],
      "product:", cup_ring[(position1 + 1) % CUP_COUNT] * cup_ring[(position1 + 2) % CUP_COUNT])
