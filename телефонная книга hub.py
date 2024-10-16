phone_dict = {
    ('Ваня', 'Петров'): 8800349523,
    ('Петя', 'Иванов'): 8800123435,
    ('Ирина', 'Васильева'): 8800212314
}

def invitation():
    print('Введите номер действия:')
    print(' 1. Добавить контакт ')
    print(' 2. Найти человека')
    select_num = int(input())
    if select_num == 1:
        enter()
    if select_num == 2:
        target_surname = input('Введите фамилию для поиска: ').lower()
        search_surname(target_surname)

def enter():
    name_surname = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split(' '))
    if nam_sur(name_surname):
        print('Такой человек уже есть в контактах.')
        print('Текущий словарь контактов:', phone_dict)
        invitation()
    else:
        phone = int(input('Введите номер телефона: '))
        phone_dict[name_surname] = phone
        print('Текущий словарь контактов:', phone_dict)
        invitation()

def nam_sur(full_name):
    for i in phone_dict.keys():
        if full_name == i:
            return True

def search_surname(surname):
    for i_persan in phone_dict:
        if surname.title() in i_persan:
            print(i_persan[0], i_persan[1], phone_dict[i_persan])
    invitation()

invitation()
