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
        print(checked_tile)


def tweak_tile(id, right_rotation_cnt, twist, row_starter):
    # print("For tile", id, "Right rotation ordered:", right_rotation_cnt, "Twist", twist, "First", row_starter)
    # 0/4 rotation: don't rotate
    # 1 rotation: 90 degrees right
    # 2 rotation: 180 degrees
    # 3 rotation: 270 degrees right (90 degrees left)
    # if row starter, twist means vertical flip; else horizontal flip
    tweaked_tile = np.zeros((10, 10)).astype(str)
    for i in range(10):
        for j in range(10):
            x = i
            y = j
            if right_rotation_cnt == 1:
                x = j
                y = 9 - i
            elif right_rotation_cnt == 2:
                x = 9 - i
                y = 9 - j
            elif right_rotation_cnt == 3:
                x = 9 - j
                y = i
            should_flip = (twist and row_starter and (right_rotation_cnt == 0 or right_rotation_cnt == 4 or right_rotation_cnt == 3)) or (
                    (not twist) and row_starter and (right_rotation_cnt == 1 or right_rotation_cnt == 2)) or (
                                  twist and (not row_starter) and (right_rotation_cnt == 1 or right_rotation_cnt == 0)) or (
                                  (not twist) and (not row_starter) and (right_rotation_cnt == 2 or right_rotation_cnt == 3))
            if should_flip and row_starter:
                y = 9 - y
            elif should_flip:
                x = 9 - x
            tweaked_tile[x][y] = tiles[id][i][j]
    tiles[id] = tweaked_tile
    return should_flip


active_tile = (VERY_FIRST_TILE_ID, 2, 0, False)
tiles_pool = neighbors.copy()
arrangement = []
flipped = False
row_starter_flipped = False
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
        if picked_neighbor is not None:
            flipped = tweak_tile(picked_neighbor[0], 3 - picked_neighbor[2], picked_neighbor[3] != flipped, False)
            flipped = flipped != (picked_neighbor[2] == 1)
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
                row_starter_flipped = tweak_tile(neighbor[0], 4 - neighbor[2], neighbor[3] != row_starter_flipped, True)
                flipped = neighbor[2] == 2
                row_starter_flipped = row_starter_flipped != (neighbor[2] == 2)
                break
print(arrangement)
for row in arrangement:
    for tile_id in row:
        for tile_row in tiles[tile_id]:
            print(tile_row)
        print()
    print("========== NEW ROW =====================================")
