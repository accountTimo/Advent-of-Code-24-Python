def count_constructions(design, patterns_set):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            if design[j:i] in patterns_set:
                dp[i] += dp[j]

    return dp[n]

with open("Data.csv", "r") as f:
    content = f.read().strip()

pattern_section, design_section = content.split("\n\n")
patterns = pattern_section.strip().split(", ")
designs = design_section.strip().splitlines()

patterns_set = set(patterns)

total_arrangements = sum(count_constructions(design, patterns_set) for design in designs)

print("Totaal aantal manieren om alle ontwerpen te maken:", total_arrangements)