num_list = []
count_num = int(input('Кол-во чисел: '))
for _ in range(count_num):
    number = input('Число: ')
    num_list.append(number)
print()
print('Последовательность:', num_list)
add_list = []
count = 0
if num_list != list(reversed(num_list)):
    num_list.append(num_list[0])
    add_list.insert(0, num_list[0])
    count += 1
    if num_list != list(reversed(num_list)):
        for i in range(1,count_num):
            num_list.insert(count_num,num_list[i])
            add_list.insert(0,num_list[i])
            count += 1
            if num_list == list(reversed(num_list)):
                break
    print('Нужно приписать чисел:', count)
    print('Сами числа:', add_list)
else:
    print('Симметричная последовательность')

