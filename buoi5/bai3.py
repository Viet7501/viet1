n = int(input('Nhập độ dài list: '))
s = []
s_1 = []
list = []
for i in range(n):
    s.append(int(input(f's[{i}]: ')))

print('List s cần ghép là:')
m = int(input('Nhập độ dài list: '))
for i in range(m):
    s_1.append(int(input(f's_1[{i}]: ')))

list = s + s_1

print(f'List mới là: {list}')