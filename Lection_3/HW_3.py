"""
Task 1. Використовуючи функцію print, надрукувати фразу “I love Python” 42 рази.
"""
# Version 1
a = "I Love Python "
print(a * 42)

# Version 2
for a in range(42):
    print("I Love Python ")
else:
    print("Done!")

# ==================================== #
"""
Task 2. Створити змінну age_in_month, надавши їй значення вашого поточного віку в місяцях.
"""
import datetime

today = datetime.date.today()
year = today.year
age_of_born = 1989
age_in_month = ((year - age_of_born) * 12) - 10

print(age_in_month)

# ==================================== #
"""
Task 3. Створити змінну age_in_years, в яку записати ваш вік в роках на основі попередньої змінної.
"""
age_in_years = int(age_in_month / 12)

print(age_in_years)

# ==================================== #
"""
Task 4. Створити змінну my_age, яка буде містити рядок 
“Му name is … I’m … years old”, де на замість пропусків буде підставлятись ваші імʼя та вік. 
Значення віку слід брати зі змінної age_in_years. 
"""
students_name = "Igor"
my_age = "My name is " + students_name + " I'm " + str(age_in_years) + " years old"

print(my_age)
# ==================================== #
"""
Task 5. Створити змінну зі значенням 1. 
Використовуючи оператори порівняння, порівняти її із будь-якими іншими значеннями 
(мінімум 5 порівнянь) і перевірити вивід в інтерпретаторі.
"""
b = 1
c = 1989
y = 2

print(b == age_of_born)
print(c == age_of_born)
print(c != age_of_born)
print(b != c)
print(b > c)
print(y < c)
print(age_of_born >= c)
print(y <= b)
# ==================================== #
"""
Task 6. Створити змінні a=2, b=5, c=6. 
На основі цих змінних створити змінну d, значення якої має бути “256”
"""
a = 2
b = 5
c = 6
d = str(a) + str(b) + str(c)

print(d)
# ==================================== #
