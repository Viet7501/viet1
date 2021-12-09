s = input('Nhập câu: ')

list = list(s.split())
max = list[0]

for i in list:
    if len(i) > len(list[0]):
        max = i

print(f'Từ dài nhất trong câu "{s} là: {max}"')