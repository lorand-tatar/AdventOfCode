# ROUND_NO = 100
ROUND_NO = 10000000
# CUP_COUNT = 9
CUP_COUNT = 1000000

starter_setup = [int(cup) for cup in "916438275"]
# starter_setup = [int(cup) for cup in "389125467"]


class Cup:
    def __init__(self, id, id_minus_n, prev=None, next=None):
        self.id = id
        self.prev = prev
        self.next = next
        self.id_minus_n = id_minus_n


cups = []
cup1 = None
j = 0
for cup_id in range(1, CUP_COUNT + 1):
    if cup_id == 1:
        cup = Cup(cup_id, [])
    else:
        i = j - 1
        connected_cups = []
        while i != 0 and i > cup_id - 6:
            connected_cups.append(cups[i])
            i -= 1
        cup = Cup(cup_id, connected_cups, cups[j - 1])
    cups.append(cup)
    j += 1
j = 1
for cup in cups:
    if j < CUP_COUNT:
        cup.next = cups[j]
    else:
        cup.next = cups[0]
    j += 1
cups[0].prev = cups[CUP_COUNT - 1]
j = 0
for start_id in starter_setup:
    if start_id == 1:
        cup1 = cups[j]
    cups[j].id = start_id
    cups[j].id_minus_n = []
    j += 1
for cup in cups[:13]:
    if cup.id in range(10, 14):
        cup.id_minus_n = []
    i = cup.id - 2
    while i > cup.id - 6:
        [cup.id_minus_n.append(elem) for elem in cups[:13] if elem.id == (i % CUP_COUNT + 1)]
        i -= 1
    if cup.id <= 4:
        cup.id_minus_n.append(cups[CUP_COUNT - 1])
    # [cup.id_minus_n.append(i) for i in cups if i.id == cup.id - 1]
    if cup.id <= 3:
        cup.id_minus_n.append(cups[CUP_COUNT - 2])
    # [cup.id_minus_n.append(i) for i in cups if i.id == cup.id - 2]
    if cup.id <= 2:
        cup.id_minus_n.append(cups[CUP_COUNT - 3])
    # [cup.id_minus_n.append(i) for i in cups if i.id == cup.id - 3]
    if cup.id == 1:
        cup.id_minus_n.append(cups[CUP_COUNT - 4])
    # [cup.id_minus_n.append(i) for i in cups if i.id == cup.id - 4]

[print("id=", cup.id, "next=", cup.next.id if cup.next is not None else None, "prev=", cup.prev.id if cup.prev is not None else None,
       "objects with lesser ids=", [meh.id for meh in cup.id_minus_n]) for cup in cups if (cup.id < 20)]
print(cups[CUP_COUNT - 1].id, cups[CUP_COUNT - 1].prev.id, cups[CUP_COUNT - 1].next.id, [meh.id for meh in cups[CUP_COUNT - 1].id_minus_n])

cup_round = 0
current_cup = None
while cup_round < ROUND_NO:
    # print("##### Start", time.process_time())
    current_cup = current_cup.next if current_cup is not None else cups[0]
    picked_cups = [current_cup.next, current_cup.next.next, current_cup.next.next.next]
    current_cup.next = current_cup.next.next.next.next
    current_cup.next.prev = current_cup
    # print("After pop out", time.process_time())
    destination_cup = current_cup.id_minus_n[0]
    i = 0
    while destination_cup in picked_cups:
        i += 1
        destination_cup = current_cup.id_minus_n[i]
    # print("After destination calc", time.process_time())
    # print("Destination cup is", destination_cup)
    dest_next = destination_cup.next
    destination_cup.next = picked_cups[0]
    picked_cups[0].prev = destination_cup
    picked_cups[2].next = dest_next
    picked_cups[2].next.prev = picked_cups[2]
    # print("After inserting 3", time.process_time())
    cup_round += 1
    # if cup_round < 11 or cup_round > 90 or True:
        # print("\nAfter round", cup_round)
        # running_cup = cup1.next
        # print(cup1.id, end=" ")
        # while running_cup != cup1:
            # print(running_cup.id, end=" ")
            # print("id=", running_cup.id, "next=", running_cup.next.id if running_cup.next is not None else None, "prev=",
            #       running_cup.prev.id if running_cup.prev is not None else None,
            #       "objects with lesser ids=", [meh.id for meh in running_cup.id_minus_n])
            # running_cup = running_cup.next

# print("\nFinal")
# running_cup = cup1.next
# while running_cup != cup1:
#     print("id=", running_cup.id, "next=", running_cup.next.id if running_cup.next is not None else None, "prev=",
#           running_cup.prev.id if running_cup.prev is not None else None,
#           "objects with lesser ids=", [meh.id for meh in running_cup.id_minus_n])
#     running_cup = running_cup.next
[print("id=", cup.id, "next=", cup.next.id if cup.next is not None else None, "prev=", cup.prev.id if cup.prev is not None else None,
       "objects with lesser ids=", [meh.id for meh in cup.id_minus_n]) for cup in cups if (cup.id == 1)]
print("Coin hideouts:", cup1.next.id, cup1.next.next.id, "product:", cup1.next.id * cup1.next.next.id)
