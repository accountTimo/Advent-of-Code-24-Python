with open("Data.csv", "r") as file:
    lines = file.readlines()

def secretStep(secret):
    secret = (secret * 64 ^ secret) % 16777216
    secret = (secret // 32 ^ secret) % 16777216
    secret = (secret * 2048 ^ secret) % 16777216
    return secret

def findMax(sequence_totals):
    return max(sequence_totals, key=sequence_totals.get)

def findMaxBananas(lines):
    sequence_totals = {}
    for line in lines:
        secret_number = int(line)
        price_list = [secret_number % 10]
        for _ in range(2000):
            secret_number = secretStep(secret_number)
            price_list.append(secret_number % 10)
        tracked_sequences = set()
        for index in range(len(price_list) - 4):
            p1, p2, p3, p4, p5 = price_list[index:index + 5]
            price_change = (p2 - p1, p3 - p2, p4 - p3, p5 - p4)
            if price_change not in tracked_sequences:
                tracked_sequences.add(price_change)
                if price_change not in sequence_totals:
                    sequence_totals[price_change] = 0
                sequence_totals[price_change] += p5
    best_sequence = findMax(sequence_totals)
    return best_sequence, sequence_totals[best_sequence]

best_sequence, max_bananas = findMaxBananas(lines)

print("Best sequence: ", best_sequence)
print("Max bananas: ", max_bananas)