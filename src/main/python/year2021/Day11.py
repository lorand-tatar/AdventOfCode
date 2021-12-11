file_path = 'inputs/day11.txt'

octopuses = []
with open(file_path, 'r') as file:
    for line in file:
        octopus_line = []
        for energy in line.rstrip():
            octopus_line.append(int(energy))
        octopuses.append(octopus_line)


# print(octopuses)


def simulate(orig_octopuses, no_of_rounds, sync_check):
    octopuses_copy = []
    for line in orig_octopuses:
        new_line = []
        for octopus in line:
            new_line.append(octopus)
        octopuses_copy.append(new_line)
    all_illuminations = 0
    round_no = 0
    sync_found = False
    while round_no < no_of_rounds or (sync_check and not sync_found):
        # print("############# Round", round_no + 1)
        to_check = []
        j = 0
        for octopus_line in octopuses_copy:
            i = 0
            for octopus in octopus_line:
                octopus += 1
                octopus %= 10
                octopuses_copy[j][i] = octopus
                if octopus == 0:
                    to_check.append((i, j))
                i += 1
            j += 1
        # print("All octopus values increased by 1")
        # print(octopuses_copy)
        # print("First set of octopuses to illuminate:")
        # print(to_check)

        done = []
        while len(to_check) != 0:
            next_checked = to_check.pop()
            # print("Checking", next_checked)
            for neighbor_x in range(next_checked[0] - 1, next_checked[0] + 2):
                for neighbor_y in range(next_checked[1] - 1, next_checked[1] + 2):
                    if 0 <= neighbor_x < 10 and 0 <= neighbor_y < 10 and (neighbor_x != next_checked[0] or neighbor_y != next_checked[1]) and (neighbor_x, neighbor_y) not in done and (neighbor_x, neighbor_y) not in to_check:
                        # print(neighbor_x, neighbor_y, "is a valid neighbor!")
                        octopuses_copy[neighbor_y][neighbor_x] += 1
                        octopuses_copy[neighbor_y][neighbor_x] %= 10
                        if octopuses_copy[neighbor_y][neighbor_x] == 0:
                            to_check.append((neighbor_x, neighbor_y))
            done.append((next_checked[0], next_checked[1]))
            # print("Left to be checked:")
            # print(to_check)
            # print("We are done with:")
            # print(done)
        illuminations_this_round = 0
        for octopus_line in octopuses_copy:
            for octopus in octopus_line:
                if octopus == 0:
                    all_illuminations += 1
                    illuminations_this_round += 1
        # print(illuminations_this_round, "illuminations happened this round")
        # if round_no + 1 in {90, 91, 92, 93, 94, 95, 100}:
        #     print("After round", round_no + 1)
        #     for octopus_line in octopuses_copy:
        #         print(octopus_line)
        if illuminations_this_round == 100 and sync_check:
            # print(octopuses_copy)
            return round_no + 1
        round_no += 1
    return all_illuminations


all_illuminations = simulate(octopuses, 100, False)
first_round_of_sync = simulate(octopuses, 0, True)

print("All illuminations after 100 rounds:", all_illuminations)
print("Round number after which the first sync happens:", first_round_of_sync)
