import heapq

with open("Data.csv", "r") as file:
    lines = [line.strip() for line in file if line.startswith("#")]

rows, cols = len(lines), len(lines[0])
grid = [list(line) for line in lines]

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (r, c)
        if grid[r][c] == 'E':
            end = (r, c)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

start_state = (start[0], start[1], 1)
distances = {start_state: 0}
previous = {start_state: []}
heap = [(0, start_state)]

while heap:
    cost, (r, c, d) = heapq.heappop(heap)
    if distances[(r, c, d)] < cost:
        continue

    nr, nc = r + directions[d][0], c + directions[d][1]
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
        new_state = (nr, nc, d)
        new_cost = cost + 1
        if new_state not in distances or new_cost < distances[new_state]:
            distances[new_state] = new_cost
            heapq.heappush(heap, (new_cost, new_state))
            previous[new_state] = [(r, c, d)]
        elif new_cost == distances[new_state]:
            previous[new_state].append((r, c, d))

    for turn in [-1, 1]:
        nd = (d + turn) % 4
        new_state = (r, c, nd)
        new_cost = cost + 1000
        if new_state not in distances or new_cost < distances[new_state]:
            distances[new_state] = new_cost
            heapq.heappush(heap, (new_cost, new_state))
            previous[new_state] = [(r, c, d)]
        elif new_cost == distances[new_state]:
            previous[new_state].append((r, c, d))

end_states = [state for state in distances if (state[0], state[1]) == end]

tiles_in_best_paths = set()

def backtrack(state):
    r, c, _ = state
    tiles_in_best_paths.add((r, c))
    for parent in previous.get(state, []):
        backtrack(parent)

for state in end_states:
    backtrack(state)

print(len(tiles_in_best_paths))
