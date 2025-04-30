from collections import deque

with open("Data.csv", "r") as file:
    lines = file.readlines()

grid = []
for line in lines:
    grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "S":
            start = (row, col)
            break
    else:
        continue
    break

dist = [[-1] * cols for _ in range(rows)]
dist[start[0]][start[1]] = 0
queue = deque([start])

# BFS
while queue:
    row, col = queue.popleft()
    if grid[row][col] == "E":
        break
    for newRow, newCol in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        if 0 <= newRow < rows and 0 <= newCol < cols\
        and grid[newRow][newCol] != "#" \
        and dist[newRow][newCol] == -1:
            dist[newRow][newCol] = dist[row][col] + 1
            queue.append((newRow, newCol))

def countCheats(grid, dist):
    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "#": 
                continue
            for newRow, newCol in [(row + 2, col), (row + 1, col + 1), (row, col + 2), (row - 1, col + 1)]:
                if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] != "#":
                    if abs(dist[row][col] - dist[newRow][newCol]) >= 102:
                        count += 1
    return count

possible_cheats = countCheats(grid, dist)
print(possible_cheats)