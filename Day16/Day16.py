import heapq

with open("Data.csv", "r") as file:
    lines = [line.strip() for line in file if line.startswith("#")]

final_grid = [list(line) for line in lines]
start = end = None

for r, row in enumerate(final_grid):
    for c, val in enumerate(row):
        if val == 'S':
            start = (r, c)
        elif val == 'E':
            end = (r, c)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start_state = (*start, 1)
dist = {start_state: 0}
queue = [(0, start_state)]

while queue:
    cost, (r, c, d) = heapq.heappop(queue)
    if (r, c) == end:
        print(cost)
        break
    if cost > dist[(r, c, d)]:
        continue
    for delta_dir, turn_cost in [((0, 1), 1), ((-1, 0), 1000), ((1, 0), 1000)]:
        new_d = (d + delta_dir[0]) % 4 if delta_dir != (0, 1) else d
        nr, nc = r + directions[new_d][0], c + directions[new_d][1]
        if 0 <= nr < len(final_grid) and 0 <= nc < len(final_grid[0]) and final_grid[nr][nc] != '#':
            state = (nr, nc, new_d) if delta_dir == (0, 1) else (r, c, new_d)
            new_cost = cost + turn_cost
            if state not in dist or new_cost < dist[state]:
                dist[state] = new_cost
                heapq.heappush(queue, (new_cost, state))
