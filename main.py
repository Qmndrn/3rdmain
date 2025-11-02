import os
from cryptography.fernet import Fernet


def write_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as file:
            file.write(key)
        print("Файл key.key создан")
    else:
        print("Файл key.key уже существует")


def load_key():
    with open("key.key", "rb") as file:
        return file.read()


def add(f):
    login = input("Введите логин: ").strip()
    password = input("Введите пароль: ").strip()
    token = f.encrypt(password.encode()).decode()
    with open("passwords.txt", "a") as file:
        file.write(f"Логин:{login}/Пароль:{token}\n")
    print("Сохранено")


def view(f):
    with open("passwords.txt", "r") as file:
        for splits in file:
         log, passw = splits.split("/", 1)
         password = f.decrypt(passw.encode()).decode()
         print(f"{log} Пароль:{password}")


def main():
    write_key()
    key = load_key()
    f = Fernet(key)
    add(f)
    while True:
        users_choice = input("1. Посмотреть  2. Добавить  3. Выйти: ").strip()
        if users_choice == "1":
            view(f)
        elif users_choice == "2":
            add(f)
        elif users_choice == "3":
            break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()
