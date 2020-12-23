import numpy as np

file_path = 'inputs/day20_input.txt'

tiles = {}
rows = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.rstrip()
        if line.startswith("Tile"):
            line = line.lstrip("Tile ").rstrip(":")
            id = int(line)
        elif line == "":
            tiles[id] = rows
            rows = []
        else:
            row = []
            for char in line:
                paint = '1' if char == "#" else '0'
                row.append(paint)
            rows.append(row)

edges = {}
for tile in tiles.keys():
    binary = ""
    sides = []
    for bit in tiles[tile][0]:
        binary = binary + bit
    sides.append(binary)
    binary = ""
    for bit in [row[-1] for row in tiles[tile]]:
        binary = binary + bit
    sides.append(binary)
    binary = ""
    for bit in tiles[tile][-1]:
        binary = binary + bit
    sides.append(binary)
    binary = ""
    for bit in [row[0] for row in tiles[tile]]:
        binary = binary + bit
    sides.append(binary)
    edges[tile] = sides

corner_id_product = 1
neighbors = {}
for checked_tile in tiles.keys():
    found_edges = 0
    current_neighbors = []
    for checked_edge in edges[checked_tile]:
        found = False
        for other_tile in tiles.keys():
            if other_tile != checked_tile:
                for matching_edge in edges[other_tile]:
                    if checked_edge == matching_edge or checked_edge[::-1] == matching_edge:
                        found_edges += 1
                        found = True
                        # print("Found one:", other_tile, checked_edge, matching_edge)
                        current_neighbors.append(other_tile)
                        break
                if found:
                    break
        if not found:
            current_neighbors.append(0)
    neighbors[checked_tile] = current_neighbors
    if found_edges == 2:
        corner_id_product *= checked_tile

tile_x = 1499
tile_y = 1499
i = 0
j = 0
image = np.zeros((96, 96)).astype(int)
while i < 96 and j < 96:
    current_tile = tiles[tile_x][1:-2][1:-2]
    inner_x = i % 8
    inner_y = j % 8
    image[i][j] =
    i += 1
    j += 1

