number = int(input('Введите значение выручки:'))
number_1 = int(input('Введите значение издержек:'))
number_2 = number - number_1
access = True
if number_2 > number_1:
    print(f'Прибыль состовила {number_2}')
    profitability = number_2 / number
    n = int(input('Введите количество сотрудников:'))
    number_4 = number_2 / n
    print(f'Прибыль на одного сотрудника составила: {number_4}')
else:
    print('Убыток')
