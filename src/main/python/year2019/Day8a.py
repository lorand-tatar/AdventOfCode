import numpy as np

file_path = 'inputs/day8_input.txt'

with open(file_path, 'r') as file:
    sequence = file.readline()

picture = np.zeros((100, 6, 25))
for layer in range(100):
    for row in range(6):
        for column in range(25):
            picture[layer][row][column] = sequence[150 * layer + 25 * row + column]
#print(picture)

min_zeros = 150
layer_with_min_zeros = -1
layerindex = 0
for layer in picture:
    nonzeros = np.count_nonzero(layer)
    if 150 - nonzeros < min_zeros:
        min_zeros = 150 - nonzeros
        layer_with_min_zeros = layerindex
        min_zeros_count_of_nonzeros = nonzeros
        ones_count = np.count_nonzero(layer == 1)
        twos_count = np.count_nonzero(layer == 2)
    layerindex += 1
print("Max filled layer index", layer_with_min_zeros, "with this many nonzeros:", min_zeros_count_of_nonzeros)

print(ones_count * twos_count)
