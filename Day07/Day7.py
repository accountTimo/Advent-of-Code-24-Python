import sys

sys.setrecursionlimit(10 ** 6)
input_file = sys.argv[1] if len(sys.argv) >= 2 else 'Data.csv'

part1_result = 0
part2_result = 0

data = open(input_file).read().strip()

def is_valid_equation(target, numbers, part2):
    if len(numbers) == 1:
        return numbers[0] == target

    if is_valid_equation(target, [numbers[0] + numbers[1]] + numbers[2:], part2):
        return True

    if is_valid_equation(target, [numbers[0] * numbers[1]] + numbers[2:], part2):
        return True

    if part2 and is_valid_equation(target, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:], part2):
        return True

    return False

for line in data.strip().split('\n'):
    target, numbers_str = line.strip().split(':')
    target = int(target)
    numbers = [int(x) for x in numbers_str.strip().split()]

    # Part 1
    if is_valid_equation(target, numbers, part2=False):
        part1_result += target


    # Part 2
    if is_valid_equation(target, numbers, part2=True):
        part2_result += target

print(f"Part 1 Result: {part1_result}")
print(f"Part 2 Result: {part2_result}")