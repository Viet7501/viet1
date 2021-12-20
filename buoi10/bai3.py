"""
Hãy nghĩ ra một đối tượng trong thực tế, tìm thuộc tính và
các hành vi của nó rồi xây dựng một class cho các đối tượng vừa nghĩ ra.
"""


class Vehicle:

    def __init__(self, loai_xe, nam_san_xuat, mau_xe):
        self.loai_xe = loai_xe
        self.nam_san_xuat = nam_san_xuat
        self.mau_xe = mau_xe

    def khoi_dong_xe(self):
        print(f'Bạn đang khởi động xe {self.loai_xe} {self.nam_san_xuat} - màu {self.mau_xe}')

    def di_chuyen(self):
        print(f'Xe {self.loai_xe} đang di chuyển')

    def dung_lai(self):
        print(f'Xe {self.loai_xe} đang không đi chuyển')

    def tang_toc(self):
        print(f'Xe {self.loai_xe} đang tăng tốc')

    def giam_toc(self):
        print(f'Xe {self.loai_xe} đang giảm tốc')


car1 = Vehicle('Ferrari', '2020', 'đỏ')
car1.khoi_dong_xe()
car1.tang_toc()
car1.giam_toc()
car1.dung_lai()

print('')
car2 = Vehicle('Mercedes', '2018', 'xanh')
car2.dung_lai()
