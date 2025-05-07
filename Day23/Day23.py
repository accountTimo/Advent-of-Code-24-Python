graph = {}

with open("Data.csv", "r") as f:
    for line in f:
        a, b = line.strip().split("-")
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)

triangles = set()

for a in graph:
    for b in graph[a]:
        if b <= a:
            continue
        for c in graph[a]:
            if c <= b or c == b:
                continue
            if c in graph[b]:
                triangle = tuple(sorted([a, b, c]))
                triangles.add(triangle)

triangles_with_t = [t for t in triangles if any(node.startswith("t") for node in t)]

# Resultaten tonen
print(f"Totaal aantal driehoeken: {len(triangles)}")
print(f"Aantal driehoeken met minstens één computer die met 't' begint: {len(triangles_with_t)}")
