
# Создайте базовый класс Employee с атрибутами name, salary (приватный) и методом display_info().
# От него унаследуйте Manager (добавляет атрибут department) и Developer (добавляет programming_language).
# Сделайте так, чтобы salary нельзя было изменить напрямую, но можно было через метод set_salary(), который проверяет, что зарплата не меньше 0.

class Employee():
    "Создание класса Сотрудник"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def display_info(self):
        print(f"Сотрудник: {self.name}")
        print(f"Зарплата: {self.__salary} рублей.")

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            raise ValueError("Зарплата не может быть отрицательной!")

class Manager(Employee):
    "Класс Менеджер, наследуется от Employee"

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display_info(self):
        super().display_info()
        print(f'Отдел: {self.department}')


class Developer(Employee):
    "Класс Разработчик, наследуется от Employee"

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Язык программирования: {self.programming_language}")

manager = Manager("Петр Васильев", 3500, "Продажи")
developer = Developer("Евгений Марков", 8600, "Python")

manager.display_info()
developer.display_info()

developer.set_salary(10000)
developer.display_info()

developer.set_salary(-1000)
