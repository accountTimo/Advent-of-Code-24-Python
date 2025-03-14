def ReadCSV():
    with open("Data.csv", "r") as f:
        data = [line.strip() for line in f]
    return data

def isValidRow(numbers):
    increasing = all(x < y for x, y in zip(numbers, numbers[1:]))
    decreasing = all(x > y for x, y in zip(numbers, numbers[1:]))
    validDifferences = all(1 <= abs(x - y) <= 3 for x, y in zip(numbers, numbers[1:]))

    return (increasing or decreasing) and validDifferences

def canBeValidByRemovingOne(numbers):
    for i in range(len(numbers)):
        new_list = numbers[:i] + numbers[i + 1:]
        if isValidRow(new_list):
            return True
    return False

def countSafeReports(data):
    safe_count = 0

    for report in data:
        numbers = list(map(int, report.split()))

        if isValidRow(numbers):
            safe_count += 1
        elif canBeValidByRemovingOne(numbers):
            safe_count += 1

    return safe_count

if __name__ == '__main__':
    data = ReadCSV()
    print(countSafeReports(data))
