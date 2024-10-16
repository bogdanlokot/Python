abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))


def caesar_cipher(a):
    for letter in abc:
        if shift + abc.index(a) >= len(abc):
            return abc[(shift + abc.index(a)) % len(abc)]
        elif letter == a:
            return abc[abc.index(a)+shift]

text = [caesar_cipher(i) if i in abc else i for i in text]

print('Зашифрованное сообщение:', ''.join(text))
