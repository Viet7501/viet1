'''
    Cho một list chứa nhiều phần tử mang nhiều kiểu dữ liệu khác nhau,
    trong đó có một phần tử kiểu tuple. Viết chương trình đếm số lượng
    các phần tử trong một list đó, đến khi gặp một phần tử kiểu tuple.
'''

list = [1, 2, 'Vietnam', (99, 'hello', 2 + 3j)]
count = 0
print(type(list[3]))
for i in range(len(list)):
    if type(list[i]) is not tuple:
        count += 1

print(f'Số lượng phần tử trong list đến khi gặp phần tử kiểu tuple là: {count}')