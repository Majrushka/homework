Напишите программу, в которой описан класс со следующими свойствами.
# В классе описан конструктор, которому в качестве аргументов
# (помимо первой ссылки на создаваемый объект) передаются текст и целое число,
# причем в произвольном порядке. Число и текст присваиваются как значения определенным полям.
# Если переданы два текстовых значения, то создается только текстовое поле со значением,
# получающимся объединением значений аргументов. Если аргументами переданы два числовых поля,
# то у объекта будет только поле с целочисленным значением, равным сумме значений аргументов.
# В иных случаях поля для объекта не создаются. Создать на основе класса объекты и проверить функциональность кода.

class Whatever:
    def __init__(self, *args):
        self.text = None
        self.number = None
        
        # Фильтрация аргументов: отдельно числа и строки
        numbers = [arg for arg in args if isinstance(arg, int)]
        texts = [arg for arg in args if isinstance(arg, str)]
        
        # Логика создания полей
        if len(texts) == 2:
            arg1, arg2 = args
            self.text = f"{arg1} {arg2}"
        elif len(numbers) == 2:
            arg1, arg2 = args
            self.number = arg1 + arg2
        # В остальных случаях поля остаются None (не создаются)

    def __str__(self):
        info = []
        if self.text is not None:
            info.append(f"Текствовое поле: '{self.text}'")
        if self.number is not None:
            info.append(f"Числовое поле: {self.number}")
        return " " .join(info) if info else "Поля не созданы"


# Тестирование всех возможных случаев
# 1. Текст и число (в разном порядке)
whatever1 = Whatever("I don't like the fact, that I have to switch the keybord the following amount of times:", 100)
print(whatever1)  # (поля не созданы)

whatever2 = Whatever(500, "It's just a random number. I don't know, why I decided to choose it.")
print(whatever2)  # (поля не созданы)

# 2. Два текста
whatever3 = Whatever("Пайтон - это очень интересно.", "Хотя путешествовать, возможно, еще интереснее.")
print(whatever3)  

# 3. Два числа
whatever4 = Whatever(40, 60)
print(whatever4)  # (Числовое поле: 100)

# 4. Некорректные случаи (поля не создаются)
whatever5 = Whatever("Я - Майрушка")  # только один аргумент
print(whatever5)  # (поля не созданы)

whatever6 = Whatever(3.14, "Это Pi")  # float + str
print(whatever6)  # (поля не созданы)

whatever7 = Whatever(10, 20, 30)  # три аргумента
print(whatever7)  # (поля не созданы)
