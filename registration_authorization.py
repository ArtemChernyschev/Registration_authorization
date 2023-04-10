def write(login, password):
    with open('storage.txt', 'a', encoding='utf-8') as f:
        f.write(f'{login}:{password}\n')
        print('Пользователь успешно зарегистрирован')


def comp_data(login):
    with open('storage.txt', encoding='utf-8') as f:
        for line in f:
            saved_login, saved_password = line.split(':')
            if login == saved_login:
                return saved_password.strip()

        
def registration():
    print('Регистрация нового пользователя')
    while True:
        login = input('Пожалуйста, введите логин (от 3 до 20 символов): ')
        assert 3 <= len(login) <= 20, 'Некорректный логин'
        password = input('Введите пароль: ')
        assert 4 <= len(password) <= 32, 'Некорректный пароль'
        if comp_data(login):
            print('Пользователь уже зарегистрирован')
            break
        else:
            write(login, password)
            break


def authorization():
    print('Авторизация пользователя')
    while True:
        login = input('Введите логин: ')
        if not comp_data(login):
            print('Такого пользователя не существует')
            break
        password = input('Введите пароль: ')
        saved_password = comp_data(login)
        if password == saved_password:
            print('Авторизация успешна')
            break
        print('Неправильный пароль')


def input_data():
    reg = '1'
    auth = '2'
    while True:
        reg_or_auth = input("'1' - для регистрации, '2' - для авторизации: ")
        if reg_or_auth == reg:
            registration()
        elif reg_or_auth == auth:
            authorization()
        else:
            print('Некорректный ввод')


def main():
    print("Привет! Выбери дейстивие:")
    input_data()


while True:
    try:
        main()
    except AssertionError:
        print('Логин должен быть от 3 до 20 символов, а пароль должен быть от 4 до 32 символов')


if __name__ == '__main__':
    main()
