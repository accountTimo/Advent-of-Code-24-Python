from collections import deque
from functools import cache
from itertools import product

def compute_sequences(layout):
    positions = {key: (r, c) for r, row in enumerate(layout) for c, key in enumerate(row) if key is not None}
    sequences = {}
    for start in positions:
        for end in positions:
            if start == end:
                sequences[(start, end)] = ["A"]
                continue
            paths, q, shortest = [], deque([(positions[start], "")]), float("inf")
            while q:
                (r, c), path = q.popleft()
                for nr, nc, move in [(r-1,c,"^"), (r+1,c,"v"), (r,c-1,"<"), (r,c+1,">")]:
                    if 0 <= nr < len(layout) and 0 <= nc < len(layout[0]) and layout[nr][nc]:
                        if layout[nr][nc] == end:
                            if len(path)+1 > shortest: break
                            shortest = len(path)+1
                            paths.append(path + move + "A")
                        else:
                            q.append(((nr, nc), path + move))
                else: continue
                break
            sequences[(start, end)] = paths
    return sequences

def generate_sequences(s, sequences):
    options = [sequences[(a, b)] for a, b in zip("A"+s, s)]
    return ["".join(seq) for seq in product(*options)]

numeric_keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
directional_keypad = [[None, "^", "A"], ["<", "v", ">"]]

@cache
def compute_sequence_length(seq, depth=25):
    if depth == 1:
        return sum(directional_lengths[(a, b)] for a, b in zip("A"+seq, seq))
    return sum(min(compute_sequence_length(s, depth-1) for s in directional_sequences[(a, b)]) for a, b in zip("A"+seq, seq))

numeric_sequences = compute_sequences(numeric_keypad)
directional_sequences = compute_sequences(directional_keypad)
directional_lengths = {k: len(v[0]) for k, v in directional_sequences.items()}

total = 0
with open("Data.csv") as f:
    for line in f.read().splitlines():
        nums = generate_sequences(line, numeric_sequences)
        shortest = min(compute_sequence_length(seq, depth=25) for seq in nums)
        total += shortest * int(line[:-1])

print(total)
