import re

with open("Data.csv", "r") as file:
    corrupted_memory = file.read().strip()

def sum_valid_mul_expressions(memory: str) -> int:
    pattern = re.compile(r"mul\s*\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")
    matches = pattern.findall(memory)

    total = 0
    for x, y in matches:
        result = int(x) * int(y)
        print(f"Found: mul({x},{y}) = {result} in input")
        total += result

    return total

if __name__ == '__main__':
    result = sum_valid_mul_expressions(corrupted_memory)
    print("Total sum:", result)