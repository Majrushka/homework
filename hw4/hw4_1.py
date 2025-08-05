
# Создайте базовый класс Vehicle (транспортное средство) с защищённым (_protected) атрибутом max_speed 
# и приватным (__private) атрибутом mileage.
# Добавьте публичный метод display_info(), который выводит эти атрибуты.
# Создайте дочерний класс Bus, который наследует Vehicle и добавляет атрибут passenger_capacity.
# Переопределите метод display_info() в Bus, чтобы он показывал также вместимость пассажиров.

class Vehicle():
    """Простая модель транспортного средства"""
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self._max_speed = max_speed
        self.__mileage = mileage
    
    def display_info(self):
        """Выводит информацию о транспортном средстве"""
        long_name = f"Название транспортного средства: {self.name.title()}, максимальная скорость: {self._max_speed}, пробег: {self.__mileage}"
        print(long_name)


class Bus(Vehicle):
    """Дочерний класс транспортного средства"""

    def __init__(self, name, max_speed, mileage, passenger_capacity):
        super().__init__(name, max_speed, mileage)
        self.passenger_capacity = passenger_capacity
    
    def display_info(self):
        """Переопределяем метод родительского класса"""
        super().display_info()
        print(f"Вместимость: {self.passenger_capacity} человек.")


my_vehicle = Vehicle('land rover', 215, 5738)
my_vehicle.display_info()

my_bus = Bus("neoplan", 210, 8745, 103)
my_bus.display_info()