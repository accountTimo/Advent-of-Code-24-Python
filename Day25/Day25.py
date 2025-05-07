with open("Data.csv") as f:
    data = f.read().split("\n\n")

locks, keys = [], []
for section in data:
    lines = section.splitlines()
    if all(c == "#" for c in lines[0]):
        locks.append(lines)
    elif all(c == "#" for c in lines[-1]):
        keys.append(lines)

def to_heights(s, rev=False):
    h, w = len(s), len(s[0])
    return [sum(1 for i in range(h) if s[i if not rev else h-1-i][c] == "#") for c in range(w)]

L = [to_heights(l) for l in locks]
K = [to_heights(k, rev=True) for k in keys]
H = len(locks[0])

print(sum(all(l[i] + k[i] <= H for i in range(len(l))) for l in L for k in K))