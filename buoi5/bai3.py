'Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ'

n = int(input('Nhập độ dài list: '))
s = []
s_1 = []
for i in range(n):
    s.append(int(input(f's[{i}]: ')))

print('List s cần ghép là:')
m = int(input('Nhập độ dài list: '))
for i in range(m):
    s_1.append(int(input(f's_1[{i}]: ')))

s.extend(s_1)


print(f'List ban đầu được ghép thành: {s}')
