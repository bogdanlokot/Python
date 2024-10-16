peop_count = int(input('Кол-во человек: '))
peoples = list(range(1,peop_count+1))
k_count = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый {}-й человек'.format(k_count))
start = 0
minus_people = k_count - 1

while len(peoples) > 1:
    if minus_people >= len(peoples):
        minus_people = (start + k_count - 1) % len(peoples)
    print('Текущий круг людей:', peoples)
    print('Начало счёта с номера', peoples[start])
    print('Выбывает человек под номером', peoples[minus_people])
    peoples.remove(peoples[minus_people])
    start = minus_people
    if start >= len(peoples):
        start = start - len(peoples)
    minus_people += k_count - 1
print()
print('Остался человек под номером', peoples[0])
