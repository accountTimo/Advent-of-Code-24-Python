grid = {i + j * 1j: char for i, row in enumerate(open('Data.csv'))
               for j, char in enumerate(row.strip())}

start_position = min(pos for pos in grid if grid[pos] == '^')

def check_path(grid):
    current_position, direction, visited = start_position, -1, set()
    while current_position in grid and (current_position, direction) not in visited:
        visited |= {(current_position, direction)}
        if grid.get(current_position + direction) == "#":
            direction *= -1j
        else:
            current_position += direction
    return {pos for pos, _ in visited}, (current_position, direction) in visited

path = check_path(grid)[0]
print(len(path),
      sum(check_path(grid | {offset: '#'})[1] for offset in path))