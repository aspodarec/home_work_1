my_list = [8, 9, 8, 4, 4, 2]
n_el = True
print('Для получения рейтинга введите число')
while n_el:
    try:
        n_el = int(input('Введите новое значение:'))
    except ValueError:
        print('ошибка ввода!')
        continue
    if not n_el: exit()
    my_list.append(n_el)
    my_list.sort(reverse=True)
    print('Результат:', ', '.join(map(str,my_list)))