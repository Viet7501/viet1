'''
    Cho 1 list chứa các tuple không rỗng. Viết chương trình sắp xếp list đó
    theo chiều tăng dần của phần tử cuối trong mỗi tuple.
    Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]
'''

list1 = [(2, 5), (4, 1), (0, 0), (1,9), (2,8)]

list1.sort(key = lambda x: x[1])

print(list1)