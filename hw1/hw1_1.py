# Задание 1. 

print('Введите последовательно два целых числа.')

number_1 = input("Введите первое число:")

number_2 = input('Введите второе число:')

a = int(number_1)
b = int(number_2)

if a > b:
    a, b = b, a # меняем местами, если a > b

numbers = list(range(a,b + 1))
# print(numbers)

total = sum(numbers)
print(total)