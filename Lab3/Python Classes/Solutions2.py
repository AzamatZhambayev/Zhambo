class StringManipulator:
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Введите строку: ")
    
    def printString(self):
        print(self.s.upper())


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Точка: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнение: {amount}. Новый баланс: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Ошибка: недостаточно средств!")
        else:
            self.balance -= amount
            print(f"Снятие: {amount}. Остаток: {self.balance}")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = [10, 15, 17, 19, 21, 23, 29, 30]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Простые числа:", prime_numbers)