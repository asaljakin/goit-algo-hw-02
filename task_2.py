# Завдання 2

# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги (deque з модуля collections в Python),
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.

from collections import deque

def is_palindrome(s):
    # Привести рядок до нижнього регістру і видалити пробіли
    s = ''.join(s.lower().split())
    
    # Додати символи до двосторонньої черги
    d = deque(s)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

user_input = input("Введіть рядок: ")
if is_palindrome(user_input):
    print(f"'{user_input}' є паліндромом.")
else:
    print(f"'{user_input}' не є паліндромом.")