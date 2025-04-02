import csv

def read_map_from_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [list(row[0]) for row in reader]

def simulate_guard(map_grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0

    rows = len(map_grid)
    cols = len(map_grid[0])

    start_position = None
    for i in range(rows):
        for j in range(cols):
            if map_grid[i][j] == '^':
                start_position = (i, j)
                map_grid[i][j] = '.'

    visited_positions = set()

    x, y = start_position

    while 0 <= x < rows and 0 <= y < cols:
        visited_positions.add((x, y))

        dx, dy = directions[direction_index]
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols and map_grid[nx][ny] == '#':
            direction_index = (direction_index + 1) % 4
        else:
            x, y = nx, ny

    return len(visited_positions)

filename = "Data.csv"
map_grid = read_map_from_csv(filename)
result = simulate_guard(map_grid)
print(f"Number of different positions visited by the guard: {result}")