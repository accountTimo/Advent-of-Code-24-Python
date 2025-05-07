from collections import defaultdict

with open("Data.csv") as f:
    lines = [line.strip() for line in f]

valid = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
antennas = [(x, y, c) for y, line in enumerate(lines) for x, c in enumerate(line) if c in valid]

freq_map = defaultdict(list)
for x, y, c in antennas:
    freq_map[c].append((x, y))

antinodes = set()
for positions in freq_map.values():
    if len(positions) < 2:
        continue
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            dx, dy = x2 - x1, y2 - y1
            for d in [-1, 1]:
                k = 1
                while 0 <= (nx := x1 + d * k * dx) < len(lines[0]) and 0 <= (ny := y1 + d * k * dy) < len(lines):
                    antinodes.add((nx, ny))
                    k += 1
    antinodes.update(positions)

print(len(antinodes))