import csv
def read_csv(file_path):
    with open(file_path) as csvFile:
        return [row[0] for row in csv.reader(csvFile)]

def count_xmas(grid):
    word = "XMAS"
    reversed_word = word[::-1]
    count = 0
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # Horizontal, vertical, diagonal, reversed diagonal

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            for dr, dc in directions:
                # Normal
                if all(0 <= row + i * dr < len(grid) and 0 <= column + i * dc < len(grid[0]) and grid[row + i * dr][
                    column + i * dc] == word[i] for i in range(4)):
                    count += 1
                # Reversed
                if all(0 <= row + i * dr < len(grid) and 0 <= column + i * dc < len(grid[0]) and grid[row + i * dr][
                    column + i * dc] == reversed_word[i] for i in range(4)):
                    count += 1
    return count

if __name__ == '__main__':
    file_path = 'Data.csv'
    grid = read_csv(file_path)
    result = count_xmas(grid)
    print("Total number of XMAS occurrences:", result)


#humbling one liner from someone else LOL

# d = open("Data.csv").read()
# w = d.index('\n') + 1
# print(sum(d[i::p][:4] in ('XMAS', 'SAMX')
#       for i in range(len(d)) for p in (1, w, w+1, w-1)))