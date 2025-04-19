with open("Data.csv", "r") as file:
    lines = file.readlines()

final_grid = [["."] * 50 for _ in range(len(lines[0]) - 1)]
moves = []

row = 0
for line in lines:
    line = line.strip()
    if "#" in line:
        for col, ch in enumerate(line):
            final_grid[row][col] = ch
        row += 1
    else:
        moves.extend(line)

def find_soulmate(grid, r, c):
    return (r, c + 1) if grid[r][c] == "[" else (r, c - 1)

def collect_boxes_and_validate(grid, r, c, dr, dc):
    boxes = []
    queue = [(r, c)]

    while queue:
        cr, cc = queue.pop(0)
        if (cr, cc) not in boxes:
            boxes.append((cr, cc))
            mate = find_soulmate(grid, cr, cc)
            queue.append(mate)
            if mate not in boxes:
                boxes.append(mate)

        nr, nc = cr + dr, cc + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] in ["[", "]"] and (nr, nc) not in boxes:
                queue.append((nr, nc))
            elif grid[nr][nc] == "#":
                return None
    return boxes

def move_robot(r, c, dr, dc, grid):
    nr, nc = r + dr, c + dc

    if grid[nr][nc] == ".":
        grid[r][c] = "."
        grid[nr][nc] = "@"
        return True

    if dr == 0 and dc == -1 and grid[nr][nc] == "]":
        path = [[dr, dc]]
        while True:
            dc -= 1
            path.append([dr, dc])
            if grid[r + dr][c + dc] == "#":
                return False
            if grid[r + dr][c + dc] == ".":
                grid[r][c] = "."
                for i in range(len(path) - 1, 0, -1):
                    pr, pc = path[i]
                    qr, qc = path[i - 1]
                    grid[r + pr][c + pc] = grid[r + qr][c + qc]
                grid[r + path[0][0]][c + path[0][1]] = "@"
                return True

    if dr == 0 and dc == 1 and grid[nr][nc] == "[":
        path = [[dr, dc]]
        while True:
            dc += 1
            path.append([dr, dc])
            if grid[r + dr][c + dc] == "#":
                return False
            if grid[r + dr][c + dc] == ".":
                grid[r][c] = "."
                for i in range(len(path) - 1, 0, -1):
                    pr, pc = path[i]
                    qr, qc = path[i - 1]
                    grid[r + pr][c + pc] = grid[r + qr][c + qc]
                grid[r + path[0][0]][c + path[0][1]] = "@"
                return True

    if grid[nr][nc] in ["[", "]"]:
        boxes = collect_boxes_and_validate(grid, nr, nc, dr, dc)
        if not boxes:
            return False
        boxes.sort(reverse=(dr == 1))
        for br, bc in boxes:
            grid[br + dr][bc + dc] = grid[br][bc]
            grid[br][bc] = "."
        grid[r][c] = "."
        grid[r + dr][c + dc] = "@"
        return True

    return False

temp_grid = [["."] * 100 for _ in range(len(lines[0]) - 1)]
for r in range(len(final_grid)):
    for c in range(len(final_grid[0])):
        ch = final_grid[r][c]
        if ch == "#":
            temp_grid[r][2 * c - 1] = "#"
            temp_grid[r][2 * c] = "#"
        elif ch == "O":
            temp_grid[r][2 * c - 1] = "["
            temp_grid[r][2 * c] = "]"
        elif ch == ".":
            temp_grid[r][2 * c - 1] = "."
            temp_grid[r][2 * c] = "."
        elif ch == "@":
            temp_grid[r][2 * c - 1] = "@"
            temp_grid[r][2 * c] = "."
final_grid = temp_grid

def find_robot(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                return r, c

def box_score(grid):
    return sum(r * 100 + c for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "]")

for m in moves:
    r, c = find_robot(final_grid)
    if m == "<":
        move_robot(r, c, 0, -1, final_grid)
    elif m == ">":
        move_robot(r, c, 0, 1, final_grid)
    elif m == "^":
        move_robot(r, c, -1, 0, final_grid)
    elif m == "v":
        move_robot(r, c, 1, 0, final_grid)

print("Box points", box_score(final_grid))
