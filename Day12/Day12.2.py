with open("Data.csv", "r") as file:
    gardenMap = [list(line.strip()) for line in file]

def getArea(regionCells):
    return len(regionCells)

def get_perimeter_sides(region_cells, gardenMap):
    fenceCoords = set()
    rows, cols = len(gardenMap), len(gardenMap[0])
    for r, c in region_cells:
        if r == 0 or gardenMap[r-1][c] != gardenMap[r][c]:
            fenceCoords.add(((r, c), "U"))
        if r == rows-1 or gardenMap[r+1][c] != gardenMap[r][c]:
            fenceCoords.add(((r, c), "D"))
        if c == 0 or gardenMap[r][c-1] != gardenMap[r][c]:
            fenceCoords.add(((r, c), "L"))
        if c == cols-1 or gardenMap[r][c+1] != gardenMap[r][c]:
            fenceCoords.add(((r, c), "R"))
    return fenceCoords

def fence_to_sides(fenceCoords):
    edges = {}
    for (r, c), d in fenceCoords:
        dr, dc = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}[d]
        er, ec = (r + r + dr) / 2, (c + c + dc) / 2
        edges[(er, ec)] = (dr, dc)

    visited = set()
    sides = 0
    for edge, direction in edges.items():
        if edge in visited:
            continue
        visited.add(edge)
        sides += 1
        er, ec = edge
        if er % 1 == 0:
            for dr in [-1, 1]:
                curr = er + dr
                while edges.get((curr, ec)) == direction:
                    visited.add((curr, ec))
                    curr += dr
        else:
            for dc in [-1, 1]:
                curr = ec + dc
                while edges.get((er, curr)) == direction:
                    visited.add((er, curr))
                    curr += dc
    return sides

def find_regions(gardenMap):
    visited = set()
    regions = []
    rows, cols = len(gardenMap), len(gardenMap[0])
    def dfs(r, c, t):
        stack, region = [(r, c)], []
        while stack:
            r, c = stack.pop()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            region.append((r, c))
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and gardenMap[nr][nc] == t and (nr, nc) not in visited:
                    stack.append((nr, nc))
        return region

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                regions.append(dfs(r, c, gardenMap[r][c]))
    return regions

total_price = sum(
    getArea(region) * fence_to_sides(get_perimeter_sides(region, gardenMap))
    for region in find_regions(gardenMap)
)

print(total_price)
