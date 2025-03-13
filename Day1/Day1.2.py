

def read_csv(file_name):
    list1, list2 = [], []
    with open(file_name, "r") as file:
        for line in file:
            row = line.split()
            if len(row) >= 2:
                list1.append(int(row[0]))
                list2.append(int(row[1]))
    return list1, list2

def count_frequencies(numbers):
    frequency_dict = {}
    for number in numbers:
        frequency_dict[number] = frequency_dict.get(number, 0) + 1
    return frequency_dict

def calculate_similarity_score(DictList1, DictList2):
    similarity_score = 0
    for number in DictList1:
        if number in DictList2:
            similarity_score += number * DictList1[number] * DictList2[number]
    return similarity_score

def main():
    list1, list2 = read_csv("ListDay1.csv")
    DictList1 = count_frequencies(list1)
    DictList2 = count_frequencies(list2)
    similarity_score = calculate_similarity_score(DictList1, DictList2)

    print("Total similarity score:", similarity_score)
    print(DictList1)
    print(DictList2)

if __name__ == '__main__':
    main()

