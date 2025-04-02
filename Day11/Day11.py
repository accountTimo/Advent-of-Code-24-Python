import csv

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
    stones = initialStones[:]

    for i in range(blinks):
        newStones = []
        for stone in stones:
            newStones.extend(transform(stone))
        stones = newStones

    return len(stones)

def read_stones_from_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            return [int(value) for cell in row for value in cell.split()]


initialStones = read_stones_from_csv("Data.csv")
stones_after_25_blinks = count_stones_after_blinks(initialStones, 25)
print("Aantal stenen na 25 knippers:", stones_after_25_blinks)
