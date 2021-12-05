import re
file_path = 'inputs/day4.txt'

drawn_numbers = []
bingo_boards = []
marker_boards = []
actual_board = []
marker_board = []
with open(file_path, 'r') as file:
    drawn_numbers = file.readline().rstrip().split(',')
    first = True
    for row in file:
        if not first:
            if row.rstrip() == '' and len(actual_board) != 0:
                bingo_boards.append(actual_board)
                marker_boards.append(marker_board)
                marker_board = []
                actual_board = []
            else:
                bingo_row = re.split("\\s+", row.strip())
                marker_row = 5 * [False]
                actual_board.append(bingo_row)
                marker_board.append(marker_row)
        else:
            first = False
    bingo_boards.append(actual_board)
    marker_boards.append(marker_board)
# print("Drawn numbers", drawn_numbers)
# print("First few bingo boards:\n", bingo_boards[0], bingo_boards[1], bingo_boards[2])
# print("Marker board init examples", marker_boards[0], marker_boards[1])
# print(bingo_boards)


def check_winner(marker_board, i, j):
    # print("Checked marker board", marker_board)
    # print(i, ". row", j, ". element investigation", )
    # print("Row:", marker_board[i])
    column = []
    for row in marker_board:
        column.append(row[j])
    # print("Column:", column)
    won = True
    for mark in marker_board[i]:
        won = won and mark
    won2 = True
    for mark in column:
        won2 = won2 and mark
    if won or won2:
        print("Winning combination!")
    return won or won2


last_winner = None
last_score = 0
already_won = []
for curr_number in drawn_numbers:
    # print("New draw:", curr_number)
    board_no = 0
    for bingo_board in bingo_boards:
        if board_no not in already_won:
            i = 0
            for bingo_row in bingo_board:
                j = 0
                for bingo_value in bingo_row:
                    if curr_number == bingo_value:
                        # print("found matching value in board", board_no, "position", i, j)
                        corresponding_marker_board = marker_boards[board_no]
                        corresponding_marker_board[i][j] = True
                        # print("This board's current marking:", corresponding_marker_board)
                        if check_winner(corresponding_marker_board, i, j):
                            already_won.append(board_no)
                            sum_of_unmarked = 0
                            k = 0
                            for marker_row in corresponding_marker_board:
                                l = 0
                                for marker in marker_row:
                                    if not marker:
                                        sum_of_unmarked += int(bingo_board[k][l])
                                    l += 1
                                k += 1
                            print("Winner board:", bingo_board)
                            last_winner = board_no
                            print("Last drawn number:", curr_number)
                            print("Sum of unmarked:", sum_of_unmarked)
                            print("Points", int(curr_number) * sum_of_unmarked)
                            last_score = int(curr_number) * sum_of_unmarked
                    j += 1
                i += 1
        board_no += 1

print("Last winning board is #", last_winner, "with score", last_score)
