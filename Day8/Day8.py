import csv

def parse_input_from_csv(filename):
    grid = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            grid.append("".join(row))
    return grid


def parse_input(grid):
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                antennas.setdefault(cell, []).append((x, y))
    return antennas


def find_antinodes(antennas, width, height):
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Compute potential antinodes
                dx, dy = x2 - x1, y2 - y1

                # First antinode: closer to (x1, y1)
                ax1, ay1 = x1 - dx, y1 - dy
                if 0 <= ax1 < width and 0 <= ay1 < height:
                    antinodes.add((ax1, ay1))

                # Second antinode: closer to (x2, y2)
                ax2, ay2 = x2 + dx, y2 + dy
                if 0 <= ax2 < width and 0 <= ay2 < height:
                    antinodes.add((ax2, ay2))

    return len(antinodes)

filename = "Data.csv"
grid = parse_input_from_csv(filename)

antennas = parse_input(grid)
width, height = len(grid[0]), len(grid)
antinode_count = find_antinodes(antennas, width, height)
print("Total unique antinodes:", antinode_count)
