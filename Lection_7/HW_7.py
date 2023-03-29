# 1. Створити телефонну книгу, яка матиме наступні команди:
# stats: кількість записів - DONE
# add: додати запис - DONE
# delete <name>: видалити запис за іменем (ключем) - DONE
# list: список всіх імен в книзі
# show <name>: детальна інформація по імені
# Записи не мають пмають повторюватися,
# заборонено перезаписувати записи, тільки видаляти і додавати заново.

phone_book = {}


def stats():
    print(f"Total amount of records in book: {len(phone_book)}")


def add():
    user_name = input("Enter the name: ")
    if user_name in phone_book:
        print("This name already exist in the phone book.")
    else:
        phone = input("Enter phone number: ")
        phone_book[user_name] = phone
        print(f"Record added: {user_name} - {phone}")


def delete(user_name):
    if user_name in phone_book:
        del phone_book[user_name]
        print(f"Record deleted: {user_name}")
    else:
        print(f"There is no record with name: {user_name}")


# Cannot add name of function "list" because PyCharm shows Shadows built-in name 'list'
def show_all():
    for user_name, phone in phone_book.items():
        print(f"Name: {user_name}, Phone: {phone}")


def show(user_name):
    if user_name in phone_book:
        print(f"Name: {user_name}, Phone: {phone_book[user_name]}")
    else:
        print(f"There is no record with name: {user_name}")


while True:
    command = input("Enter command (stats, add, delete, show_all, show, exit): ")
    if command == "stats":
        stats()
    elif command == "add":
        add()
    elif command == "delete":
        delete(user_name=input("What name to delete? "))
    elif command == "show_all":
        show_all()
    elif command == "show":
        show(user_name=input("Enter the name: "))
    elif command == "exit":
        break
    else:
        print("Invalid command. Please try again.")
