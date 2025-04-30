
with open("Data.csv", "r") as f:
    content = f.read().strip()
def can_construct(design, patterns_set):
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and design[j:i] in patterns_set:
                dp[i] = True
                break

    return dp[n]

pattern_section, design_section = content.split("\n\n")
patterns = pattern_section.strip().split(", ")
designs = design_section.strip().splitlines()

patterns_set = set(patterns)
count_possible = sum(can_construct(design, patterns_set) for design in designs)

print("Aantal mogelijke ontwerpen:", count_possible)