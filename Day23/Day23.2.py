from collections import defaultdict

graph = defaultdict(set)
with open("Data.csv") as f:
    for line in f:
        a, b = line.strip().split("-")
        graph[a].add(b)
        graph[b].add(a)

largest_clique = []

def bron_kerbosch(R, P, X):
    global largest_clique
    if not P and not X:
        if len(R) > len(largest_clique):
            largest_clique = list(R)
        return
    u = max(P | X, key=lambda node: len(graph[node]))
    for v in P - graph[u]:
        bron_kerbosch(R | {v}, P & graph[v], X & graph[v])
        P.remove(v)
        X.add(v)

all_nodes = set(graph.keys())
bron_kerbosch(set(), all_nodes, set())

password = ",".join(sorted(largest_clique))
print(f"LAN party wachtwoord: {password}")