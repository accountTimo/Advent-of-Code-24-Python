from functools import cache

def read_topographic_map(filename):
    with open(filename, "r") as file:
        return [list(map(int, line.strip())) for line in file]


def find_trailheads(grid):
    return [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 0]


def find_reachable_nines(grid, start):
    from collections import deque

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    reachable_nines = set()

    while queue:
        r, c = queue.popleft()
        if grid[r][c] == 9:
            reachable_nines.add((r, c))
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                if grid[nr][nc] == grid[r][c] + 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    return len(reachable_nines)


def count_distinct_paths(grid, start):


    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @cache
    def dfs(r, c):
        if grid[r][c] == 9:
            return 1

        path_count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == grid[r][c] + 1:
                path_count += dfs(nr, nc)

        return path_count

    return dfs(start[0], start[1])


def calculate_total_score(filename):
    grid = read_topographic_map(filename)
    trailheads = find_trailheads(grid)

    total_score = sum(find_reachable_nines(grid, start) for start in trailheads)
    total_rating = sum(count_distinct_paths(grid, start) for start in trailheads)

    print("Total Score:", total_score)
    print("Total Rating:", total_rating)

    return total_score, total_rating


if __name__ == "__main__":
    calculate_total_score("Data.csv")