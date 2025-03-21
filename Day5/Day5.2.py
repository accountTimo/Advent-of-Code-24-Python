from functools import cmp_to_key

with open('Data.csv') as f:
    rules, pages = f.read().split('\n\n')

cmp = cmp_to_key(lambda x, y: -(x + '|' + y in rules))
middle_page_numbers_sum = 0

for p in pages.split():
    p = p.split(',')
    s = sorted(p, key=cmp)

    if p != s:
        middle_page_numbers_sum += int(s[len(s) // 2])

print(middle_page_numbers_sum)