""" Xem code đã có trong file btvn_04_dog_walking.py.
Giải quyết yêu cầu sau:
        - Thêm method walk() vào class Pet và Dog. Khi gọi đến hàm walk() trong Pet thì vỡi mỗi đối tượng của Dog
        trong Pet sẽ gọi đến hàm walk() tương ứng.
        - Viết đoạn chương trình để in ra như sau:
            Tom is walking!
            Jerry is walking!
            Butt is walking!
"""


class Pets:
    name = []

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name} is walking! ')


class Dog(Pets):
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def eat(self):
        self.is_hungry = False

    def walk(self):
        print(f'{self.name} is walking! ')


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


dog1 = Dog('Tom', 5)
dog2 = Dog('Jerry', 2)
dog3 = Dog('Butt', 1)

Pets.walk(dog1)
Pets.walk(dog2)
Pets.walk(dog3)
