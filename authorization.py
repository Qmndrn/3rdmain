from cryptography.fernet import Fernet
from main import load_key


def authorization(login, password, fernet):
    with open("passwords.txt", "r") as file:
        for line in file:
            raw_login, token = line.split("/", 1)
            stored_login = raw_login.split(":", 1)[1]

            if stored_login == login and password == fernet.decrypt(token.encode()).decode():
                print("Вы успешно авторизованы")
                return True

            if stored_login == login:
                print("Неверный пароль")
                return False

    print("В базе нет такого пользователя")
    return False


def main():
    key = load_key()
    fernet = Fernet(key)

    while True:
        login = input("Введите логин: ").strip()
        password = input("Введите пароль: ").strip()
        if authorization(login, password, fernet):
            break


if __name__ == "__main__":
    main()
