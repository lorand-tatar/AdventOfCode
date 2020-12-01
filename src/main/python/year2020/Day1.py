file_path = 'inputs/day1_input.txt'

costs = []
with open(file_path, 'r') as file:
    for cost in file:
        costs.append(int(cost))

product = -1
for first_part in costs:
    for second_part in costs:
        if (first_part != second_part) and (first_part + second_part == 2020):
            product = first_part * second_part
            break
    if product != -1:
        break

product_of_three = -1
for first_third_part in costs:
    for second_third_part in costs:
        for third_third_part in costs:
            if (first_third_part != second_third_part) and (first_third_part != third_third_part) and (second_third_part != third_third_part) \
                    and (first_third_part + second_third_part + third_third_part == 2020):
                product_of_three = first_third_part * second_third_part * third_third_part
                break
        if product_of_three != -1:
            break
    if product_of_three != -1:
        break

print(first_part, "and", second_part, "adds up to 2020, and their product is", product)
print("Three costs that add up to 2020:", first_third_part, second_third_part, third_third_part, "and their product:", product_of_three)
