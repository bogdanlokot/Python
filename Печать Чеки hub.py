one_ten = {1: 'Первый', 2: 'Второй', 3: 'Третий', 4: 'Четвертый', 5: 'Пятый', 6: 'Шестой', 7: 'Седьмой', 8: 'Восьмой', 9: 'Девятый', 10: 'Десятый'}

num_order = int(input('Введите количество заказов: '))
count = 1
order_dict = dict()

for i in range(num_order):
    order = list(input('{} заказ: '.format(one_ten[count])).split())
    count += 1
    if order[0] in order_dict.keys() and order[1] in order_dict[order[0]].keys():
        order_dict[order[0]][order[1]] += int(order[2])
    elif order[0] in order_dict.keys():
        order_dict[order[0]][order[1]] = int(order[2])
    else:
        order_dict[order[0]] = {order[1]:int(order[2])}

for i_key, i_value in order_dict.items():
    print(i_key + ':')
    for j_key, j_value in i_value.items():
        print(7*' ', j_key + ':', j_value)
