import numpy as np

file_path = 'inputs/day8a_input.txt'

with open(file_path, 'r') as file:
    sequence = file.readline()

picture = np.zeros((100, 6, 25))
for layer in range(100):
    for row in range(6):
        for column in range(25):
            picture[layer][row][column] = sequence[150 * layer + 25 * row + column]

convoluted_picture = np.empty((6, 25))
convoluted_picture.fill(-1)
# print(convoluted_picture)
for layer in picture:
    rowno = 0
    for row in layer:
        columno = 0
        for pixel in row:
            if pixel != 2 and convoluted_picture[rowno][columno] == -1:
                convoluted_picture[rowno][columno] = pixel
            columno += 1
        rowno += 1

print(convoluted_picture)
