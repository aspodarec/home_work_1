from functools import reduce


def my_values(el_p, el):
    return el_p * el

print(f'Четные значение от 100 до 1000 {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Перемножение всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')