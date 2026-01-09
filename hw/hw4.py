# Задание 1: Магические методы __str__ и __call__
class Notification:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __call__(self):
        print("Уведомление отправлено")
# Проверка 1
n = Notification("Новое сообщение")
print(n) 
n()      

# Задание 2: Магические методы __add__ и __eq__
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
# Проверка 2
v1 = Vector(2, 3)
v2 = Vector(1, 1)
v3 = v1 + v2
print(f"Сложение векторов: x={v3.x}, y={v3.y}")
print(f"Векторы равны? {v1 == v2}")

# Задание 3: Методы класса
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def create_admin(cls, name):
        return cls(name, "admin")
# Проверка 3
admin = User.create_admin("Ardager")
print(f"Пользователь: {admin.name}, Роль: {admin.role}")