import numpy as np

IMAGE_SIZE_IN_NO_OF_TILES = 12
# IMAGE_SIZE_IN_NO_OF_TILES = 3
VERY_FIRST_TILE_ID = 1499
# VERY_FIRST_TILE_ID = 1951

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
                color = '1' if char == "#" else '0'
                row.append(color)
            rows.append(row)
new_tiles = np.zeros((10, 10)).astype(str)
for i in range(10):
    for j in range(10):
        new_tiles[9 - j][i] = tiles[VERY_FIRST_TILE_ID][i][j]
tiles[VERY_FIRST_TILE_ID] = new_tiles
# for i in range(10):
#     for j in range(10):
#         new_tiles[9 - i][j] = tiles[VERY_FIRST_TILE_ID][i][j]
# tiles[VERY_FIRST_TILE_ID] = new_tiles

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
    checked_edge_code = 0
    for checked_edge in edges[checked_tile]:
        found = False
        for other_tile in tiles.keys():
            if other_tile != checked_tile:
                matching_edge_code = 0
                for matching_edge in edges[other_tile]:
                    if checked_edge == matching_edge or checked_edge[::-1] == matching_edge:
                        found_edges += 1
                        found = True
                        twisted = not checked_edge == matching_edge
                        # print("Found one:", other_tile, checked_edge, matching_edge)
                        current_neighbors.append((other_tile, checked_edge_code, matching_edge_code, twisted))
                        break
                    matching_edge_code += 1
                if found:
                    break
        if not found:
            current_neighbors.append(0)
        checked_edge_code += 1
    neighbors[checked_tile] = current_neighbors
    if found_edges == 2:
        corner_id_product *= checked_tile
        print(checked_tile)

active_tile = (VERY_FIRST_TILE_ID, 2, 0, False)
tiles_pool = neighbors.copy()
arrangement = []
for i in range(IMAGE_SIZE_IN_NO_OF_TILES):
    # print("##### Setting up line", i + 1)
    arrangement_row = []
    for j in range(IMAGE_SIZE_IN_NO_OF_TILES):
        # print("Setting column", j + 1)
        current_neighbors = tiles_pool.pop(active_tile[0])
        # print(current_neighbors)
        picked_neighbor = None
        for neighbor in current_neighbors:
            if neighbor != 0:
                if j == 0:
                    if (active_tile[2] + 1) % 4 == neighbor[1] or (active_tile[2] - 1) % 4 == neighbor[1]:
                        picked_neighbor = neighbor
                        break
                elif abs(active_tile[2] - neighbor[1]) == 2:
                    picked_neighbor = neighbor
                    break
        # print("Chosen neighbor for", active_tile[0], ":", picked_neighbor)
        # TODO rotate picked neighbor's tile according to direction and twisted info
        arrangement_row.append(active_tile[0])
        active_tile = picked_neighbor
    arrangement.append(arrangement_row)
    for neighbor in neighbors[arrangement_row[0]]:
        # print("Last row base:", neighbors[arrangement_row[0]])
        # print("Checking neighbor for next row start candidate:", neighbor)
        if neighbor != 0:
            if neighbor[0] in tiles_pool.keys():
                # print("Found it!")
                active_tile = neighbor
                # TODO rotate/twist new row's first element's tile
                break
print(arrangement)


