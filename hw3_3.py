# Напишите программу, в которой описан класс. 
# У объектов класса должно быть поле, представляющее собой числовой список.
# Этот список формируется на основе списка, переданного конструктору в качестве аргумента.
# При этом из списка-аргумента в список-поле включаются только числовые элементы (элементы других типов игнорируются).
# Необходимо также описать метод, отображающий содержимое поля списка, 
# а также метод, вычисляющий среднее значение элементов поля списка (сумма значений элементов, деленная на их количество).


class MixedList:

    def __init__(self, input_list):
        self.numbers = [
            item for item in input_list 
            if isinstance(item, (int, float)) and not isinstance(item, bool)
            ]
    

    def numbers_display(self):
        print("Здесь мы можем увидеть список с полученными числами: ", self.numbers)


    def average_numbers(self):
        if self.numbers:
            average = (sum(self.numbers) / len(self.numbers))
            print("Среднее значение элементов в списке: ", average)
        else:
            print("Список пуст.")


my_list = [-10, 9.16, "Привет", 42, True, "World", 7.5, False, 100000]

# Создаем экземпляр класса MixedList
mixed_list1 = MixedList(my_list)
mixed_list1.numbers_display()
mixed_list1.average_numbers()


# Пример с пустым списком
mixed_list2 = MixedList(["какой-то текст", True, False, "чисел нет"])
mixed_list2.numbers_display()
mixed_list2.average_numbers()
