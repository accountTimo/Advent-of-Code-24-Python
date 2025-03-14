import re

def ReadCSV():
    with open("Data.csv", "r") as file:
        corrupted_memory = file.read().strip()
    return corrupted_memory

def sum_valid_mul_expressions(memory: str) -> int:
    mul_pattern = re.compile(r"mul\s*\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")
    do_pattern = re.compile(r"do\s*\(\)")
    dont_pattern = re.compile(r"don't\s*\(\)")

    enabled = True
    total = 0

    index = 0
    while index < len(memory):
        if do_pattern.match(memory, index):
            enabled = True
            index += 4
        elif dont_pattern.match(memory, index):
            enabled = False
            index += 7
        else:
            match = mul_pattern.match(memory, index)
            if match and enabled:
                x, y = map(int, match.groups())
                result = x * y
                print(f"Found: mul({x},{y}) = {result} in input")
                total += result
            index += 1

    return total

if __name__ == '__main__':
    corrupted_memory = ReadCSV()
    result = sum_valid_mul_expressions(corrupted_memory)
    print("Total sum:", result)