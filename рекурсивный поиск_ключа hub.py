site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
def search(struct, key):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = search(sub_struct, key)
            if result:
                break
    else:
        result = None
    return result

find_key = input('Введите ключ: ')
value_key = search(site, find_key)
if value_key:
    print(value_key)
else:
    print('Нет такого ключа')