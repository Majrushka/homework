
# 1) Задача на строки: "Шифровальщик"
# Напишите программу, которая:
# Принимает строку от пользователя.
# Заменяет каждую гласную букву (а, е, ё, и, о, у, ы, э, ю, я) на следующую по алфавиту гласную (например, а → е, о → у, я → а).
# Выводит зашифрованную строку.

def encrypt_vowels(text):
    lower_vowels = "аеёиоуыэюя"
    upper_vowels = "АЕЁИОУЫЭЮЯ"
    encrypted_text = []
    
    for char in text:
        if char in lower_vowels:
            index = lower_vowels.index(char)
            next_index = (index + 1) % len(lower_vowels)
            encrypted_text.append(lower_vowels[next_index])
        elif char in upper_vowels:
            index = upper_vowels.index(char)
            next_index = (index + 1) % len(upper_vowels)
            encrypted_text.append(upper_vowels[next_index])
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text) # объединяет элементы списка в строку, используя указанный разделитель 


user_input = input("Введите строку для шифрования: ")

# Шифруем и выводим результат
encrypted = encrypt_vowels(user_input)
print("\n Зашифрованная строка:", encrypted)