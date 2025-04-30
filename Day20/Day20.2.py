from collections import deque

with open("Data.csv") as f:
    grid = [list(line.strip()) for line in f]

rows, cols = len(grid), len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            start = (r, c)
            break
    else:
        continue
    break

dist = [[-1] * cols for _ in range(rows)]
dist[start[0]][start[1]] = 0
queue = deque([start])

while queue:
    r, c = queue.popleft()
    if grid[r][c] == "E":
        break
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            queue.append((nr, nc))

def count_cheats(grid, dist):
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue
            for d in range(2, 21):
                for dr in range(d + 1):
                    dc = d - dr
                    for nr, nc in {(r+dr,c+dc), (r+dr,c-dc), (r-dr,c+dc), (r-dr,c-dc)}:
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
                            if dist[r][c] - dist[nr][nc] >= 100 + d:
                                count += 1
    return count

print(count_cheats(grid, dist))
