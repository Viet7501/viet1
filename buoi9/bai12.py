"""
Viết hàm
        def find_x(a_list, x)
trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
"""

def find_x(a_list, x):
    if x not in a_list:
        print(-1)
    else:
        for i in range(len(a_list)):
            if a_list[i] == x:
                print(i, end=' ')


find_x(['a', 'a', 'b', 'c', 'a'], 'a')
print('\n')
find_x([1, 2, 3, 4, 5, 3, 3, 7], 3)
