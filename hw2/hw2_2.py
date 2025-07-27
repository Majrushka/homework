# 2) Задача на списки и словари: "Статистика по тексту"
# Напишите программу, которая:
# Принимает от пользователя текст (можно многострочный).
# Считает:
# Количество уникальных слов (без учёта регистра).
# Самое длинное слово.
# Частоту каждой буквы (сколько раз встречается а, б и т.д.).

def text_statistics():
    # Получаем текст от пользователя (многострочный)
    print("Введите текст (для завершения ввода нажмите Enter дважды):")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    
    # Обработка текста
    words = []
    current_word = []
    for char in text.lower():
        if char.isalpha():  # если это буква
            current_word.append(char)
        else:
            if current_word:  # если накопились буквы
                words.append(''.join(current_word))
                current_word = []
    # Добавляем последнее слово, если текст заканчивается буквой
    if current_word:
        words.append(''.join(current_word))
    
    # 1. Количество уникальных слов
    unique_words = set(words)
    print(f"\nКоличество уникальных слов: {len(unique_words)}")
    
    # 2. Самое длинное слово
    if words:
        longest_word = max(words, key=len)
        print(f"Самое длинное слово: '{longest_word}' (длина: {len(longest_word)})")
    else:
        print("В тексте нет слов")
    
    # 3. Частота каждой буквы
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    print("\nЧастота букв:")
    for letter in sorted(letter_counts):
        print(f"'{letter}': {letter_counts[letter]}")


# Запускаем программу
text_statistics()