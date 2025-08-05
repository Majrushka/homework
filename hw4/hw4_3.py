
# Реализуйте класс BankAccount:
# Приватные атрибуты: __balance, __account_number.
# Геттеры для баланса и номера счёта. Сеттер только для баланса (с проверкой, что баланс не может быть отрицательным).
# Статический метод generate_account_number(), который возвращает случайный 10-значный номер счёта.
# Метод класса create_account(cls, initial_balance), который создаёт аккаунт с сгенерированным номером.

import random

class BankAccount():
    "Создание класса Банковский счет"

    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, x):
        if x < 0:
            raise ValueError("Баланс не может быть отрицательным!")
        self.__balance = x


    @property
    def account_number(self):
        return self.__account_number
    
    @staticmethod
    def generate_account_number():
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    @classmethod
    def create_account(cls, initial_balance):
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным!")
        account_number = cls.generate_account_number()
        return cls(initial_balance, account_number)
    

account = BankAccount.create_account(100000)

print(f"Номер Вашего банковского счета: {account.account_number}")
print(f"Баланс: {account.balance} долларов США")

# Попробуем изменить баланс
account.balance = 15000000
print(f"Баланс: {account.balance} долларов США")

# Отрицательный баланс
account.balance = -500