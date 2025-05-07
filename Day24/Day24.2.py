with open("Data.csv") as f:
    lines = f.readlines()

formulas = {}
for line in lines:
    if "->" in line:
        a, op, b, _, c = line.strip().split()
        formulas[c] = (a, b, op)

def w(p, i): return f"{p}{i:02d}"

def vz(wire, i):
    if wire not in formulas: return False
    x, y, op = formulas[wire]
    if op != "XOR": return False
    if i == 0: return sorted([x, y]) == ["x00", "y00"]
    return (vix(x, i) and vcb(y, i)) or (vix(y, i) and vcb(x, i))

def vix(wire, i):
    if wire not in formulas: return False
    x, y, op = formulas[wire]
    return op == "XOR" and sorted([x, y]) == [w("x", i), w("y", i)]

def vcb(wire, i):
    if wire not in formulas: return False
    x, y, op = formulas[wire]
    if i == 1: return op == "AND" and sorted([x, y]) == ["x00", "y00"]
    if op != "OR": return False
    return (vdc(x, i-1) and vrc(y, i-1)) or (vdc(y, i-1) and vrc(x, i-1))

def vdc(wire, i):
    if wire not in formulas: return False
    x, y, op = formulas[wire]
    return op == "AND" and sorted([x, y]) == [w("x", i), w("y", i)]

def vrc(wire, i):
    if wire not in formulas: return False
    x, y, op = formulas[wire]
    return op == "AND" and ((vix(x, i) and vcb(y, i)) or (vix(y, i) and vcb(x, i)))

def verify(i): return vz(w(f"z", i), i)

def progress():
    i = 0
    while verify(i): i += 1
    return i

swaps = []
for _ in range(4):
    base = progress()
    for x in formulas:
        for y in formulas:
            if x == y: continue
            formulas[x], formulas[y] = formulas[y], formulas[x]
            if progress() > base:
                swaps += [x, y]
                break
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else: continue
        break

print(",".join(sorted(swaps)))
