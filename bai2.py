import math

x = float(input('Nhập x: '))
y = float(input('Nhập y: '))
z = float(input('Nhập z: '))

F = (x + y + z)/(x**2 + y**2 + 1) - abs(x - z * math.cos(y))

print(f'F = {round(F,3)}')