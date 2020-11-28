file_path = 'inputs/day1a_input.txt'

with open(file_path, 'r') as file:
    total_fuel_required = 0
    for mass in file:
        fuel_required = int(mass) // 3 - 2
        total_fuel_required += fuel_required

print("Ennyi köll össz:", total_fuel_required)