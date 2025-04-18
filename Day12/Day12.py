from collections import deque

def parse_inputFile(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines() if line.strip()]

def getNeighbors(x, y, width, height):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < height and 0 <= ny < width:
            yield nx, ny

def bfs(grid, visited, start_x, start_y):
    plantType = grid[start_x][start_y]
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    regionCells = []

    while queue:
        x, y = queue.popleft()
        regionCells.append((x, y))

        for nx, ny in getNeighbors(x, y, len(grid[0]), len(grid)):
            if not visited[nx][ny] and grid[nx][ny] == plantType:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return regionCells

def computePerimeter(grid, region_cells):
    plant_type = grid[region_cells[0][0]][region_cells[0][1]]
    perimeter = 0
    for x, y in region_cells:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                nx < 0 or nx >= len(grid) or
                ny < 0 or ny >= len(grid[0]) or
                grid[nx][ny] != plant_type
            ):
                perimeter += 1
    return perimeter

def total_fence_price(filename):
    grid = parse_inputFile(filename)
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    total_price = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if not visited[x][y]:
                region = bfs(grid, visited, x, y)
                area = len(region)
                perimeter = computePerimeter(grid, region)
                total_price += area * perimeter

    return total_price

print(total_fence_price("Data.csv"))
