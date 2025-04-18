def parseInput(filepath):
    machines = []
    with open(filepath, "r") as file:
        lines = [line.strip() for line in file if line.strip()]
        for i in range(0, len(lines), 3):
            a_line = lines[i].split(":")[1].strip().split(",")
            b_line = lines[i+1].split(":")[1].strip().split(",")
            p_line = lines[i+2].split(":")[1].strip().split(",")

            Ax = int(a_line[0].replace("X+", "").strip())
            Ay = int(a_line[1].replace("Y+", "").strip())
            Bx = int(b_line[0].replace("X+", "").strip())
            By = int(b_line[1].replace("Y+", "").strip())
            Px = int(p_line[0].replace("X=", "").strip())
            Py = int(p_line[1].replace("Y=", "").strip())

            machines.append(((Ax, Ay), (Bx, By), (Px, Py)))
    return machines
def find_min_token_cost(A, B, P):
    Ax, Ay = A
    Bx, By = B
    Px, Py = P
    min_cost = None
    for a in range(0, 101):
        for b in range(0, 101):
            x = a * Ax + b * Bx
            y = a * Ay + b * By
            if x == Px and y == Py:
                cost = 3 * a + 1 * b
                if min_cost is None or cost < min_cost:
                    min_cost = cost
    return min_cost

machines = parseInput("Data.csv")
total_cost = 0
for A, B, P in machines:
    cost = find_min_token_cost(A, B, P)
    if cost is not None:
        total_cost += cost

print(total_cost)
