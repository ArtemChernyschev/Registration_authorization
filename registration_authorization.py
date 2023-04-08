def write(login, password):
    with open('storage.txt', 'a', encoding='utf-8') as f:
        f.write(f'{login}:{password}\n')
        print('Пользователь успешно зарегистрирован')


def read(login):
    with open('storage.txt', encoding='utf-8') as f:
        for line in f:
            store_login, store_password = line.split(':')
            if login == store_login:
                return store_password.strip()

        
def registration():
    print('Регистрация нового пользователя')
    while True:
        login = input('Пожалуйста, введите логин (от 3 до 20 символов): ')
        assert 3 <= len(login) <= 20, 'Некорректный логин'
        password = input('Введите пароль: ')
        if not (4 <= len(password) <= 32):
            print('Некорректный пароль')
            continue
        if read(login):
            print('Пользователь уже зарегистрирован')
            break
        else:
            write(login, password)
            break


def authorization():
    print('Авторизация пользователя')
    while True:
        login = input('Введите логин: ')
        store_password = read(login)
        if store_password is None:
            print('Такого пользователя не существует')
            break
        password = input('Введите пароль: ')
        store_password = read(login)
        if password == store_password:
            print('Авторизация успешна')
            break
        read(login)
        print('Неправильный пароль')


def main():
    while True:
        reg_or_auth = input("Введите '1' - для регистрации, '2' - для авторизации: ")
        if reg_or_auth == '1':
            registration()
        elif reg_or_auth == '2':
            authorization()
        else:
            print('Некорректный ввод')


while True:
    try:
        main()
    except AssertionError:
        print('Логин должен быть от 3 до 20 символов')


if __name__ == '__main__':
    main()
