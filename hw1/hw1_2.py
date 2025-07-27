# Задание 2.


# создадим список вводимых пользователем чисел
numbers = []

while True:
    user_input = input("Введите число (или любой нечисловой символ для завершения): ")
    try:
        number = float(user_input)  # Преобразуем ввод в число (учтём и целые, и дробные)
        numbers.append(number)
    except ValueError:
        break  # Выходим из цикла при вводе нечислового значения

if numbers:
    min_num = min(numbers)
    max_num = max(numbers)
    print(f"Минимальное число: {min_num}")
    print(f"Максимальное число: {max_num}")
    
else:
    print("Вы не ввели ни одного числа.")