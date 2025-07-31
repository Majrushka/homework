
class Bike:
    '''Простая модель велосипеда'''
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    def bike_info(self):
        print(f"У меня есть велосипед бренда {self.brand}. Его цвет {self.color}.")
    
# Создаем объекты класса Bike
bike1 = Bike("Cube", "синий")
bike2 = Bike("Specialized", "красный") # type: ignore
bike3 = Bike("Trek", "белый")

#выводим информацию о великах
bike1.bike_info()
bike2.bike_info()
bike3.bike_info()