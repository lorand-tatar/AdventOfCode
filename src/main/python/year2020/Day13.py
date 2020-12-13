import math

target_departure = 1000053
available_buses = [19, 37, 523, 13, 23, 29, 547, 41, 17]
full_input = [19, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 37, 1, 1, 1, 1, 1, 523, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 23,
              1, 1, 1, 1, 1, 29, 1, 547, 1, 1, 1, 1, 1, 1, 1, 1, 1, 41, 1, 1, 1, 1, 1, 1, 17]
# target_departure = 939
# available_buses = [7, 13, 59, 31, 19]

next_departs = [(bus, int(((target_departure // bus + 1) * bus))) for bus in available_buses]
bus_n_wait_minutes = [(next_depart[0], next_depart[1] - target_departure) for next_depart in next_departs]
minutes = [elem[1] for elem in bus_n_wait_minutes]
minimum = min(minutes)
print("Product", [bus[0] * bus[1] for bus in bus_n_wait_minutes if bus[1] == minimum][0])
print("=====================================")

# The buses arrival interval should get an integer product after # of minutes that matches their index in the bus array
numbers_n_required_residues = []
i = 0
for number in full_input:
    if number != 1:
        numbers_n_required_residues.append((number, -i))
    i += 1
print(numbers_n_required_residues)

# Product of all (btw prime) bus IDs
product_of_all = math.prod(number[0] for number in numbers_n_required_residues)
# Product of all but the current bus ID - step 1 for chinese remainder theorem
Mis = [product_of_all // num for num in [number[0] for number in numbers_n_required_residues]]
print(product_of_all, Mis)

# Solving Mi * yi <congruent to> 1 (mod busID) - step 2 for chinese remainder theorem
subsolutions = []
i = 0
for data in numbers_n_required_residues:
    j = 1
    # Finding out which multiple of Mi gives 1 residue for the busID
    while (j * Mis[i] - 1) % data[0] != 0:
        j += 1
    subsolutions.append(j)
    i += 1
# We have got the yi-s
print(subsolutions)

# Calculating the remainder class of the solution (the first one such number will be our output
# as that is the minimum of all solutions) - step 3 of chinese remainder theorem
solutions = []
i = 0
for number in numbers_n_required_residues:
    solutions.append(number[1] * Mis[i] * subsolutions[i])
    i += 1
print(sum(solutions) % product_of_all)
