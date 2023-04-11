reg = '1'
auth = '2'


def create_file(file_name):
    try:
        with open(file_name, 'x', encoding='utf-8') as f:
            print(f'Файл {file_name} успешно создан')
    except FileExistsError:
        print(f'Файл {file_name} уже есть')


def write_file(file_name, login, password):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f'{login}:{password}\n')
        print('Пользователь успешно зарегистрирован')


def check_file(file_name, login):
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            saved_login, saved_password = line.split(':')
            if login == saved_login:
                return saved_password.strip()


def intro_logpass(file_name):
    login = input('Пожалуйста, введите логин: ')
    password = input('Введите пароль: ')
    return login, password


def test_log(file_name):
    login, password = intro_logpass(file_name)
    while True:
        assert 3 <= len(login) <= 20, 'Некорректный логин'
        assert 4 <= len(password) <= 32, 'Некорректный пароль'
        if check_file(file_name, login):
            print('Пользователь уже зарегистрирован')
            break
        write_file(file_name, login, password)
        break


def test_pass(file_name):
    login, password = intro_logpass(file_name)
    while True:
        if not check_file(file_name, login):
            print('Такого пользователя не существует')
            break
        saved_password = check_file(file_name, login)
        if password == saved_password:
            print('Авторизация успешна')
            break
        print('Неправильный пароль')


def registration(file_name):
    print('Регистрация нового пользователя')
    test_log(file_name)


def authorization(file_name):
    print('Авторизация пользователя')
    test_pass(file_name)


def entry_data(file_name):
    while True:
        reg_or_auth = input("'1' - для регистрации, '2' - для авторизации: ")
        if reg_or_auth == reg:
            registration(file_name)
        elif reg_or_auth == auth:
            authorization(file_name)
        else:
            print('Некорректный ввод')


def main():
    file_name = input('Введите имя файла для хранения: ')
    create_file(file_name)
    print("Привет! Выбери дейстивие:")
    entry_data(file_name)


while True:
    try:
        main()
    except AssertionError:
        print('Логин должен быть от 3 до 20 символов, а пароль должен быть от 4 до 32 символов')


if __name__ == '__main__':
    main()
