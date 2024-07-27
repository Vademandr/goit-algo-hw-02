from collections import deque


def is_palindrome(input_string):
    # Нормалізуємо вхідний рядок: перетворюємо його в нижній регістр і видаляємо пробіли
    normalized_string = "".join(input_string.lower().split())

    # Створюємо двобічну чергу (deque) і додаємо всі символи
    char_deque = deque(normalized_string)

    while len(char_deque) > 1:
        # Порівнюємо символи на обох кінцях
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


# Тести
test_strings = [
    "Radar",
    "C i v i c",
    "Neoversity",
    "My life 1",
    "The best way to predict the future is to create it",
    "L i m i t",
    "8 Level 8",
]

for test in test_strings:
    print(f"'{test}' palindrom: {is_palindrome(test)}")