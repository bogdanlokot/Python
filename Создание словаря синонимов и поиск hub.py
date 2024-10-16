num_word = int(input('Введите количество пар слов: '))

def synonym():
    word = input('Введите слово: ').lower()
    if word.title() in synonyms_dict.keys():
        print('Синоним:', synonyms_dict[word.title()])
        return
    else:
        print('Такого слова в словаре нет.')
        synonym()

synonyms_dict = dict()
synonyms_list = []
count = 1
for _ in range(num_word):
    synonyms = input('{} пара: '.format(count)).split()
    count += 1
    synonyms_list += synonyms
    synonyms_list.pop(len(synonyms_list)-2)

for i in range(0,len(synonyms_list)-1,2):
    synonyms_dict[synonyms_list[i]] = synonyms_list[i+1]
    synonyms_dict[synonyms_list[i+1]] = synonyms_list[i]

synonym()
