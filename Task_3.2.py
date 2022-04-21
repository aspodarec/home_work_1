a = input("Имя:")
b = input("Фамилия:")
c = input("Год рождения:")
k = input("Город:")
l = input("Почта:")
p = input("Телефон:")


def my_func(**kwargs):
    return kwargs


print(my_func(name=a, last_name=b, year=c, city=k, email=l, phone=p))
