file_path = 'inputs/day9_input.txt'

numbers = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        numbers.append(int(line))

i = 0
addition_succeded = True
while addition_succeded:
    found = False
    for first in numbers[i:i + 25]:
        for second in numbers[i:i + 25]:
            if first != second:
                if first + second == numbers[i + 25]:
                    found = True
                    break
        if found:
            break
    if not found:
        addition_succeded = False
    i += 1

print("First not addable number:", numbers[i + 24])
faulty_target_number = numbers[i + 24]

sum = 0
i = 0
while sum != faulty_target_number:
    sum = 0
    if numbers[i] != faulty_target_number:
        j = i
        while sum < faulty_target_number:
            sum += numbers[j]
            j += 1
    i += 1

print("first index:", i - 1, "last index:", j - 1, "min:", min(numbers[i - 1:j]), "max:", max(numbers[i - 1:j]))
print("Sum of min, max:", min(numbers[i - 1:j]) + max(numbers[i - 1:j]))
