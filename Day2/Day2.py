def ReadCSV():
    with open("Data.csv", "r") as f:
        data = [line.strip() for line in f]
    return data

def isValidRow(report):
    numbers = list(map(int, report.split()))

    increasing = all(x < y for x, y in zip(numbers, numbers[1:]))
    decreasing = all(x > y for x, y in zip(numbers, numbers[1:]))

    validDifferences = all(1 <= abs(x - y) <= 3 for x, y in zip(numbers, numbers[1:]))
    return (increasing or decreasing) and validDifferences

def countSafe_reports(data):
    return sum(1 for report in data if isValidRow(report))

if __name__ == '__main__':
    data = ReadCSV()
    print(countSafe_reports(data))