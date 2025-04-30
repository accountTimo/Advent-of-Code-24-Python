from collections import deque

corrupted = set()
with open("Data.csv", "r") as f:
    count = 0
    for line in f:
        line = line.strip()
        if not line:
            continue
        if count >= 1024:
            break
        try:
            x, y = map(int, line.split(','))
            corrupted.add((x, y))
            count += 1
        except ValueError:
            print(f"Fout bij parsen van regel: {line}")

def bfs(start, goal, corrupted, grid_size=71):
    queue = deque()
    visited = set()
    queue.append((start[0], start[1], 0))
    visited.add((start[0], start[1]))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == goal:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                if (nx, ny) not in corrupted and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
    return -1

start = (0, 0)
goal = (70, 70)
steps_needed = bfs(start, goal, corrupted)

print(f"Minimum number of steps to reach the exit: {steps_needed}")