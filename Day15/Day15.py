with open("Data.csv", "r") as file:
    lines = file.readlines()
final_grid = [["."] * (50) for _ in range(len(lines[0]) - 1)]


def move_from_to(from_row, from_col, go_row, go_col, final_grid):
    if final_grid[from_row + go_row][from_col + go_col] == ".":
        final_grid[from_row][from_col] = "."
        final_grid[from_row + go_row][from_col + go_col] = "@"
        return True
    if final_grid[from_row + go_row][from_col + go_col] == "O":
        O_riginal = [go_row, go_col]
        while True:
            if go_row > 0:
                go_row += 1
            if go_row < 0:
                go_row -= 1
            if go_col > 0:
                go_col += 1
            if go_col < 0:
                go_col -= 1

            if final_grid[from_row + go_row][from_col + go_col] == "#":
                return False
            if final_grid[from_row + go_row][from_col + go_col] == ".":
                final_grid[from_row][from_col] = "."
                final_grid[from_row + O_riginal[0]][from_col + O_riginal[1]] = "@"
                final_grid[from_row + go_row][from_col + go_col] = "O"

                return True
    return False


moves = []
row = 0
for line in lines:
    if "#" in line[0]:
        line = line.split("\n")[0]
        col = 0
        for i in line:
            final_grid[row][col] = i
            col += 1
        row += 1
    else:
        line = line.split("\n")[0]
        for i in line:
            moves.append(i)

print(final_grid)
print(moves)


def findRobotCoords(final_grid):
    for row in range(len(final_grid)):
        for col in range(len(final_grid[0])):
            if final_grid[row][col] == "@":
                return row, col


def boxPoints(final_grid):
    total = 0
    for row in range(len(final_grid)):
        for col in range(len(final_grid[0])):
            if final_grid[row][col] == "O":
                total += row * 100 + col
    return total


for move in moves:
    robot_row, robot_col = findRobotCoords(final_grid)
    if move == "<":
        move_from_to(robot_row, robot_col, 0, -1, final_grid)
        continue
    if move == ">":
        move_from_to(robot_row, robot_col, 0, 1, final_grid)
        continue

    if move == "^":
        move_from_to(robot_row, robot_col, -1, 0, final_grid)
        continue

    if move == "v":
        move_from_to(robot_row, robot_col, 1, 0, final_grid)
        continue

print(boxPoints(final_grid))
