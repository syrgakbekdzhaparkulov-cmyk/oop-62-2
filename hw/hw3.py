class User:
    def __init__(self, name, email, password):
        self.name = name               
        self._email = email            
        self.__password = password      

    def show_email(self):
        print(f"Email пользователя {self.name}: {self._email}")

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            print("Пароль успешно изменен.")
        else:
            print("Ошибка: старый пароль введен неверно. Доступ запрещен.")

user1 = User("Алексей", "alex@example.com", "secret123")

print(f"Имя: {user1.name}") 

user1.show_email()

print(f"Пароль '12345' верный? {user1.check_password('12345')}")
print(f"Пароль 'secret123' верный? {user1.check_password('secret123')}")

user1.change_password("wrong_pass", "new_pass_777") 
user1.change_password("secret123", "new_pass_777")


from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Машина едет по дороге")

class Bicycle(Transport):
    def move(self):
        print("Велосипед едет по велодорожке")

car = Car()
bike = Bicycle()

car.move()
bike.move()