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
            Px = int(p_line[0].replace("X=", "").strip()) + 10**13
            Py = int(p_line[1].replace("Y=", "").strip()) + 10**13

            machines.append(((Ax, Ay), (Bx, By), (Px, Py)))
    return machines

def extended_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x1, y1, d = extended_gcd(b, a % b)
        return y1, x1 - (a // b) * y1, d

def find_min_token_cost(A, B, P):
    Ax, Ay = A
    Bx, By = B
    Px, Py = P

    det = Ax * By - Ay * Bx
    if det == 0:
        return None

    dx = Px
    dy = Py

    a_numer = dx * By - dy * Bx
    b_numer = Ax * dy - Ay * dx

    if a_numer % det != 0 or b_numer % det != 0:
        return None

    a = a_numer // det
    b = b_numer // det

    if a < 0 or b < 0:
        return None

    return 3 * a + b

machines = parseInput("Data.csv")
total_cost = 0
for A, B, P in machines:
    cost = find_min_token_cost(A, B, P)
    if cost is not None:
        total_cost += cost

print("Totaal minimum aantal tokens:", total_cost)