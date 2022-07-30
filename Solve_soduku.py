board = [
    [8, 7, 0, 1, 3, 0, 0, 2, 5],
    [0, 9, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 3, 0, 6, 9, 8, 0, 4],
    [0, 0, 4, 0, 0, 7, 1, 0, 9],
    [7, 0, 0, 0, 1, 6, 0, 5, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 7, 0, 0, 3, 0],
    [0, 1, 7, 0, 8, 0, 2, 0, 6],
    [0, 0, 0, 2, 0, 3, 0, 0, 1]
]


# 0 refers to an empty case

def solve(bo):     #This function to solve sudoku
    find = find_empty(bo)
    if not find:    # sudoku is solved
        return True
    else:
        row, column = find
    for i in range(1, 10):
        if valid(bo, i, (row, column)):
            bo[row][column] = i

            if solve(bo):
                return True

            bo[row][column] = 0
    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False
    # Check square
    square_x = pos[1] // 3
    square_y = pos[0] // 3
    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):  # to visualize my list
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:  # After 3 rows
            print("-------------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end='')

            if j == 8:
                print(bo[i][j])

            else:
                print(str(bo[i][j]) + " ", end='')


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row & column
    return None


print_board(board)
solve(board)
print("=================================")
print_board(board)
print("\n" + "By Abdellah ELGUERMEZ")