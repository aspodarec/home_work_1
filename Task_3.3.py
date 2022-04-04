input_1 = float(input("Введите значение:"))
input_2 = float(input("Введите второе значение:"))
input_3 = float(input("Введите третье значение:"))


def my_func(n_1, n_2, n_3):
    list = [n_1, n_2, n_3]
    max_1 = max(n_1, n_2, n_3)
    max_index = list.index(max_1)
    list.pop(max_index)
    max_2 = max(list)
    return max_1 + max_2


print(my_func(input_1, input_2, input_3))
