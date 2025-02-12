# Завдання 3 (необов'язкове завдання)

# У багатьох мовах програмування ми маємо справу з виразами, виділеними символами-розділювачами,
#  такими як круглі ( ), квадратні [ ] або фігурні дужки { }.

# Напишіть програму, яка читає рядок з послідовністю символів-розділювачів,
#  наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, 
# коли розділювачі симетричні, несиметричні, наприклад ( ( ( ) , 
# або коли розділювачі різних видів стоять у парі, як-от ( }.

# Приклад очікуваного результату:

# ( ){[ 1 ]( 1 + 3 )( ){ }}: Симетрично
# ( 23 ( 2 - 3);: Несиметрично
# ( 11 }: Несиметрично


def is_balanced(expression):
    stack = []
    open_brackets = "({["
    close_brackets = ")}]"
    matching_bracket = {")": "(", "}": "{", "]": "["}
    
    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return False
    return not stack

# Запитати у користувача рядок
user_input = input("Введіть рядок з розділювачами: ")
if is_balanced(user_input):
    print(f"'{user_input}' симетрично.")
else:
    print(f"'{user_input}' несиметрично.")