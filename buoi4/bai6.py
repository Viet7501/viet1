s = input('Nhập chuỗi: ')

k = input('Nhập ký tự: ')
print(f'Vị trí của ký tự "{k}" trong chuỗi "{s}" là: ')
for i in range(0,len(s)):
    if k == s[i]:
        print(i, end=' ')