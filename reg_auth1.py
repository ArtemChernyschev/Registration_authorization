

def registeration():
    print("Регистрация нового пользователя")
    while True:
        login = input("Пожалуйста, введите логин (от 3 до 20 символов): ")
        if not (3 <= len(login) <= 20):
            print("Некорректный логин")
            continue
        try:
            with open(f"{login}.лог", "x") as f:
                password = input("Введите пароль (от 4 до 32 символов): ")
                if not (4 <= len(password) <= 32):
                    print("Некорректный пароль")
                    continue
                f.write(password)
                print("Пользователь успешно зарегистрирован")
                break
        except FileExistsError:
            print("Пользователь уже зарегистрирован")


def authorization():
    print("Авторизация пользователя")
    while True:
        login = input("Введите логин: ")
        try:
            with open(f"{login}.лог", "r") as f:
                password = input("Введите пароль: ")
                if password == f.read():
                    print("Авторизация успешна")
                    break
                else:
                    print("Неправильный пароль")
        except FileNotFoundError:
            print("Пользователь не найден")


def main():
    while True:
        reg_or_auth = input("Введите '1' - для регистрации, '2' - для авторизации: ")
        if reg_or_auth == '1':
            registeration()
        elif reg_or_auth == '2':
            authorization()
        else:
            print("Некорректный ввод")


if __name__ == "__main__":
    main()

