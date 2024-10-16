goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код
total_qtt = 0
total_price = 0

for i_article in goods.keys():
    for j_article in store.keys():
        if goods[i_article] == j_article:
            for i in range (0,len(store[j_article])):
                total_qtt += store[j_article][i]['quantity']
                total_price += store[j_article][i]['price'] * store[j_article][i]['quantity']
            print(i_article, '- {} штук, стоимость {} рублей'.format(total_qtt, total_price))
            total_qtt = 0
            total_price = 0
