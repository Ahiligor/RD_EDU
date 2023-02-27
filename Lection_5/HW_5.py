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
            print("This is a digit and it is even")
        else:
            print("This is a digit and it is odd")
    elif letter.isupper():
        print("Letter is Capital")
    elif letter.islower():
        print("Letter is Small")
    elif letter.isspace():
        print("This is space")
    elif letter.isalnum():
        print("This is a symbol")
