from cryptography.fernet import Fernet
from main import load_key

key = load_key()
f = Fernet(key)

def authorization(f):
    login = input("Введите логин: ").strip()
    password = input("Введите пароль: ").strip()

    with open("passwords.txt", "r") as file:
        for line in file:
            log, token = line.split("/", 1)
            trash, stored_log= log.split(":", 1)
            if stored_log == login:
                decrypted_pass = f.decrypt(token.encode()).decode()
                if password == decrypted_pass:
                    print("Вы успешно авторизованы")
                    return True
                else:
                    print("Неверный пароль")
                    return False
        print("В базе нет такого пользователя")
        return False

while True:
    if authorization(f):
        break