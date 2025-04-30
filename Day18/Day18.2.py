from collections import deque

def is_path_possible(corrupted, grid_size=71):
    start = (0, 0)
    goal = (grid_size - 1, grid_size - 1)

    if start in corrupted or goal in corrupted:
        return False

    queue = deque([start])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                if (nx, ny) not in corrupted and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return False

byte_positions = []
with open("Data.csv", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            x_str, y_str = line.split(',')
            byte_positions.append((int(x_str), int(y_str)))

corrupted = set()
for coord in byte_positions:
    corrupted.add(coord)
    if not is_path_possible(corrupted):
        print(f"{coord[0]},{coord[1]}")
        break