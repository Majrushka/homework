
class Whatever:
    def __init__(self, *args):
        self.text_field = None
        self.number_field = None

        #Проверяем количество и тип аргументов
        if len(args) == 2:
            arg1, arg2 = args

            if isinstance(arg1, str) and isinstance(arg2, str):
                self.text_field = f"{arg1} {arg2}"

            elif isinstance (arg1, int) and isinstance(arg2, int):
                self.number_field = arg1 + arg2

            elif (isinstance(arg1, str) and isinstance(arg2, int)) or (isinstance(arg1, int) and isinstance(arg2, str)):
                for arg in args:
                    if isinstance(arg, str):
                        self.text_field = arg
                    else:
                        self.number_field = arg

    
    def __str__(self):
        info = []
        if self.text_field is not None:
            info.append(f"Текствовое поле: '{self.text_field}'")
        if self.number_field is not None:
            info.append(f"Числовое поле: {self.number_field}")
        return " " .join(info) if info else "Поля не созданы"
    

# Тестирование всех возможных случаев
# 1. Текст и число (в разном порядке)
whatever1 = Whatever("I don't like the fact, that I have to switch the keybord the following amount of times:", 100)
print(whatever1)  

whatever2 = Whatever(500, "It's just a random number. I don't know, why I decided to choose it.")
print(whatever2)  

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