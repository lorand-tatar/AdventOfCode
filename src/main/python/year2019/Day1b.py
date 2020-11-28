file_path = 'inputs/day1a_input.txt'

total_fuel_required = 0

with open(file_path, 'r') as file:

    for mass in file:
        intMass = int(mass)
        while intMass // 3 - 2 > 0:
            total_fuel_required += intMass // 3 - 2
            intMass = intMass // 3 - 2

print("ä", total_fuel_required)