# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
n = ''
a = 0
ph = ''
e = ''
postal_code = 0
postal_address = ''
i = ''
# information about the entrepreneur
ogrnip = 0
inn = 0
payment_account = 0
bank = ''
bik = 0
correspondent_account = 0


def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, i_parameter, postal_code_parameter, postal_address_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19: years_parameter = 'лет'
    elif a_parameter % 10 == 1: years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4: years_parameter = 'года'
    else: years_parameter = 'лет'


    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Индекс:', postal_code_parameter)
    print('Адрес: ', postal_address_parameter)
    if i:
            print('')
            print('Дополнительная информация:')
            print(i_parameter)

def index():
    index_result = ''
    index_input = input('Введите почтовый индекс: ')
    for i in index_input:
        if '0' <= i <= '9':
            index_result += i
    return int(index_result)

def check_ogrnip():
    count = 0
    ogrnip_input = int(input('Введите ОГРНИП: '))
    ogrnip_result = ogrnip_input
    while ogrnip_input > 0:
        ogrnip_input //= 10
        count += 1
    if count == 15:
        return ogrnip_result
    else:
        print('ОГРНИП должен содержать 15 цифр')
        return check_ogrnip()

def check_payment_account():
    count = 0
    payment_account_input = int(input('Введите расчетный счет: '))
    payment_account_resalt = payment_account_input
    while payment_account_input > 0:
        payment_account_input //= 10
        count += 1
    if count == 20:
        return payment_account_resalt
    else:
        print('Расчетный счет должен содержать 20 цифр')
        return check_payment_account()

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
            break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                n = input('Введите имя: ')
                while 1:
                        # validate user age
                        a = int(input('Введите возраст: '))
                        if a > 0:
                            break
                        print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ph = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        ph += ch


                e = input('Введите адрес электронной почты: ')
                postal_code = index()
                postal_address = input('Введите почтовый адрес (без индекса): ')
                i = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # information about the entrepreneur
                ogrnip = check_ogrnip()
                inn = int(input('Введите ИНН: '))
                payment_account = check_payment_account()
                bank = input('Введите название банка: ')
                bik = int(input('Введите БИК: '))
                correspondent_account = int(input('Введите корреспондентский счет: '))
            else: print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(n, a, ph, e, i, postal_code, postal_address)

            elif option2 == 2:
                general_info_user(n, a, ph, e, i, postal_code, postal_address)

                # information about the entrepreneur
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:', ogrnip)
                print('ИНН:   ', inn)
                print('Банковские реквизиты')
                print('Р/с:   ', payment_account)
                print('Банк:  ', bank)
                print('К/с:   ', correspondent_account)
            else:   print('Введите корректный пункт меню')
    else:       print('Введите корректный пункт меню')