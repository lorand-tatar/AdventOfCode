from numpy.matlib import zeros

file_path = 'inputs/day1.txt'

columns = []
first = []
second = []
with open(file_path, 'r') as file:
    for number_line in file:
        (f, s) = number_line.split("   ")
        first.append(int(f))
        second.append(int(s))

first.sort()
second.sort()

sum_of_diffs = 0
for ordinal in range(len(first)):
    diff = abs(first[ordinal] - second[ordinal])
    sum_of_diffs += diff

print("Sum of all differences:", sum_of_diffs)

second_histogram = {}
for number in second:
    if number not in second_histogram.keys():
        second_histogram[number] = 1
    else:
        second_histogram[number] += 1

sum_of_similarities = 0
for number in first:
    if number in second_histogram.keys():
        sum_of_similarities += number * second_histogram[number]

print("Similarity points:", sum_of_similarities)
