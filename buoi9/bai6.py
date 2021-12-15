"""
Viết hàm
        def is_pangram(str, alphabet)
    đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
    Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần
"""


def is_pangram(str, alphabet='abcdefghijklmnopqrstuvwxyz'):
    for i in alphabet:
        if i not in str:
            return False
    return True

def pangram(str):
    if is_pangram(str) == True:
        print('Là chuỗi Pangram')
    else:
        print('Không phải chuỗi Pangram')

pangram('A quick brown fox jumps over the lazy dog')
pangram('A quick brown fox jumps over the lazy dog 123')
pangram('Hello my name is Viet')
