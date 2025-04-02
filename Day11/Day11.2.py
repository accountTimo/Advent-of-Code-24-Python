import csv
from collections import Counter

def transform(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        left = int(str(stone)[:half])
        right = int(str(stone)[half:])
        return [left, right]
    else:
        return [stone * 2024]

def count_stones_after_blinks(initialStones, blinks):
    stoneCounts = Counter(initialStones)

    for _ in range(blinks):
        new_stone_counts = Counter()
        for stone, count in stoneCounts.items():
            transformedStones = transform(stone)
            for new_stone in transformedStones:
                new_stone_counts[new_stone] += count \

        stoneCounts = new_stone_counts

    return sum(stoneCounts.values())

def read_stones_from_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            return [int(value) for cell in row for value in
                    cell.split()]

initial_stones = read_stones_from_csv("Data.csv")
stones75Blinks = count_stones_after_blinks(initial_stones, 75)
print("Aantal stenen na 75 knippers:", stones75Blinks)
