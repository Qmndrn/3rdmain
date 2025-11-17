from cryptography.fernet import Fernet
from main import load_key


def authorization(fernet: Fernet):
    login = input("Введите логин: ").strip()
    password = input("Введите пароль: ").strip()

    with open("passwords.txt", "r") as file:
        for line in file:
            raw_login, encrypted = line.split("/", 1)
            _, stored_login = raw_login.split(":", 1)
            if (
                stored_login == login
                and password == fernet.decrypt(encrypted.encode()).decode()
            ):
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
    while not authorization(fernet):
        pass


if __name__ == "__main__":
    main()
