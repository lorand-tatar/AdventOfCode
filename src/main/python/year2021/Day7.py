file_path = 'inputs/day7.txt'

crab_positions = []
with open(file_path, 'r') as file:
    crab_positions = file.readline().rstrip().split(',')
no_of_crabs = len(crab_positions)
i = 0
for position in crab_positions:
    crab_positions[i] = int(position)
    i += 1
print(no_of_crabs, max(crab_positions))

crab_positions.sort()
# for i in range(497, 503):
#     print(crab_positions[i], end=', ')

median_position = int(crab_positions[(no_of_crabs + 1) // 2 - 1])
print("The median of crab positions:", median_position)

sum_fuel_cost = 0
for position in crab_positions:
    sum_fuel_cost += abs(int(position) - median_position)

print("Sum fuel cost:", sum_fuel_cost)

position_histogram = (max(crab_positions) + 1) * [0]
for position in crab_positions:
    position_histogram[int(position)] += 1

# weighed_sum = 0
# for i in range(2000):
#     weighed_sum += position_histogram[i] * i
# crab_center = weighed_sum // 2000
# print("Approximate crab center:", crab_center)


for k in range(max(crab_positions) + 1):
    j = 0
    fuel_needed = 0
    for position_crowd in position_histogram:
        if position_crowd != 0:
            distance = abs(j - k)
            fuel_needed += (distance * (distance + 1) / 2) * position_crowd
        j += 1
    if k == 0:
        min_fuel = fuel_needed
    if fuel_needed <= min_fuel:
        min_fuel = fuel_needed
    else:
        break

print("Minimal position", k)
print("Minimal consumption: ", min_fuel)
