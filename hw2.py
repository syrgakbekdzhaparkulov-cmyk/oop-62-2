class Employee: 
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def get_name (self):
        return self.name 
    def get_salary (self):
        return self.salary 
    def get_info (self):
        return f'Сотрудник: {self.name}, зарплата: {self.get_salary()}, позиция: {self.role}'

class BackendDeveloper (Employee):
    def __init__(self, name, salary, role, level):

        super().__init__(name, salary, role)
        self.level = level
        
    def get_salary(self):
        if self.level == 'Middle':
            return self.salary * 1.2  
        elif self.level == 'Senior':
            return self.salary * 1.5  
        else:
            return self.salary
        
    def get_info(self):
        return f'Сотрудник: {self.name}, зарплата: {int(self.get_salary())}, позиция: {self.role}, уровень: {self.level}'
class Manager (Employee):
    def __init__(self, name, salary, role, team_size):
        
        super().__init__(name, salary, role)
        self.team_size = team_size

    def get_salary(self):
        bonus = self.team_size * 1000
        return self.salary + bonus
    
    def get_info(self):
        return f'Сотрудник: {self.name}, зарплата: {int(self.get_salary())}, бонус за: {self.team_size} чел., позиция: {self.role}'

class Intern (Employee):
    def __init__(self, name, salary, role, months):
        
        super().__init__(name, salary, role)
        self.months = months

    def get_salary(self):
        return self.salary 
    
    def get_info(self):
        return f'Сотрудник: {self.name}, зарплата: {int(self.get_salary())}, позиция: {self.role}, длительность: {self.months}'


intrn = Intern("Artem", 10000, "Intern", "2 месяца")
man = Manager("Maria", 30000, "Bonus", 5)
dev = BackendDeveloper("Martin", 30000, "BackendDeveloper", "Senior")
emp = Employee ("Alex", 30000, "Employee")

print(emp.get_info())
print(dev.get_info())
print(man.get_info())
print(intrn.get_info())

def print_salary(employees_list):
    print('Список зарплат:')
    for employee in employees_list:
        salary = int(employee.get_salary())
        print(f"Имя: {employee.name} | Роль: {employee.role} | Зарплата: {salary}")
        
employees = [
   BackendDeveloper("Artem", 40000, "Backend Dev", "Middle"),
   Manager("Maria", 50000, "Manager", 5),
   Intern("Artem", 20000, "Intern", 3),
]
print_salary(employees)