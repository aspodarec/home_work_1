input_1 = float(input("Введите значение:"))
input_2 = float(input("Введите второе значение:"))


def my_sum(arg_1, arg_2):
    try:
        result = arg_1 / arg_2
        return result
    except ZeroDivisionError:
        return "Деление на 0 запрещено"


print(my_sum(input_1, input_2))
