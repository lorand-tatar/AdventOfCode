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
                        twisted = not (checked_edge == matching_edge)
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
        # print(checked_tile)


def tweak_tile(tile, right_rotation_cnt, twist, row_starter, tile_width=10):
    # print("For tile", tile, "Right rotation ordered:", right_rotation_cnt, "Twist", twist, "Row starter", row_starer)
    # 0/4 rotation: don't rotate
    # 1 rotation: 90 degrees right
    # 2 rotation: 180 degrees
    # 3 rotation: 270 degrees right (90 degrees left)
    # if row starter, twist means vertical flip; else horizontal flip
    tweaked_tile = np.zeros((tile_width, tile_width)).astype(str)
    for i in range(tile_width):
        for j in range(tile_width):
            x = i
            y = j
            if right_rotation_cnt == 1:
                x = j
                y = tile_width - 1 - i
            elif right_rotation_cnt == 2:
                x = tile_width - 1 - i
                y = tile_width - 1 - j
            elif right_rotation_cnt == 3:
                x = tile_width - 1 - j
                y = i
            if twist and row_starter:
                y = tile_width - 1 - y
            elif twist:
                x = tile_width - 1 - x
            tweaked_tile[x][y] = tile[i][j]
    return tweaked_tile


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
                break

i = 0
for row in arrangement:
    j = 0
    for tile_id in row:
        # print("Tile", i, j)
        current_tile = tiles[tile_id].copy()
        if j == 0 and tile_id != VERY_FIRST_TILE_ID:
            while ([k for k in tiles[arrangement[i - 1][0]][-1]] != [k for k in current_tile[0]]) and ([k for k in tiles[arrangement[i - 1][0]][-1][::-1]] != [k for k in current_tile[0]]):
                # print("Rotating once")
                current_tile = tweak_tile(current_tile, 1, False, True)
            if [k for k in tiles[arrangement[i - 1][0]][-1]] != [k for k in current_tile[0]]:
                # print("Need to flip")
                current_tile = tweak_tile(current_tile, 0, True, True)
        elif j != 0:
            while ([row[-1] for row in tiles[arrangement[i][j - 1]]] != [row[0] for row in current_tile]) and ([row[-1] for row in tiles[arrangement[i][j - 1]]][::-1] != [row[0] for row in current_tile]):
                # print("Rotating once")
                current_tile = tweak_tile(current_tile, 1, False, False)
            if [row[-1] for row in tiles[arrangement[i][j - 1]]] != [row[0] for row in current_tile]:
                # print("Need to flip")
                current_tile = tweak_tile(current_tile, 0, True, False)
        tiles[tile_id] = current_tile
        j += 1
    i += 1

for tile_id in tiles.keys():
    tile = tiles[tile_id]
    new_tile = []
    tile = tile[1:9]
    for row in tile:
        new_tile.append(row[1:9])
    tiles[tile_id] = new_tile

image = np.zeros((8 * IMAGE_SIZE_IN_NO_OF_TILES, 8 * IMAGE_SIZE_IN_NO_OF_TILES)).astype(int)
i = 0
j = 0
saved_i = 0
saved_j = 0
stuff_cnt = 0
for row in arrangement:
    for tile_id in row:
        i = saved_i
        for tile_row in tiles[tile_id]:
            j = saved_j
            for pixel in tile_row:
                if int(pixel) == 1:
                    stuff_cnt += 1
                image[i][j] = int(pixel)
                j += 1
            i += 1
        saved_j = j
    saved_i = i
    saved_j = 0

with open("output/radar_image.txt", 'w', encoding="utf-8") as out_file:
    # Transposed game matrix as array handling made the x and y exchanged
    for row in image:
        for element in row:
            if element == 0:
                pixel = '.'
            if element == 1:
                pixel = '#'
            out_file.write(pixel)
        out_file.write('\n')

print(arrangement)
# print()
# for row in arrangement:
#     for tile_id in row:
#         for tile_row in tiles[tile_id]:
#             print(tile_row)
#         print()
#     print("========== NEW ROW =====================================")

with open('inputs/day20b_monster.txt', 'r') as monster_file:
    monster_pattern = []
    for line in monster_file:
        line = line.rstrip()
        row = []
        for char in line:
            if char == '#':
                row.append(1)
            else:
                row.append(0)
        monster_pattern.append(row)

monster_count = 0
rotation_cnt = 0
while monster_count == 0:
    # print(rotation_cnt, "tweaks so far")
    for i in range(8 * IMAGE_SIZE_IN_NO_OF_TILES - 2):
        for j in range(8 * IMAGE_SIZE_IN_NO_OF_TILES - 19):
            monster_found = True
            rolling_i = i
            while rolling_i < i + 3:
                rolling_j = j
                while rolling_j < j + 20:
                    monster_found = monster_found and ((int(image[rolling_i][rolling_j]) == 1) or (monster_pattern[rolling_i - i][rolling_j - j] == 0))
                    rolling_j += 1
                rolling_i += 1
            if monster_found:
                monster_count += 1
    if monster_count == 0 and rotation_cnt < 3:
        image = tweak_tile(image, 1, False, False, 8 * IMAGE_SIZE_IN_NO_OF_TILES)
        rotation_cnt += 1
    elif monster_count == 0:
        if rotation_cnt != 3:
            image = tweak_tile(image, 0, True, False, 8 * IMAGE_SIZE_IN_NO_OF_TILES)
        image = tweak_tile(image, 1, True, False, 8 * IMAGE_SIZE_IN_NO_OF_TILES)
        rotation_cnt += 1

print("This many monsters in the water:", monster_count)
print("Water thickness without monsters:", stuff_cnt - monster_count * 15)
