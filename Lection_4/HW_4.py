"""
1. Створити програму, яка буде очікувати введення тексту від користувача і повідомляти —
чи є введений текст “числом” чи “словом”.

2. Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.

3. Якщо це “слово”, програма має вказати його довжину.
"""

text_or_value = input("Enter please any text ")

if text_or_value is int:
    print("This is 'number")
else:
    print("This is text")

print(type(text_or_value))
print(text_or_value)
