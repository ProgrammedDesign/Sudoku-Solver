
grid = [[1, 6, 8, 0, 0, 0, 9, 0, 2],
        [0, 0, 0, 3, 0, 1, 0, 0, 0],
        [0, 3, 0, 6, 2, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 1, 0, 6],
        [0, 0, 1, 0, 0, 0, 3, 7, 0],
        [0, 4, 3, 5, 0, 0, 0, 0, 9],
        [0, 0, 0, 8, 0, 2, 6, 0, 0],
        [0, 0, 0, 9, 0, 5, 0, 2, 3],
        [2, 0, 6, 0, 3, 0, 7, 0, 0]]


def board(gr):  # to make the grid look like a normal sudoku game board

    for i in range(len(grid)): # works with the rows
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])): # works with the columns
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def move_check(row, col, number):  # looks if each move is valid

    # check row
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    # check column
    for i in range(0, 9):
        if grid[i][col] == number:
            return False

    # check 3x3 square
    rows = (row // 3) * 3
    cols = (col // 3) * 3
    for r in range(0, 3):
        for c in range(0, 3):
            if grid[rows + r][cols + c] == number:
                return False

    return True


def finding_open_space(gr):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                return r, c


def solve(gr):  # does the actual solving

    blank = finding_open_space(grid) # 'blank' is the empty space on an actual sudoku board
    if not blank: # if there are no empty spaces then the board must be solved
        return True
    else:
        row, col = blank # making the values given from 'blank' into two separate values

        for number in range(1, 10):
            if move_check(row, col, number):
                grid[row][col] = number

                if solve(gr):
                    return True

                grid[row][col] = 0


print("Your unsolved Sudoku board is :")
board(grid)
solve(grid)
print("Your solved Sudoku board is :")
board(grid)
