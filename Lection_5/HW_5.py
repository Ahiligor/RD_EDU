"""
Task 1. 1. Створити програму, яка буде очікувати від користувача введення тексту
і виведе інформацію по кожному надрукованому символу:

це “число” + яке воно (парне, непарне),
це “буква” + яка вона (велика чи маленька),
це “символ”
"""

text = input("Enter any text please: ")

for letter in text:
    if letter.isdigit():
        if int(letter) % 2 == 0:
            print(f"This is a digit {letter} and it is even")
        else:
            print(f"This is a digit {letter} and it is odd")
    elif letter.isupper():
        print(f"This is Letter {letter} and it's Capital")
    elif letter.islower():
        print(f"This is Letter {letter} and it's Small")
    elif letter.isspace():
        print("This is space")
    else:
        print(f"This is a symbol {letter}")

# ===============================================

"""
Task 2.

Створити програму, яка буде друкувати в консоль “I love Python” кожні 4.2 секунди, 
поки її виконання не буде перервано вручну.

Підказка: для того, щоб програма могла зупинитися на вказаний час, можна використати бібліотеку time (import time), 
а саме функцію sleep(). (time.sleep(second), де second, це кількість секунд, які програма має чекати).
"""
import time

while True:
    print("I Love Python")
    time.sleep(4.2)
