
# Создайте класс Temperature с приватным атрибутом __celsius.
# Реализуйте геттер и сеттер для celsius, где сеттер проверяет, 
# что температура не может быть ниже -273.15°C (абсолютный ноль).
# Добавьте свойство fahrenheit (геттер), которое возвращает температуру в Фаренгейтах
# (формула: °F = °C * 9/5 + 32).

class Temperature():
    """Создание класса Температура"""

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        print("getter method")
        return self.__celsius

    @celsius.setter
    def celsius(self, new_celsius):
        if new_celsius < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля!!!")
        self.__celsius = new_celsius

    def fahrenheit(self):
        return self.__celsius * 9/5 + 32

temp1 = Temperature(47)
print(f"Температура в Фаренгейтах: {temp1.fahrenheit()}")

temp2 = Temperature(-281)
print(f"Температура в Фаренгейтах: {temp2.fahrenheit()}")
temp2.celsius
temp1.celsius = -300
