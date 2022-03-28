number = input('введите число')
number_1 =f'{number}{number}'
number_2 =f'{number_1}{number}'
result = int(number) + int(number_1) + int(number_2)
print(f'{number} + {number_1} + {number_2} = {result}')