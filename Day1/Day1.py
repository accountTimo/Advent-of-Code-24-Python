

def split_list():
    list1 = []
    list2 = []

    with open("ListDay1.csv", "r") as file:
        for line in file:
            row = line.split()
            if len(row) >= 2:
                list1.append(int(row[0]))
                list2.append(int(row[1]))


    list1.sort()
    list2.sort()

    return list1, list2

def count_difference(list1, list2):
    differences = []

    for i, j in zip(list1, list2):
        differences.append(abs(j - i))

    return differences

def sum_difference(differences):
    total = 0
    for i in differences:
        total += i
    return total

if __name__ == '__main__':
    list1, list2 = split_list()
    differences = count_difference(list1, list2)
    total_difference = sum_difference(differences)
    print("Totale verschil:", total_difference)
