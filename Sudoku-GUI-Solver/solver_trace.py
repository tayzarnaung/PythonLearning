# solver.py
board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            print(f'Changed from {bo[row][col]} to {i} at pos {row}x{col}')
            bo[row][col] = i

            if solve(bo):
                print("Solve")
                return True

            bo[row][col] = 0
            print(f'Board reset to 0 at {row}x{col}')

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            print(f'{bo[pos[0]][i]} already exists in row')
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            print(bo[i][pos[1]], ' already exists in col')
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    print(f"Box at row:{box_x} col:{box_y}")

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                print(f'pos {i}x{j} is {num}')
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                print(f"Empty {i} x {j}")
                return (i, j)  # row, col

    return None


print_board(board)
solve(board)

print('***********************************')
print_board(board)
