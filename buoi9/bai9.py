"""
Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
"""

def dem_so_le(n):
    so_le = 0
    while n > 0:
        num = list(str(n))
        for i in num:
            if i in ('1', '3', '5', '7', '9'):
                so_le += 1
        return so_le

print(dem_so_le(123))
print(dem_so_le(19922610))

# def countOdd(n):
#     so_le = 0
#
#     while (n > 0):
#         rem = n % 10
#         if (rem % 2 != 0):
#             so_le += 1
#
#         n = int(n / 10)
#
#     return so_le
#
# print(countOdd(1235))