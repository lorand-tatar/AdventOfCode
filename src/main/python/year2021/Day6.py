file_path = 'inputs/day6.txt'

fish_ages_string = []
with open(file_path, 'r') as file:
    fish_ages_string = file.readline().rstrip().split(',')
fish_agegroups = 9 * [0]
for fish_age in fish_ages_string:
    fish_agegroups[int(fish_age) % 7] += 1
# print(fish_agegroups)

days_of_simulation = 256
for day in range(days_of_simulation):
    breeding = fish_agegroups[0]
    for i in range(8):
        fish_agegroups[i] = fish_agegroups[i + 1]
    fish_agegroups[6] += breeding
    fish_agegroups[8] = breeding


    # print("\nEnding fishes:", fish_ages)

print("We have", sum(fish_agegroups), "fish after", days_of_simulation, "days")
